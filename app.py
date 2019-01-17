from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about_us')
def about_us():
	return render_template('about_us.html')

@app.route('/offers')
def offers():
	return render_template('offer.html')

@app.route('/create')
def create():
	return render_template('create.html')


@app.route('/search', methods=['POST'])
def search_bar():
    if request.method=='POST':
        search=request.form["search"]
        offers=query_by_name(name=search).all()
        return render_template('search.html', results=offers)
    return render_template('home.html',login_session=login_session )

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
        return render_template('login.html')

@app.route('/signup',methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        username = request.form['username']
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]    
        password= request.form["password"]
        confirm= request.form["confirm password"]

    if password==confirm:
        add_user(first_name, last_name, username, password)
        login_session['id'] = query_by_username(username).id
        login_session['username']= username
        login_session['first_name']=first_name
        login_session['last_name']=last_name
        return redirect(url_for('home'))
        
    else:
        return render_template('signup.html', confirm=False)

    if request.method=="GET":
        return render_template('signup.html')



@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

