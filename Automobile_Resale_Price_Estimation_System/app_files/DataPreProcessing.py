'''
Created on 23-Feb-2022

@author: Srijan-PC
'''

import pickle
import numpy as np
from collections import Counter

class DataPreProcessing:
    
    def __init__(self):
        self.year = "./model_files/data_processing/year_scaler"
        self.manufacturer = "./model_files/data_processing/manufacturer_onehot_encoder"
        self.model = "./model_files/data_processing/dict_model_freq"
        self.condition = "./model_files/data_processing/condition_onehot_encoder"
        self.cylinders = "./model_files/data_processing/cylinders_dict"
        self.fuel = "./model_files/data_processing/fuel_onehot_encoder"
        self.odometer = "./model_files/data_processing/odometer_scaler"
        self.transmission = "./model_files/data_processing/transmission_onehot_encoder"
        self.drive = "./model_files/data_processing/drive_onehot_encoder"
        self.cartype = "./model_files/data_processing/cartype_onehot_encoder"
        self.paint_color = "./model_files/data_processing/paint_color_ordinal_encoder"
        self.state = "./model_files/data_processing/state_ordinal_encoder"
        
    
    def preprocess_year(self,year):
        year_scaler = pickle.load(open(self.year,'rb'))
        value = year_scaler.transform(np.array(year).reshape(-1,1))
        return value
    
    def preprocess_manufacturer(self,manufacturer):
        manufacturer_onehot_encoder = pickle.load(open(self.manufacturer,'rb'))
        value = manufacturer_onehot_encoder.transform(np.array(manufacturer).reshape(-1,1))
        return value
    
    # def preprocess_model(self,model):
    #     dict_model_freq = pickle.load(open(self.model,'rb'))
    #     dict_model = dict(Counter(model))
    #     value = dict_model.map(dict_model_freq).fillna(0).astype('int64').values.reshape(-1,1)
    #     return value
    
    def preprocess_condition(self,condition):
        condition_onehot_encoder = pickle.load(open(self.condition,'rb'))
        value = condition_onehot_encoder.transform(np.array(condition).reshape(-1,1))
        return value
    #
    # def preprocess_cylinders(self,cylinders):
    #     manufacturer_onehot_encoder = pickle.load(open(self.manufacturer,'rb'))
    #     value = manufacturer_onehot_encoder.transform(np.array(manufacturer).reshape(-1,1))
    #     return value
    #
    def preprocess_fuel(self,fuel):
        fuel_onehot_encoder = pickle.load(open(self.fuel,'rb'))
        value = fuel_onehot_encoder.transform(np.array(fuel).reshape(-1,1))
        return value
    
    def preprocess_odometer(self,odometer):
        odometer_scaler = pickle.load(open(self.odometer,'rb'))
        value = odometer_scaler.transform(np.array(odometer).reshape(-1,1))
        return value
    #
    def preprocess_transmission(self,transmission):
        transmission_onehot_encoder = pickle.load(open(self.transmission,'rb'))
        value = transmission_onehot_encoder.transform(np.array(transmission).reshape(-1,1))
        return value
    #
    def preprocess_drive(self,drive):
        drive_onehot_encoder = pickle.load(open(self.drive,'rb'))
        value = drive_onehot_encoder.transform(np.array(drive).reshape(-1,1))
        return value
    
    def preprocess_cartype(self,cartype):
        cartype_onehot_encoder = pickle.load(open(self.cartype,'rb'))
        value = cartype_onehot_encoder.transform(np.array(cartype).reshape(-1,1))
        return value
    
    def preprocess_paint_color(self,paint_color):
        paint_color_ordinal_encoder = pickle.load(open(self.paint_color,'rb'))
        value = paint_color_ordinal_encoder.transform(np.array(paint_color).reshape(-1,1))
        return value
    
    def preprocess_state(self,state):
        state_ordinal_encoder = pickle.load(open(self.state,'rb'))
        value = state_ordinal_encoder.transform(np.array(state).reshape(-1,1))
        return value



    
if __name__ == '__main__':
    dp = DataPreProcessing()
    
    value = dp.preprocess_year("2017")
    print("year: ",value)
    
    value = dp.preprocess_manufacturer("toyota")
    print("manufacturer: ",value)
    
    # value = dp.preprocess_model("tundra double cab sr")
    # print("model: ",value)
    
    value = dp.preprocess_condition("good")
    print("condition: ",value)
    
    # value = dp.preprocess_cylinders("8")
    # print("cylinders: ",value)
    
    value = dp.preprocess_fuel("gas")
    print("fuel: ",value)
    
    value = dp.preprocess_odometer("41124")
    print("odometer: ",value)
    
    value = dp.preprocess_transmission("automatic")
    print("transmission: ",value)
    
    value = dp.preprocess_drive("4wd")
    print("drive: ",value)
    
    value = dp.preprocess_cartype("pickup")
    print("cartype: ",value)
    
    value = dp.preprocess_paint_color("red")
    print("paint_color: ",value)
    
    value = dp.preprocess_state("al")
    print("state: ",value)
    
    
    
        
        
        
