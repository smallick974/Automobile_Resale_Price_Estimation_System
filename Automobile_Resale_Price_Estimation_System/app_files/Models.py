'''
Created on 23-Feb-2022

@author: Srijan-PC
'''

import pickle
import numpy as np
from scipy.sparse import hstack

class Models:
    
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
        
        self.dtr = "./model_files/models/Decision_Tree_Regressor"
        self.lgb = "./model_files/models/LGBM_Regressor"
        self.mlp = "./model_files/models/MLP_Regressor"
        
    
    def preprocess_year(self,year):
        year_scaler = pickle.load(open(self.year,'rb'))
        value = year_scaler.transform(np.array(year).reshape(-1,1)).ravel()
        return value
    
    def preprocess_manufacturer(self,manufacturer):
        manufacturer_onehot_encoder = pickle.load(open(self.manufacturer,'rb'))
        value = manufacturer_onehot_encoder.transform(np.array(manufacturer).reshape(-1,1))
        return value
    
    def preprocess_model(self,model):
        dict_model_freq = pickle.load(open(self.model,'rb'))
        value = 0
        if model in dict_model_freq.keys():
            value = dict_model_freq[model]
        return value
    
    def preprocess_condition(self,condition):
        condition_onehot_encoder = pickle.load(open(self.condition,'rb'))
        value = condition_onehot_encoder.transform(np.array(condition).reshape(-1,1))
        return value
    
    def preprocess_cylinders(self,cylinders):
        cylinders_dict = pickle.load(open(self.cylinders,'rb'))
        value = 0
        if cylinders in cylinders_dict.keys():
            value = cylinders_dict[cylinders]
        return value
    
    def preprocess_fuel(self,fuel):
        fuel_onehot_encoder = pickle.load(open(self.fuel,'rb'))
        value = fuel_onehot_encoder.transform(np.array(fuel).reshape(-1,1))
        return value
    
    def preprocess_odometer(self,odometer):
        odometer_scaler = pickle.load(open(self.odometer,'rb'))
        value = odometer_scaler.transform(np.array(odometer).reshape(-1,1)).ravel()
        return value

    def preprocess_transmission(self,transmission):
        transmission_onehot_encoder = pickle.load(open(self.transmission,'rb'))
        value = transmission_onehot_encoder.transform(np.array(transmission).reshape(-1,1))
        return value

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
        value = paint_color_ordinal_encoder.transform(np.array(paint_color).reshape(-1,1)).ravel()
        return value
    
    def preprocess_state(self,state):
        state_ordinal_encoder = pickle.load(open(self.state,'rb'))
        value = state_ordinal_encoder.transform(np.array(state).reshape(-1,1)).ravel()
        return value




    # 1. Decision Tree Regressor
    def predict_DTR(self,x):
        dtr = pickle.load(open(self.dtr,'rb'))
        y = dtr.predict(x)
        return y[0]
    
    # 2. LGBM Regressor
    def predict_LGB(self,x):
        dtr = pickle.load(open(self.lgb,'rb'))
        y = dtr.predict(x)
        return y[0]
    
    # 3. MLP Regressor
    def predict_MLP(self,x):
        dtr = pickle.load(open(self.mlp,'rb'))
        y = dtr.predict(x)
        return y[0]
    

    
if __name__ == '__main__':
    models = Models()
    
    year = models.preprocess_year("2017")
    print("year: ",year)
    
    manufacturer = models.preprocess_manufacturer("toyota")
    print("manufacturer: ",manufacturer)
    
    model = models.preprocess_model("tundra double cab sr")
    print("model: ",model)
    
    condition = models.preprocess_condition("good")
    print("condition: ",condition)
    
    cylinders = models.preprocess_cylinders("8 cylinders")
    print("cylinders: ",cylinders)
    
    fuel = models.preprocess_fuel("gas")
    print("fuel: ",fuel)
    
    odometer = models.preprocess_odometer("41124")
    print("odometer: ",odometer)
    
    transmission = models.preprocess_transmission("automatic")
    print("transmission: ",transmission)
    
    drive = models.preprocess_drive("4wd")
    print("drive: ",drive)
    
    cartype = models.preprocess_cartype("pickup")
    print("cartype: ",cartype)
    
    paint = models.preprocess_paint_color("red")
    print("paint_color: ",paint)
    
    state = models.preprocess_state("al")
    print("state: ",state)
    
    # Encoding all the features
    
    X_stack = hstack((year, manufacturer, model, condition, cylinders, 
                      fuel, odometer, transmission, drive, cartype, 
                      paint, state))
    
    y = models.predict_DTR(X_stack)
    print(y)
    
    y = models.predict_LGB(X_stack)
    print(y)
    
    y = models.predict_MLP(X_stack)
    print(y)
    
    
    
        
        
        
