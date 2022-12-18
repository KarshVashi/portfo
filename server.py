from flask import Flask, render_template
from flask import request, redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
	with open('database.csv',mode='a') as database_csv:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=csv.writer(database_csv, delimiter=',')
		file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'





# @app.route('/works.html')
# def work():
# 	return render_template('works.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')