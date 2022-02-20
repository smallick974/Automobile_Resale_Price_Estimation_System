'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from datetime import datetime
from app_files.Constants import Constants

class DbUtils:
    
    def getMappedUserData(self,userFormData):
        userDataDict = {}
        if "firstname" in userFormData:
            userDataDict[Constants.FIRSTNAME] = userFormData.get("firstname")
            
        if "lastname" in userFormData:
            userDataDict[Constants.LASTNAME] = userFormData.get("lastname")
            
        if "emailid" in userFormData:
            userDataDict[Constants.EMAIL_ID] = userFormData.get("emailid")
            
        if "dob" in userFormData:
            userDataDict[Constants.DATE_OF_BIRTH] = userFormData.get("dob")
                    
        if "pass" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("pass")      
            
        if "addr_1" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_1] = userFormData.get("addr_1")
            
        if "addr_2" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_2] = userFormData.get("addr_2")
            
        if "city" in userFormData:
            userDataDict[Constants.CITY] = userFormData.get("city")
            
        if "states" in userFormData:
            userDataDict[Constants.STATE] = userFormData.get("states")
            
        if "zip" in userFormData:
            userDataDict[Constants.ZIP_CODE] = userFormData.get("zip")
            
        if "country" in userFormData:
            userDataDict[Constants.COUNTRY] = userFormData.get("country")
            
        if "contact" in userFormData:
            userDataDict[Constants.CONTACT] = userFormData.get("contact")
                   
        userDataDict[Constants.USER_LAST_LOGIN] = datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")
        
        return userDataDict
    
    
    def getMappedUserDataForUpdate(self,userFormData):
        userDataDict = {}                    
        if "pass" in userFormData:
            userDataDict[Constants.PASSWORD] = userFormData.get("pass")      
            
        if "addr_1" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_1] = userFormData.get("addr_1")
            
        if "addr_2" in userFormData:
            userDataDict[Constants.ADDRESS_LINE_2] = userFormData.get("addr_2")
            
        if "city" in userFormData:
            userDataDict[Constants.CITY] = userFormData.get("city")
            
        if "states" in userFormData:
            userDataDict[Constants.STATE] = userFormData.get("states")
            
        if "zip" in userFormData:
            userDataDict[Constants.ZIP_CODE] = userFormData.get("zip")
            
        if "country" in userFormData:
            userDataDict[Constants.COUNTRY] = userFormData.get("country")
            
        if "contact" in userFormData:
            userDataDict[Constants.CONTACT] = userFormData.get("contact")
            
        return userDataDict
    
    def getMappedCarDetails(self,carFormData):
        carDetailsDict = {}
        if "manufacturer" in carFormData:
            carDetailsDict[Constants.MANUFACTURER] = carFormData.get("manufacturer")
            
        if "model" in carFormData:
            carDetailsDict[Constants.MODEL] = carFormData.get("model")
            
        if "title_status" in carFormData:
            carDetailsDict[Constants.TITLE_STATUS] = carFormData.get("title_status")
            
        if "buildYear" in carFormData:
            carDetailsDict[Constants.BUILD_YEAR] = carFormData.get("buildYear")
        
        if "carCondition" in carFormData:
            carDetailsDict[Constants.CAR_CONDITION] = carFormData.get("carCondition")
            
        if "cylinders" in carFormData:
            carDetailsDict[Constants.CYLINDERS] = carFormData.get("cylinders")
            
        if "fuel" in carFormData:
            carDetailsDict[Constants.FUEL] = carFormData.get("fuel")
            
        if "odometer" in carFormData:
            carDetailsDict[Constants.ODOMETER] = carFormData.get("odometer")
            
        if "transmission" in carFormData:
            carDetailsDict[Constants.TRANSMISSION] = carFormData.get("transmission")
            
        if "VIN" in carFormData:
            carDetailsDict[Constants.VIN] = carFormData.get("VIN")
            
        if "carSize" in carFormData:
            carDetailsDict[Constants.CARSIZE] = carFormData.get("carSize")
            
        if "carType" in carFormData:
            carDetailsDict[Constants.CARTYPE] = carFormData.get("carType")
            
        if "paint_color" in carFormData:
            carDetailsDict[Constants.PAINT_COLOR] = carFormData.get("paint_color")    
            
        if "description" in carFormData:
            carDetailsDict[Constants.DESCRIPTION] = carFormData.get("description")
            
        if "states" in carFormData:
            carDetailsDict[Constants.STATES] = carFormData.get("states")
            
        if "image_url" in carFormData:
            carDetailsDict[Constants.IMAGE_URL] = carFormData.get("image_url")
            
        if "price" in carFormData:
            carDetailsDict[Constants.PRICE] = carFormData.get("price")
            
        if "drive" in carFormData:
            carDetailsDict[Constants.DRIVE] = carFormData.get("drive")
            
        if "userId" in carFormData:
            carDetailsDict[Constants.USER_ID] = carFormData.get("userId")
            
        carDetailsDict[Constants.POSTING_DATE] = datetime.now()

        return carDetailsDict
    
    
    def getMappedCarDetailsForUpdate(self,carFormData):
        carDetailsDict = {}                 
        if "description" in carFormData:
            carDetailsDict[Constants.DESCRIPTION] = carFormData.get("description")
                        
        if "image_url" in carFormData:
            carDetailsDict[Constants.IMAGE_URL] = carFormData.get("image_url")
            
        if "price" in carFormData:
            carDetailsDict[Constants.PRICE] = carFormData.get("price")
                                    
        return carDetailsDict
        