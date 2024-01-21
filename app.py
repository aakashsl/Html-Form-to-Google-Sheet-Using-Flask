from flask import Flask, request, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet
sheet = gc.open_by_key('Your_Sheet_Key')  # Replace with your sheet's key
worksheet = sheet.get_worksheet(0)  # Select the first worksheet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Append data to the Google Sheet
        worksheet.append_row([name, email])

        return 'Data submitted successfully!'
    else:
        return render_template('index.html')  # Render the HTML form

if __name__ == '__main__':
    app.run(debug=True)