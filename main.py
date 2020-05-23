from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#to write to file
def write_to_file(data):
    with open("C:/Users/rahkumar/Desktop/pp/WebDevepment/venv/database.txt", mode='a') as my_database:
       email = data['email']
       subject = data['subject']
       message = data['message']
       my_database.write(f'\n{email}{subject}{message}')

def write_to_csv(data):
    with open("C:/Users/rahkumar/Desktop/pp/WebDevepment/venv/database.csv",newline='', mode='a') as my_database2:
       email = data['email']
       subject = data['subject']
       message = data['message']
       csf_file= csv.writer(my_database2, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
       csf_file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # to get data in form of dictionary
            write_to_csv(data)
            return redirect('/thankyou.html') #to redirect to other page
        except:
            return "did not save to database"
    else:
        return "went wrong"

'''
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() # to get data in form of dictionary
        #to store data in database
        with open("C:/Users/rahkumar/Desktop/pp/WebDevepment/venv/database.txt" , mode='a') as my_database:
            my_database.write('\n' + str(data))
        print(data)
        return redirect('/thankyou.html') #to redirect to other page
    else:
        return "went wrong"

'''

