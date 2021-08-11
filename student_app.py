from flask import Flask, render_template, request, Response, session, jsonify, redirect, url_for, flash
import re
import csv
from csv import writer
import pandas as pd

app=Flask(__name__, template_folder='./templates')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        if request.form.get("addstudent"):
            return redirect(url_for('addstudent'))
        elif request.form.get("searchstudent"):
            return redirect(url_for('searchstudent'))
        elif request.form.get("displaystudents"):
            return redirect(url_for('displaystudents'))

    return render_template('index.html')

@app.route("/addstudent", methods =['GET', 'POST'])
def addstudent():
    print(request.method)
    if request.method == 'POST':
        print(request.form['studentid'])
        df=[]
        df.append(request.form['studentid'])
        df.append(request.form['studentname'])
        df.append(request.form['gender'])
        df.append(request.form['dateofbirth'])
        df.append(request.form['city'])
        df.append(request.form['state'])
        df.append(request.form['email'])
        df.append(request.form['qualification'])
        df.append(request.form['stream'])
        with open('D:\Workspace -VSCode\LBJ - Case Study 2\students.csv','a') as file:
            write=writer(file)
            write.writerow(df)
        file.close()    
        return render_template('index.html')
    else:
        return render_template('add-student.html')

@app.route("/searchstudent", methods =['GET', 'POST'])
def searchstudent():
    #rows=0
    #tstate=False
    if request.method == "POST":
        Student_ID=request.form.get("studentid")
        df=[]
        with open(r"D:\Workspace -VSCode\LBJ - Case Study 2\students.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if(len(row)):
                    if(row[0]==Student_ID):
                        df.append(row)
        file.close()
        #tstate=True
        return render_template('display-students.html', records=df) #row=rows,tstate=tstate)
    else:
        return render_template('search-student.html') #,row=rows,tstate=tstate)

@app.route("/displaystudents", methods=['GET'])
def displaystudents():
    df=[]
    with open(r"D:\Workspace -VSCode\LBJ - Case Study 2\students.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if(len(row)):
                df.append(row)
    file.close()            
    return render_template('display-students.html',records=df)

if __name__=='__main__':
    app.run(debug=True)

