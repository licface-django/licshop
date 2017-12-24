#data = u'{"auth": "jVVvSZfm84ZdV0xRQo4JXjFtUtWpXouw0RNLKlV", "emailverified": true, "plan": 0, "cryptosubscription": false, "quota": 17179869184, "cryptosetup": false, "result": 0, "userid": 3234671, "premium": false, "usedquota": 112074469, "language": "en", "business": false, "email": "todut001@gmail.com", "registered": "Wed, 07 Oct 2015 21:47:29 +0000"}'

# print "data =", data

# from ast import literal_eval
# from collections import MutableMapping

# my_dict = literal_eval(data)
# assert isinstance(my_dict, MutableMapping)
# d = eval(data)
# print "d =", d
#import json
#result = json.loads(data)
#print result
#print type(result)

#class A(object):
    #def __init__(self):
        #super(A, self)
        
    #def test1(self, data):
        #key = ''
        #def getdata():
            #if data == 'post':
                #key = 'data is POST'
                #return key
            #else:
                #key = 'data is GET'
                #return key
                
        #key = getdata()
        #print "KEY =", key
#if __name__ == '__main__':
    #c = A()
    #c.test1('post')
    
#from tqdm import tqdm
#import time
#for i1 in tqdm(range(5)):
    #for i2 in tqdm(range(300)):
        ## do something, e.g. sleep
        #time.sleep(0.01)
        
#import progressbar, time, sys

#def up():
    ## My terminal breaks if we don't flush after the escape-code
    #sys.stdout.write('\x1b[1A')
    #sys.stdout.flush()

#def down():
    ## I could use '\x1b[1B' here, but newline is faster and easier
    #sys.stdout.write('\n')
    #sys.stdout.flush()

## Total bar is at the bottom. Move down to draw it
#down()
#total = progressbar.ProgressBar(maxval=50)
#total.start()

#for i in range(1,51):
    ## Move back up to prepare for sub-bar
    #up()

    ## I make a new sub-bar for every iteration, thinking it could be things
    ## like "File progress", with total being total file progress.
    #sub = progressbar.ProgressBar(maxval=50)
    #sub.start()
    #for y in range(51):
        #sub.update(y)
        #time.sleep(0.005)
    #sub.finish()

    ## Update total - The sub-bar printed a newline on finish, so we already
    ## have focus on it
    #total.update(i)
#total.finish()

from progressbar import ProgressBar

class Writer(object):
    """Create an object with a write method that writes to a
    specific place on the screen, defined at instantiation.

    This is the glue between blessings and progressbar.
    """
    def __init__(self, location):
        """
        Input: location - tuple of ints (x, y), the position
                        of the bar in the terminal
        """
        self.location = location

    def write(self, string):
        with term.location(*self.location):
            print(string)
            
#from blessings import Terminal

#term = Terminal()

#location = (0, 10)
#text = 'blessings!'
#print term.location(*location), text

## alternately,
#with term.location(*self.location):
    #print text

def test_function(location):
    writer = Writer(location)
    pbar = ProgressBar(fd=writer)
    pbar.start()
    for i in range(100):
        # mimic doing some stuff
        time.sleep(0.01)
        pbar.update(i)
    pbar.finish()

#x_pos = 0  # zero characters from left
#y_pos = 10  # ten characters from top
#location = (x_pos, y_pos)
#test_function(location)

def test10():
    a = 1
    while 1:
        if not a == 20:
            a += 1
            print "a1 =", a
            if a == 10:
                print "a2 =", a
                return a
        else:
            break
        
test10()