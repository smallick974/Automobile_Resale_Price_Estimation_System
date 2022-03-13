'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
from app_files.Users import Users
from app_files.Cars import Cars
import json

app= Flask(__name__)
app.secret_key = "56TiQWdoVayEhqJQezBb4n3k5QlnPIxjpfx"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def homepage():
    car_manufacturer_list = list(Cars().getCarManufacturer('false'))
    return render_template("Home.html",car_manufacturers = car_manufacturer_list)

@app.route('/nav', methods=['POST','GET'])
def nav():
    return render_template("Nav_Bar_test.html")

@app.route('/Home', methods=['POST','GET'])
def usersignup():
    Users().userSignUp(request.form)
    return render_template("Home.html")

@app.route('/Welcome', methods =['POST','GET'])
def signin(): 
    if request.method == "POST":
        print("data: ",request.form)
        session["userData"] = Users().userLogin(request.form)
    if session["userData"][0][1] == request.form["txt_email_id"]:
        return render_template("Home.html") 
    else:
        return redirect(url_for('homepage'))

@app.route('/Logout',methods =['POST','GET'])
def logout():
    session.pop("userData",None)
    return redirect(url_for('homepage'))   
    
@app.route('/Profile', methods=['POST','GET'])
def displayprofile():
    data=Users().displayProfile(session["userData"][0][1])
    return render_template("Profile.html",profiledata=data)

@app.route('/Test', methods=['POST','GET'])
def test():
    return render_template("Nav_Bar_test.html")
                               
@app.route('/testUpdateUser', methods=["POST"])
def updateuser():
    Users().userUpdate(request.form)
    return render_template("Home.html")
    
@app.route('/NewCar', methods=['POST','GET'])
def newcar():
    car_manufacturer = list(Cars().getCarManufacturer('true'))
    return render_template("UploadCar.html",car_manufacturer_list=car_manufacturer)    

@app.route('/Search', methods=['POST','GET'])
def searchdata():
    form_value = request.args.get('value', type=str)
    car_models = Cars().getCarModels(form_value)
    return jsonify(selected_car_models=car_models) 

@app.route('/CarDetails', methods=['POST','GET'])
def GetCarDetails():
    cars = Cars().getCars()
    return jsonify(car_list=cars) 

@app.route('/testUpdateCar', methods=["POST"])
def updateCar():
    print('My car details for update>>', request.form)
    Cars().updateCar(request.form)
    return render_template("Home.html")   

@app.route('/Wishlist', methods=["POST","GET"])
def wishlist():
    return render_template("Wishlist.html") 

@app.route('/testDelete', methods=["POST"])
def delete():
    print('My car details for update>>', request.form)
    if "userid" in request.form:
        Users().deleteUser(request.form)
    elif "carid" in request.form:
        Cars().deleteCar(request.form)
    elif "imageid" in request.form:
        Cars().deleteCarImage(request.form)       
    return render_template("Home.html")


# @app.route('/testModel', methods=["POST"])
# def testModel():
#     year = request.form.get("year")
#     manufacturer = request.form.get("manufacturer")
#     model = request.form.get("model")
#     condition = request.form.get("condition")
#     cylinders = request.form.get("cylinders")
#     fuel = request.form.get("fuel")
#     odometer = request.form.get("odometer")
#     transmission = request.form.get("transmission")
#     drive = request.form.get("drive")
#     cartype =request.form.get("cartype")
#     paint_color = request.form.get("paint_color")
#     state = request.form.get("state")
#
#     Models().loadvariables(year, manufacturer, model, condition, cylinders, fuel, odometer, transmission, drive, cartype, paint_color, state)
#     return render_template("Home.html")   

# main function
if __name__ == '__main__':
    app.run(debug=True)
    
