""" connecting to postgreSQL using psycopg2 """
import psycopg2

class PostgresConnect:
    
    dbname = 'connection_test'
    user = 'kevinwatt'
    password = ''
    host = '127.0.0.1'
    port = 5432
    
    
    def __init__(self, dbname=dbname, user=user, password=password,
        host=host, port=port):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.conn = self._create_connection(dbname, user, password, 
                        host, port)
        
        
    def __repr__(self):
        """ prints the dbname@host,port"""
        return f'{self.dbname}@{self.host},{self.port}'
        
        
    def _create_connection(self, dbname, user, password, host, port):
        """ this is a file """
        return psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port)


    def _create_cursor(self):
        """ returns a cursor of the given class """
        return self.conn.cursor()
    
    
    def query(self, sql):
        """ factory function to create cursor and execute query safely """
        with self._create_cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
	    
    def bulk_insert(self, table_name, values):
	""" use the execute many function to insert many records """
		sql = f'INSERT INTO {self.dbname}({table_name}) VALUES({values})'
		with self._create_curosr() as cur:
			cur.executemany(sql, values)
			self.conn.commit()
