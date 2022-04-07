from flask import Flask, render_template, request, redirect, url_for, send_file
import json,time
from camera import VideoCamera
from flask import jsonify, Response
import requests
import cv2

app=Flask(__name__)
output=[]
database={}
@app.route('/')
def home_page():
    return render_template("k.html",result=output)
@app.route('/k')
def k():
    return send_file('Report.csv',mimetype='text/csv',attachment_filename='Report.csv',
                     as_attachment=True)

if __name__=="__main__":
    app.run(debug=True)