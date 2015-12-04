'''
Created on 04.12.2015

@author: maxdriller
'''

import urllib2

req = urllib2.Request("https://en.wikipedia.org/wiki/Lambda_phage")

try:
    fetch = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except urllib2.URLError as e:
    print 'Couldn\'t reach the server.'
    print e.reason

html = fetch.read()

print html