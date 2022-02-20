'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

from app_files.DbOperations import insertData, searchData, updateData, deleteData
from app_files.DbUtils import DbUtils
from app_files.Constants import Constants

class Users:

    def userSignUp(self,userFormData):
        useremaildict = {}
        useremaildict[Constants.EMAIL_ID] = userFormData["emailid"]
        emailid = searchData(Constants.TABLE_USER_DETAILS,[Constants.EMAIL_ID],useremaildict)
        try:
            if len(emailid) != 0:
                raise ValueError
            else:
                dbUtil = DbUtils()
                userDataDict = dbUtil.getMappedUserData(userFormData)
                insertData(Constants.TABLE_USER_DETAILS,userDataDict)
                print('inserted message>>')
        except ValueError:
            print("This Email ID already exists..")
    
    
    def userLogin(self,userFormData):
        dbUtil = DbUtils()
        loginDict = dbUtil.getMappedUserData(userFormData) 
        credDict = {} 
        credDict[Constants.EMAIL_ID] = loginDict["emailid"]    
        credDict[Constants.PASSWORD] = loginDict["pass"]
        data = searchData(Constants.TABLE_USER_DETAILS,[Constants.EMAIL_ID],credDict)
        try:
            if len(data) == 0:
                raise ValueError
            else:
                timestampDict = {}
                timestampDict[Constants.USER_LAST_LOGIN] = loginDict[Constants.USER_LAST_LOGIN]
                updateData(Constants.TABLE_USER_DETAILS,timestampDict,credDict)
                print("LogIn Successful..")
        except ValueError:
            print("Email ID or Password Incorrect..")
    
    
    def userUpdate(self,userFormData):
        userDetails = DbUtils().getMappedUserDataForUpdate(userFormData)
        idDict = {}
        idDict[Constants.USER_ID] = userFormData.get("userid") 
        try:       
            updateData(Constants.TABLE_USER_DETAILS,userDetails,idDict)
        except Exception as e:
            print(e)
        print('Data update>> ')
        
    def deleteUser(self,userFormData):
        idDict = {}
        idDict[Constants.USER_ID] = userFormData.get("userid")
        try:
            deleteData(Constants.TABLE_USER_DETAILS, idDict)
        except Exception as e:
            print(e)
        
        