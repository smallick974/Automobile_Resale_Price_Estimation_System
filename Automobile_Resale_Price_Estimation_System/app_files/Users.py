'''
Created on 19-Feb-2022

@author: Srijan-PC
'''

from app_files.DbOperations import insertData, searchData, updateData, deleteData
from app_files.DbUtils import DbUtils
from app_files.Constants import Constants

class Users:

    def userSignUp(self,userFormData):
        print('USER FORM DATA: ',userFormData)
        useremaildict = {}
        useremaildict[Constants.EMAIL_ID] = userFormData["txt_email_id"]
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
        except Exception as e:
            print("Exception: ",e)    
    
    
    def userLogin(self,userFormData):
        print("userFormData: ",userFormData)
        dbUtil = DbUtils()
        loginDict = dbUtil.getMappedUserData(userFormData) 
        credDict = {} 
        credDict[Constants.EMAIL_ID] = loginDict["emailid"]    
        credDict[Constants.PASSWORD] = loginDict["pass"]
        firstName = searchData(Constants.TABLE_USER_DETAILS,[Constants.FIRSTNAME,Constants.EMAIL_ID,Constants.USER_LAST_LOGIN],credDict)
        try:
            if len(firstName) == 0:
                raise ValueError
            else:
                timestampDict = {}
                timestampDict[Constants.USER_LAST_LOGIN] = loginDict[Constants.USER_LAST_LOGIN]
                updateData(Constants.TABLE_USER_DETAILS,timestampDict,credDict)
                return firstName
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
            
    def displayProfile(self,emailid):
        emailDict={}
        emailDict[Constants.EMAIL_ID] = emailid    
        profiledata = searchData(Constants.TABLE_USER_DETAILS,[Constants.FIRSTNAME,Constants.LASTNAME,Constants.EMAIL_ID,Constants.CONTACT,Constants.DATE_OF_BIRTH,Constants.ADDRESS_LINE_1,Constants.ADDRESS_LINE_2,Constants.CITY,Constants.STATE,Constants.ZIP_CODE,Constants.COUNTRY],emailDict)
        try:
            if len(profiledata) == 0:
                raise ValueError
            else:
                return profiledata
        except ValueError:
            print("No Data Found..")
        pass        
        
        