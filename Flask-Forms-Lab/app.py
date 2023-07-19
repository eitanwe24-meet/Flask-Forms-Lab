from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "eitan"
password = "1"
facebook_friends=["eitan","shira","sagi", "osnat", "morrie", "nevo", "Jihad"]
db = {"jihad":"cs", "ava":"mit","eitan":"e"}


@app.route('/', methods= ['POST', 'GET'])  # '/' for the default page
def login()	:
	if request.method == 'POST':
		name = request.form['username']
		pas = request.form['password']
		if name in db and db[name] == pas:
			return redirect(url_for('home')) 
	return render_template('login.html')
  

@app.route('/home')
def home():
	return render_template('home.html',friends = facebook_friends)

@app.route('/friends_exists/<string:name>', methods = ['POST','GET'])
def hello(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', n = name, b = True)
	else:
		return render_template('friend_exists.html', n = name, b = False)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)