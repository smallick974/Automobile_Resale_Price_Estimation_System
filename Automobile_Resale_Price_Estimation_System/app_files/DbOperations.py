'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

from app_files.DbConUtil import connectDB

def insertData(tableName,dataDict):
    con,cursor = connectDB()
    query = "insert into mca." + tableName + " (" + ",".join(dataDict.keys()) + ")"  + " values (" + ",".join(["%s"] * len(dataDict.keys())) + " ) "
    print(query)
    cursor.executemany(query,(list(dataDict.values()),))
    con.commit()
    cursor.close()
    con.close()
    

def updateData(tableName,updateDict,idDict):
    con,cursor = connectDB()
    query = "update mca." + tableName + " set " + "" + " , ".join(name +" = " +"'"+updateDict[name]+"'" for name in updateDict) + " where "+" and ".join(idn +" = " + "'" + idDict[idn] + "'" for idn in idDict)
    print(query)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    
    
def searchData(tableName,columnName,dictName):
    con,cursor = connectDB()
    query = "select " + ",".join(columnName) +" from mca."+ tableName +" where " + " and ".join(name +" = " +"'"+dictName[name]+"'" for name in dictName)
    print('query>> ',query)
    cursor.execute(query)
    data = cursor.fetchall()
    return data
    con.commit()
    cursor.close()
    con.close()
    pass

def deleteData(tableName,idDict):
    con,cursor = connectDB()
    query = "delete from mca." + tableName + " where "+" and ".join(idn +" = " + "'" + idDict[idn] + "'" for idn in idDict)
    print(query)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()    
    
# for debug
if __name__ == '__main__':
    pass

