'''
Created on Dec 20, 2018

@author: S528358
'''
import unittest
import RE_python


 
class MyTest(unittest.TestCase):
    def input_url(self):            
            string = input('enter url')
            obj = RE_python.Regex_python(string)
            obj.Validate_url()

    def test1(self):
        '''successful scenario: dummy url website remembered by the code'''
        string='http://dummy.restapiexample.com/api/v1/employees'
        try:
            obj = RE_python.Regex_python(string)
            obj.Validate_url()
        except Exception as e:
            self.fail(e)
    def test2(self):        
        """
        Enter a new URL from the user
        """
        try:
            self.input_url()
        except Exception as e:
            count = 0 #keep count of invalid urls entered
            for i in range(2):
                try:
                    count = count + 1
                    self.input_url()                    
                    break
                except:
                    print(count)
                    if count == 2: #if count is 2 then raise exception and fail the case
                        self.fail(e)
                    else:
                        pass #if count is less than 2 and valid url entered then pass the case