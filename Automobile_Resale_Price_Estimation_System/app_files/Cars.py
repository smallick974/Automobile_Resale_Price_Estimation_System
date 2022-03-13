'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from app_files.DbUtils import DbUtils
from app_files.Constants import Constants
from app_files.DbOperations import insertData, updateData, deleteData, searchData, getCarDetailsWithImage


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
        
    def getCarManufacturer(self,isactive):
        idDict = {}
        if isactive=='true':
            idDict[Constants.IS_ACTIVE] = 'true'
        car_manufacturer_list = searchData(Constants.TABLE_CAR_MANUFACTURER,'*',idDict)
        return car_manufacturer_list
    
    def getCarModels(self,mid):
        idDict = {}
        idDict[Constants.MANUFACTURER_ID] = mid
        idDict[Constants.IS_ACTIVE] = 'true'
        car_models_list = searchData(Constants.TABLE_CAR_MODEL,'*',idDict)
        return car_models_list
    
    def getCars(self):
        #car_list = searchData(Constants.TABLE_CAR_DETAILS,[Constants.MANUFACTURER,Constants.MODEL,Constants.PRICE],{})
        car_list = getCarDetailsWithImage()
        print(car_list)
        return car_list
            