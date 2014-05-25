import MySQLdb
import MySql

def main():
    while True:
        try:
            q = raw_input("Please enter MySql query: ")
            response = db.query(q)
            
            for element in response:
                print element
        except:
            print 'Query invalid or server unreachable!'
            
if __name__ == '__main__':
    db = MySql.Database("localhost", "pythondb", "pythonUser", "pythondb")
    main()
