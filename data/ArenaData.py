from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def show_csv():
    # Read the CSV data
    data = []
    with open('Arenas.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    
    # Pass the data to the HTML template
    return render_template('csv_display.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
