'''
Created on Dec 20, 2018

@author: S528358
'''
import re

class Regex_python:
    def __init__(self,url_string=None):
        self.url_string = url_string
        
    def Validate_url(self):
        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9a-z](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,6}\.?|[a-zA-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d{2,5})?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE                
                )
        
        result = re.match(regex,self.url_string)# look for pattern in the url string

        if result is None:
            raise Exception("invalid url") #raise exception if pattern is not found in the url string
        



        