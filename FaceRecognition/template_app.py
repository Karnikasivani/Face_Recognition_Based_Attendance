from flask import Flask, render_template, request, redirect, url_for
import json,time
from camera import VideoCamera
from flask import jsonify, Response,send_file
import requests
import cv2

app=Flask(__name__)
output=[]
database={}
@app.route('/')
def home_page():
    return render_template("new.html",result=output)

@app.route('/next')
def next():
    return render_template("new1.html")


def gen(camera):
    while True:
        data= camera.get_frame()

        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/vf')
def vf():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/success/<name>/<passwrd>')
def Success(name,passwrd):
    if name in database.keys():
        if passwrd==database[name]:
            return "<h1>Welcome to Innovate Yourself !!!</h1>"
        else:
            return "<h1>Invalid Username or password</h1>"
    else:
        return "<h1>Username doesn't exists.</h1>"



@app.route('/fetch_data',methods=['POST','GET'])
def FetchData():
    if request.method=="POST":
        user=request.form['nm']
        password=request.form['pw']
        return redirect(url_for('Success',name=user,passwrd=password))
    else:
        user = request.args.get('nm')
        password = request.args.get('pw')
        return redirect(url_for('Success', name=user,passwrd=password))

@app.route('/signup_page')
def signup_page():
    return render_template("signup.html")



@app.route('/registered/<name>/<passwrd>/<cnfpass>')
def Registered(name,passwrd,cnfpass):
    if passwrd==cnfpass:
        database.update({name:passwrd})
        return render_template("signup.html",message="You have successfully signed up.")
    else:
        return render_template("signup.html",message="Password didn't matched.")




@app.route('/signup',methods=['POST','GET'])
def Signup():
    if request.method=="POST":
        user=request.form['snm']
        password=request.form['spw']
        cpassword=request.form['scpw']
        return redirect(url_for('Registered',name=user,passwrd=password,cnfpass=cpassword))
    else:
        user = request.args.get('snm')
        password = request.args.get('spw')
        cpassword = request.args.get('scpw')
        return redirect(url_for('Registered', name=user,passwrd=password,cnfpass=cpassword))



#save time and
if __name__=="__main__":
    app.config['DEBUG']=True
    app.run(host='127.0.0.1',port='8080')