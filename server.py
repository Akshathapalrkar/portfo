# 
from flask import Flask, render_template, url_for,request,redirect
import csv
app = Flask(__name__)
print(__name__)
# print(VIRTUAL_ENV)

@app.route('/')
def my_home():
   	return render_template('index.html')

@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open("database.txt", mode = "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\n{email}.{subject},{message}")

def write_to_csv(data):
	with open("database.csv", "a",newline="") as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_file = csv.writer(database2, delimiter=",", quotechar="'",quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		# email = data["email"]
		# print(data)
		write_to_csv(data)
		# return data["email"]

		return render_template("thankyou.html", Email=data["email"], subject=data["subject"])
		# return redirect("/thankyou.html")
	else:
		return "something went wrong!"




# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact_me():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

