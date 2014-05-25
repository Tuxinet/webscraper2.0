import MySQLdb

class Database:
    
    def __init__(self, host, database, user, password):
        self.connection = MySQLdb.connect( host = host,
                                           user = user,
                                           passwd = password,
                                           db = database )
        
    def query(self, q):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)
        self.connection.commit()
        
        return cursor.fetchall()
    
    def __del__(self):
        self.connection.close()