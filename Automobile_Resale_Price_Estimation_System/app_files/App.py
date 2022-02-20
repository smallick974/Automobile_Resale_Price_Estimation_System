'''
Created on 19-Feb-2022

@author: Srijan-PC
'''
from flask import Flask, render_template, request
from app_files.Users import Users
from app_files.Cars import Cars

app= Flask(__name__)

@app.route('/')
def signinpage():
    return render_template("Home.html")

@app.route('/testUserSignup', methods=["POST"])
def usersignup():
    Users().userSignUp(request.form)
    return render_template("Home.html")

@app.route('/testSignIn', methods =["POST"])
def signin(): 
    Users().userLogin(request.form)
    return render_template("Home.html")

@app.route('/testUpdateUser', methods=["POST"])
def updateuser():
    Users().userUpdate(request.form)
    return render_template("Home.html")
    
@app.route('/testNewCar', methods=["POST"])
def newcar():
    print('My car details>>', request.form)
    Cars().newCar(request.form)
    return render_template("Home.html")    

@app.route('/testUpdateCar', methods=["POST"])
def updateCar():
    print('My car details for update>>', request.form)
    Cars().updateCar(request.form)
    return render_template("Home.html")   

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


# main function
if __name__ == '__main__':
    app.run(debug=True)
    
