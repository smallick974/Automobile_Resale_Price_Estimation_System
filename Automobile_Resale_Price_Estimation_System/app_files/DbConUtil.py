'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

# returns a dictionary based on database.ini file

from configparser import ConfigParser
import psycopg2

# get section and update dictionary with connection string key:value pairs
def config(conf_file='database.ini', section='db_connection'): 
    parser = ConfigParser()  # to parse database configuration file   
    parser.read(conf_file)   # read database.ini file    
    try:
        db = {}
        if section in parser:
            for key in parser[section]:
                db[key] = parser[section][key]           
        return db  
    except Exception as e:
            print(e)
            
# connect to PostgreSQL database         
def connectDB():
    try:
        print('\n')
        dbValues = config()
        port = dbValues['port']
        username = dbValues['username']
        password = dbValues['password']
        hostname = dbValues['hostname']        
        database = dbValues['database']
        
        con = psycopg2.connect(host=hostname, database=database, user=username, password=password, port=port)
        cursor = con.cursor()
        return con,cursor          
    except Exception as e:
        print(e)
        