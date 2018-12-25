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
        string='https://linkprotect.cudasvc.com/url?a=https%3a%2f%2fdrive.google.com%2ffile%2fd%2f1Issk-oEOx0aU2FydLkTw3tL4dRAg4MAE%2fview%3fusp%3dsharing&c=E,1,X5RaPKPX7FEuMVyuurBysSFT3VYsHliLZCMIvvXgNLCPagns_3vPvS35nPYqz-LrwCyBPOFpujRbu46Z57yv-RB1h2ZZN-EJcuJMPIsV37Y,&typo=1'
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