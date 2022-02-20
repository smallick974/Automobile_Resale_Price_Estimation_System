'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from app_files.DbUtils import DbUtils
from app_files.Constants import Constants
from app_files.DbOperations import insertData, updateData, deleteData

class Cars:
    
    def newCar(self,carFormData):
        carDetailDict = DbUtils().getMappedCarDetails(carFormData)
        insertData(Constants.TABLE_CAR_DETAILS,carDetailDict)
    
    def updateCar(self,carFormData):
        carDetailDict = DbUtils().getMappedCarDetailsForUpdate(carFormData)
        idDict = {}
        idDict[Constants.USER_ID] = carFormData.get("userid")
        idDict[Constants.CAR_ID] = carFormData.get("carid")
        updateData(Constants.TABLE_CAR_DETAILS, carDetailDict, idDict)
    
    def deleteCar(self,carFormData):
        idDict = {}
        idDict[Constants.USER_ID] = carFormData.get("userid")
        idDict[Constants.CAR_ID] = carFormData.get("carid")
        deleteData(Constants.TABLE_CAR_DETAILS, idDict)
        
        
    def deleteCarImage(self,carFormData):
        idDict = {}
        idDict[Constants.IMAGE_ID] = carFormData.get("imageid")
        deleteData(Constants.TABLE_CAR_IMAGE, idDict)