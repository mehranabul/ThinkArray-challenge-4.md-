######## Importing Lib for Python works and Flasks #################
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='frontend')

@app.route('/')
@app.route("/login",methods = ['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        from class_files.login import login
        login_obj = login(request=request)
        login_obj.login_check()
        return render_template('home.html')
        # else:
            # return render_template('register.html')
    else:
        return render_template('login.html')

@app.route("/register",methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        from class_files.candidate_registration import candidate_registration
        obj = candidate_registration(request = request)
        obj.update_data()
        return render_template('login.html')
    else:
        return render_template('register.html')

@app.route("/home",methods = ['GET'])
def home():
    import pandas as pd
    data = pd.read_csv('job_description/job_description.csv', )
    data = data.head()
    return render_template('home.html', tables=[data.to_html()], titles=[''])


@app.route("/cv_scanner",methods = ['POST','GET'])
def cv_scan():
        from class_files.resume_scanner import resume_scanner
        obj = resume_scanner()
        text = 'Responsible for digital marketing of products or services in support of Oracle demand'
        candidate_data = obj.run_scanner(text = text)
        return render_template('report.html', tables=[candidate_data.to_html()], titles=[''])



if __name__ == "__main__":
    app.run(host = 'localhost',port=int("5000"),debug= True)