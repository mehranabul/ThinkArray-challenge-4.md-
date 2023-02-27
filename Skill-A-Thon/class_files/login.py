import pandas as pd
from werkzeug.security import check_password_hash
from flask_login import login_user
from flask import url_for, redirect

class login:
    def __init__(self, request):        
        self.email = request.form['email']
        self.password = request.form['password']

    def login_check(self):
        existing_data = pd.read_csv("candidate_data.csv")
        data = existing_data[existing_data['email']== self.email]
        print(self.password)
        print(data['password'][0])
        if len(data)>0:
            if data['password'][0]== self.password:
                return True
            else:
                return redirect(url_for('login_page') + '?error=incorrect-password')
        else:
            return redirect(url_for('login_page') + '?error=user-not-found')
        