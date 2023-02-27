import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from werkzeug.security import generate_password_hash
from flask import url_for, redirect

class candidate_registration:
    def __init__(self, request):        
        self.username = request.form['username']
        self.email = request.form['email']
        self.password = request.form['password']
        self.confirm_password = request.form['confirm-password']

    def validate_password(self):
        if self.username and self.email and self.password and self.confirm_password:
            if self.password == self.confirm_password:
                hashed_password = generate_password_hash(self.password, method='sha256')
                return hashed_password
            else:
                return redirect(url_for('login.login') + '?success=account-created')
        else:
            return redirect(url_for('register.register') + '?error=missing-fields')   

    def update_data(self):
        import csv
        try:
            up_dt = []
            new_data = {'name': self.username,
                    'email': self.email,
                    'password': self.password,
                    'cv_name': '12442909.pdf'}
            

            op = open("candidate_data.csv", newline='')
            existing_dt = csv.DictReader(op)
            for raw in existing_dt:
                up_dt.append(raw)
            
            up_dt.append(new_data)
            headers = ['name', 'email', 'password','cv_name']
            data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
            data.writerow(dict((heads, heads) for heads in headers))
            data.writerows(up_dt)
            op.close()
        except Exception:
            return redirect(url_for('register.register') + '?error=user-or-email-exists')
        