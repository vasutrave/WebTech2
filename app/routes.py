from flask import Flask
from flask import render_template, redirect, url_for, request, session, flash
from werkzeug.utils import redirect
from db_access import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

import psycopg2
import psycopg2.extras


conn = psycopg2.connect("dbname='db' user='username' host='localhost' password='password'")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True
 
@app.route("/")
def home():

    
    
    if not session.get('logged_in'):
        return render_template('signin.html')
    else:
        return render_template('main.html')
    




@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route('/get_restaurant', methods=['POST', 'GET'])
def get_restaurant():

    data = request.form.to_dict(flat = False)
    keyword = ''.join(data['keyword'])
    filter = ''.join(['filter'])
    print("###################HERE################")
    print(keyword)
    print(filter)
    filter = "Cuisine"

    

    results = get_restaurant_details(keyword, filter)
    


    return render_template("Listed.html", results = results)

@app.route('/get_info', methods = ['POST', 'GET'])
def get_info():

    data = request.form.to_dict(flat = False)
    id = ''.join(data['id'])

    resp = get_restaurant_reviews(id)
    print(resp)
    results = resp[0][0]
    datas = resp[1]
    print(results)

    return render_template("restaurant.html", results = results, datas = datas)

@app.route('/set_review', methods = ['POST', 'GET'])
def set_review():

    data = request.form.to_dict(flat = False)
    review = ''.join(data['review'])
    id = ''.join(data['id'])
    username = "Varuni"
    sentiment = "positive"
    print("##############################IN REVIEW###################")
    print(review)
    print(id)

    #add sentiment function call here

    resp = set_restaurant_review(id, username, review, sentiment)

    resp = get_restaurant_reviews(id)
    print(resp)
    results = resp[0][0]
    datas = resp[1]
    print(results)

    return render_template("restaurant.html", results = results, datas = datas)

@app.route('/get_location', methods = ['POST', 'GET'])
def get_location():

    data = request.form.to_dict(flat = False)
    location = ''.join(data['location'])
    filter = "location"

    results = get_restaurant_details(location, filter)

    return render_template("Listed.html", results = results)






 
if __name__ == "__main__":
    app.run(debug = True)   

