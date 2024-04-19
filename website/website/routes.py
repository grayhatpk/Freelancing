from website import app,db
from flask import render_template, redirect, url_for
from website.forms import register, login
from website.models import user
from flask_login import login_required ,login_user, logout_user, current_user
from flask import render_template ,redirect, url_for

@app.route("/",methods=['POST','GET'])
def goto():
    print()
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login_page():
    form = login()
    if form.validate_on_submit():
        try:
            if current_user.is_authenticated:
                return redirect(url_for('profile'))
            check_username = user.query.filter_by(username= form.username.data).first()
            
            if check_username and check_username.password_hash == form.password.data:
                login_user(check_username)
                print(f'Congratulations! You are logged in as {check_username.username}')
                return redirect(url_for('profile'))
            
            else:
                print("Username or Password is not Correct. Please try another Username or Password")
        except Exception as e:
            print("Username or Password is not Correct. Please try another Username or Password")
        
    return render_template('login.html' , form=form)

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

@app.route("/register", methods=['GET','POST'])
def register_page(): 
    form = register()
    
    if form.validate_on_submit():
        try:
            if current_user.is_authenticated:
                return redirect(url_for('profile'))
            new_user  = user( username = form.username.data ,  email = form.email.data , password_hash = form.password1.data )   
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            print(f'Congratulations! You have been registered as {new_user.username}')
            return redirect(url_for('profile'))
        except Exception as e:
            print(f'Error: Creating Your Account: {e}')
            return redirect(url_for("register_page"))
            
    if form.errors != {} : 
        for error in form.errors.values():
            print(f"Error Creating Your Account: {error}")  
        
    return render_template('register.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('home'))