import robotparser
import socket
import sys
from time import sleep
from urllib import FancyURLopener
import urlparse

from bs4 import BeautifulSoup

import MySql


class myOpener(FancyURLopener, object):
    version = 'Slow Web Crawler v0.1'


class Scraper():
    def __init__(self, url, urlLimit, delay):
        #self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.s.settimeout(3600)
        #self.s.connect(("localhost", 1337))

        self.sleeptime = delay
        self.limit = urlLimit
        self.url = url
        
        self.db = MySql.Database("127.0.0.1", "pythondb", "pythonUser", "pythondb")

        self.filename = self.url
        
        self.urlfile = open(self.filename + '.txt', 'wb')
        
        self.url = 'http://' + self.url
        self.urls = [self.url]
        self.counter = 0

        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(self.url + '/robots.txt')
        self.rp.read()
        print 'Set robotparser url to:', self.url + '/robots.txt'

        self.urlOpener = myOpener()
        
    def setConnection(self, host, port):
        try:
            self.s.connect(host, port)
        except:
            print "Unable to connect to host"
            sys.exit()
        print "Connected to DatabaseHandler, waiting for task..."

    def crawl(self):
        while len(self.urls) > 0:
            sleep(self.sleeptime)
            try:
                try:
                    htmltext = self.urlOpener.open(self.urls[0]).read()
                    print 'Opening:', self.urls[0]
                except:
                    print "Something went wrong while opening the url:", self.urls[0]
                self.soup = BeautifulSoup(htmltext)
                
                self.urls.pop(0)       
                
                for tag in self.soup.findAll("a", href=True):
                    tag['href'] = urlparse.urljoin(self.url, tag['href'])
                    if self.url in tag['href'] and self.checkDB(tag['href']) != True and self.rp.can_fetch('*', tag['href']):
                        self.counter += 1
                        print 'Adding:', tag['href']
                        self.urlfile.write(tag['href']  + '\n')            
                        self.addToDB(tag['href'])
                        if self.counter < self.limit:
                            self.urls.append(tag['href'])
                
                print "Urls left: " + len(self.urls)
                print "Urls found: " + self.counter

            except:
                print "Error, something went wrong!"

                                    
    def initDB(self):
        pass
                        
    def addToDB(self, url):
        q = """
        insert into pythondbtable (website, url) values ('%s', '%s');
        """ % (self.url, url)
        
        self.db.query(q)
            
            
    def checkDB(self, url):
        q = """
        select * from pythondbtable where url like '%s';
        """ % (url)
        response = self.db.query(q)
        if response:
            return True
        else:
            return False
            
    def __del__(self):
        self.urlfile.close()
