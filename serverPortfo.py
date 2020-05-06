from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def page1Home():
    return render_template('index.html')


# <--below: "url" variable rules for dynamic "page name"
@app.route('/<string:page_name>')
def pageDyna(page_name):
    return render_template(page_name)


def write_to_txt(thisData):  # <--stores into txt file
    with open('dbPortfo.txt', mode='a') as database:
        email = thisData["email"]
        subject = thisData["subject"]
        message = thisData["message"]
        # <--in txt file, "headers" are pre-written as: " email, subject, message, ""
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(thisData):  # <--stores into csv file
    with open('dbPortfo.csv', newline='', mode='a') as database2:
        email = thisData["email"]
        subject = thisData["subject"]
        message = thisData["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        # <--in csv, headers are pre written as: " email, subject, message, ""

# <--below... note: "post"--browser saves data   "get"--browser sends data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            dataCollectd = request.form.to_dict()
            write_to_txt(dataCollectd)
            write_to_csv(dataCollectd)
            # print(dataCollectd)  # <--for test on terminal
            return redirect('/thanks.html')
        except:
            return 'Failed to save to database'
    else:
        return 'something went wrong, TRY AGAIN'
# <--linked to "contact.html"...when "send" is pressed..thank you page appears
