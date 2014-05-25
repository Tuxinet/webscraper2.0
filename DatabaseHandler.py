import socket

import MySql


class DatabaseHandler:
    def __init__(self):
        self.dbHost = raw_input("Please enter the dbHost to the database: ")
        self.database = raw_input("Please enter the database name: ")
        self.dbUser = raw_input("Please enter username: ")
        self.dbPasswd = raw_input("Please enter the password: ")
        
        self.database = MySql.Database(self.dbHost, 
                                       self.database, 
                                       self.dbUser, 
                                       self.dbPasswd)
        
        PORT = raw_input("Please enter the port you wish to use: ")
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def idle(self):
        pass
        

    def addToDB(self, url):
        pass
    
    def checkDB(self, url):
        q = "select url from %s where url = %s" % (self.database, url)
        response = self.database.query(q)
        if response:
            return True
        else: 
            return False


if __name__ == '__main__':
    url = raw_input("Input url: ")
    limit = input("Input number of urls to visit: ")
