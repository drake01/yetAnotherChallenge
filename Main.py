'''
* ABOUT: The code in this file is an attempt to solve a challenge
pre-requisite for a job opportunity.
This code was tested on a machine running Python 2.7.3 GNU/Linux

* HOW TO USE: python <name of this file> should do the magic.
  (Instead of python use python2, if there is any problem)
'''
import urllib2
import json


def Magic():
    '''
    Magic Function : This function does all the magic; hence the name.
    '''
    url = "http://www.letsrevolutionizetesting.com/challenge"
    header = {'User-Agent': 'Mozilla/5.0'}
    ctr = 0
    while True:
        try:
            url = url.replace("challenge", "challenge.json")
            ctr += 1
            # Added header in Request call to fake the user-agent.
            req = urllib2.Request(url, headers=header)
            res = urllib2.urlopen(req)
            # expecting the response to be a valid json
            magicObj = json.load(res)
            # Expecting the magicObj to have member corresponding to
            # 'follow' key. Last one of this contraption doesn't.
            url = magicObj['follow']
            print("Currently fetching ({}) : {}".format(ctr, url))
        except KeyError:
            # Dumping The Final one
            print("Finallly  fetched  ({}) : {}".format(ctr, magicObj))
            # print("Finallly  fetched ({}) : {}".format(ctr, magicObj['message']))
            break

if __name__ == '__main__':
    # Do the magic
    Magic()
