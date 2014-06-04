#!/usr/bin/python
#!coding:utf8

def isPalindrome(s):
    s1 = s[::-1]
    if cmp(s,s1):
	print s + ' is not palindrome'
    else:
	print s + ' is palindrome'
i = isPalindrome

i("palindromeemordnilap")
i("palindrome")
