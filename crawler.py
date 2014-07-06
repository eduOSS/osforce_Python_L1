#!/usr/bin/python
#coding:utf8

__author__ = ['markshao']

import signal
import multiprocessing
import shutil
import Queue
import httplib
import urllib
from optparse import OptionParser
import time
import sys

import os
from BeautifulSoup import BeautifulSoup


BOOK_DOUBAN = "book.douban.com"
BASE_URl = "/tag/"

PAGE = 20

default_dir = os.path.abspath(os.path.join(os.path.curdir, "douban"))
option_parser = OptionParser()
option_parser.add_option("-d", "--destination",
                         action="store", type="string", dest="destination", default=default_dir)
option_parser.add_option("-p", "--process",
                         action="store", type="int", dest="process", default=multiprocessing.cpu_count())
option_parser.add_option("-s", "--sleep", action="store", type="int", dest="sleep", default=60 * 3
)


class CrawlerTask(multiprocessing.Process):
    def __init__(self, tid, host, base_url, parent_destination, task_queue, task_sleep):
        super(CrawlerTask, self).__init__()
        self.tid = tid
        self.host = host
        self.parent_destination = parent_destination
        self.task_queue = task_queue
        self.sleep = task_sleep
        self.base_url = base_url

        self.httpConnection = httplib.HTTPConnection(self.host)

        print "start the process %s" % self.tid

    def run(self):
        current_time = time.time()
        task = self.task_queue.get()
        while (task):
            # do the task
	    task_folder = os.path.join(self.parent_destination, task)
            if not os.path.exists(task_folder):
                os.makedirs(task_folder)

            start = 0
            while True:
                # decide whether need to sleep
                if time.time() - current_time > self.sleep:
                    time.sleep(10)
                    print "It's time to sleep"
                    current_time = time.time()

                urlparam = urllib.urlencode({"start": start, "type": "T"})
                url = self.base_url + task.encode('gb2312')+ "?" + urlparam
                soup ,response = None,None
                try:
                    self.httpConnection.request("GET", url)
                    response = self.httpConnection.getresponse()
                    soup = BeautifulSoup(response.read())
                except:
                    print "Fail to download the subtask [%s] and rebuild the connection" % task
                    self.httpConnection.close()
                    self.httpConnection = httplib.HTTPConnection(self.host) # reconnect
                    continue

                items = soup.findAll("li", {"class": "subject-item"})
                if not items or len(items) == 0:
                    break  # the subtask has been finished
                else:
                    for item in items:
                        img = item.find("div", {"class": "pic"}).find("img")
                        src = img["src"]
                        file_name = src[src.rfind("/") + 1:]
                        img_path = os.path.join(task_folder,file_name)
                        try:
                            urllib.urlretrieve(src,img_path)
                            print "successfully download [%s]" % img_path
                        except:
                            pass

		    time.sleep(0.5)
            try:
                task = self.task_queue.get_nowait()
            except Queue.Empty:
                print "no task in the queue"
            finally:
                self.httpConnection.close()



def main():
    options, args = option_parser.parse_args()

    if os.path.exists(options.destination):
        shutil.rmtree(options.destination)

    os.makedirs(options.destination)

    task_queue = multiprocessing.Queue(options.process)
    http_connection = None


    # create the task
    tasks = {}
    for i in range(options.process):
        crawler_task = CrawlerTask(i, BOOK_DOUBAN, BASE_URl, options.destination, task_queue, options.sleep)
        tasks[i] = crawler_task
        crawler_task.start()

    # add task into the queue
    try:
        print "Collect the task from master"
        http_connection = httplib.HTTPConnection(BOOK_DOUBAN)
        http_connection.request("GET", BASE_URl)
        response = http_connection.getresponse()
        soup = BeautifulSoup(response.read())
        for td in soup.findAll("td"):
            href = td.find("a")["href"]
            if href.startswith("./"):
                task_queue.put(href[2:])
                print "add task [%s] into the queue" % href[2:]

    except httplib.HTTPException:
        sys.stderr.write("The [%s] not accessible" % BOOK_DOUBAN)
        sys.exit(1)
    finally:
        if not http_connection:
            http_connection.close()

    def signal_action(*args,**kwargs):
         for tid, task in tasks.items():
            task.terminate()

    #signal.signal(signal.SIGKILL,signal_action)


if __name__ == "__main__":
    main()
