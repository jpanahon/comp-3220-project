from flask import Flask, render_template
import csv

app = Flask(__name__)

BASE_PATH = 'C:/Users/MICHAEL/OneDrive/Desktop/Data/'

def read_csv(file_name):
    # Full path to the CSV file
    file_path = f'{BASE_PATH}{file_name}'
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/arenas')
def show_arenas():
    data = read_csv('Arenas.csv')
    return render_template('csv_display.html', data=data, title='Arenas')

@app.route('/community-centres')
def show_community_centres():
    data = read_csv('Community_Centres.csv')
    return render_template('csv_display.html', data=data, title="Community Centres")

@app.route('/fire-stations')
def show_fire_stations():
    data = read_csv('Fire_Stations.csv')
    return render_template('csv_display.html', data=data, title="Fire Stations")

@app.route('/hospitals')
def show_hospitals():
    data = read_csv('Hospitals.csv')
    return render_template('csv_display.html', data=data, title="Hospitals")

@app.route('/libraries')
def show_libraries():
    data = read_csv('Libraries.csv')
    return render_template('csv_display.html', data=data, title="Libraries")

@app.route('/parks')
def show_parks():
    data = read_csv('Park Name and Addresses.csv')
    return render_template('csv_display.html', data=data, title='Park Names and Addresses')

@app.route('/schools')
def show_schools():
    data = read_csv('Schools.csv')
    return render_template('csv_display.html', data=data, title='Schools')

@app.route('/bus-stops')
def show_bus_stops():
    data = read_csv('Transit Windsor Bus Stops.csv')
    return render_template('csv_display.html', data=data, title='Transit Windsor Bus Stops')

if __name__ == '__main__':
    app.run(debug=True)
