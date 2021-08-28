# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from joblib import dump, load
from flask import Flask,request, url_for, redirect, render_template

app=Flask(__name__)

pipe_gn=load("pipe_gn.joblib")
pipe_obc=load("pipe_obc.joblib")
pipe_sc=load("pipe_sc.joblib")
pipe_st=load("pipe_st.joblib")

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    caste_inf=request.form['caste']
    course_inf=request.form['course']
    rank=request.form['rank']
    if caste_inf=='GEN':
        data={"Course":[course_inf],"Closing_gn":[rank]}
        df=pd.DataFrame(data)
        pred=pipe_gn.predict(df)
    elif caste_inf=="OBC":
        data={"Course":[course_inf],"Closing_obc":[rank]}
        df=pd.DataFrame(data)
        pred=pipe_obc.predict(df)
    elif caste_inf=="SC":
        data={"Course":[course_inf],"Closing_sc":[rank]}
        df=pd.DataFrame(data)
        pred=pipe_sc.predict(df)
    elif caste_inf=="ST":
        data={"Course":[course_inf],"Closing_st":[rank]}
        df=pd.DataFrame(data)
        pred=pipe_st.predict(df)
        
    return render_template("index.html",Make_Prediction=pred)
    





if __name__=="__main__":
    app.run(debug=True,port=4444)
