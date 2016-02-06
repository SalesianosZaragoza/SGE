#!/usr/bin/python
# -*- coding: utf-8 -*-


class FunWithSnow:

    def isPalindrome(self, str):
        str = str.lower()
        str = str.replace(' ', '')
        str = str.replace(',', '')
        str = str.replace('ñ', 'n')
        str = str.replace("á", "a")
        str = str.replace("é", "e")
        str = str.replace("í", "i")
        str = str.replace("ó", "o")
        str = str.replace("ú", "u")
        str2 = str[::-1]
        if str == str2:
            return True
        else:
            return False

    
    def reverseString(self, list):
        s2 = list.split()
        for num, word in enumerate(s2):
            s2[num] = word[::-1]
        return ' '.join(s2)
        pass
    
    def reverseList(self, list):
        for num, word in enumerate(list):
            list[num] = word[::-1]
        return ' '.join(list)
        pass
