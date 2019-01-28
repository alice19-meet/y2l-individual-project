from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
from database import *


app = Flask(__name__)
app.config["SECRETKEY"] = "change-this-letter"
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def home():
    return render_template("home.html", login_session=login_session)

@app.route('/offers/<int:id>')
def offer_profile(id):

    offer=get_offer(id)
    return render_template('item.html', offer=offer)


@app.route('/create', methods=['GET', 'POST'])
def add_offer():
    if request.method == 'GET':
 
        return render_template('create.html', login_session=login_session)
    else:
        name = request.form['name']
        ingredients = request.form["ingredients"]
 

        create_offer(name, ingredients)  
        offers = get_all_offers()
        return redirect(url_for('offers'))


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', login_session=login_session)

@app.route('/offers')
def offers():
    offers = query_all()
    return render_template('offer.html', login_session=login_session, offers=offers)

@app.route('/create')
def create():
    return render_template('create.html', login_session=login_session)


@app.route('/search', methods=["GET",'POST'])
def search():
    if request.method=='POST':
        search=request.form["search"]
        offers=query_by_name(search)
        return render_template('offer.html', login_session=login_session, offers=offers)
    if request.method=="GET":
        return render_template('offer.html', login_session=login_session)


@app.route("/login", methods=["GET", "POST"])
def login():
    #POST
    if request.method=="POST":
        username = request.form['username']
        password= request.form["password"]
        user=query_by_username(username)
        if user==None:
            return "User doesn't exist."
        else:
            # TODO check if password matches
            if user.password==password:
                login_session['id'] = user.id
                login_session['username']= user.username
                login_session['first_name']=user.first_name
                login_session['last_name']=user.last_name
                return redirect(url_for('home'))

            else:
                return "Wrong Password"
        

    if request.method=="GET":
        return render_template('login.html', login_session=login_session)

@app.route('/signup',methods=["GET", "POST"])
def signup():

    if request.method=="POST":
        print(request.form)
        username = request.form['username']
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]    
        password= request.form["password"]
        confirm= request.form["confirm"]


        if password==confirm:
            add_user(first_name, last_name, username, password)
            login_session['id'] = query_by_username(username).id
            login_session['username']= username
            login_session['first_name']=first_name
            login_session['last_name']=last_name
            return redirect(url_for('home'))

        if password!=confirm:
            return " Wrong Password"
        
    else:
        return render_template('signup.html', confirm=False)

    if request.method=="GET":
        return render_template('signup.html')

app.route('/users')
def users(username):
    comments=query_comment_by_user(username)
    return render_template('users.html', u=query_by_username(login_session['username']), comments=comments)

@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

