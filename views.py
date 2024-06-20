from flask import Blueprint,render_template

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
	return render_template("index.html")

@my_view.route("/helloworld")
def helloworld():
	return render_template("helloworld.html")

@my_view.route("/contributers")
def contributers():
	#return render_template("contributers.html")
	return f"<h1>Contributers</h1>\n{credit_devs()}"

def credit_devs():
	_devs = ["Joe Bloggs","Carl Bloggs"] # Made-up names.
	return "<ul>" + ''.join([f"<li>{name}</li>" for name in _devs]) + "</ul>"
