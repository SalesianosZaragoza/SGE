#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
from string import join

class FunWithSnow:
    
    def isPalindrome(self, str):
        
        str.replace(" ", "")
        
        return True if str[::-1].lower() == str.lower() else False
            
    
    def reverseString(self, list):
        
        for index in range (len(list)):
            
            list[index] = list[index][::-1]
        
        return join(list)
    
    def reverseList(self, list):
        
        list.reverse()
        
        return list

