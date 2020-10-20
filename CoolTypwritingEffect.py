#So what I have here is a small bit of code that will make a sort of type writing effect in your print statements
#Im not sure how else to explain it but if you put this small bit of code at the top of your script you can have a typwriting effect on your code

import time 
import sys

def lprint(s):
    for c in s:   
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.03)
      
#then when you want it to type out letter by letter just use the created function 'lprint'
lprint ("hello, hope you have a great day")
#enjoy
