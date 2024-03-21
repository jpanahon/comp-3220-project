import pandas as pd
import os

class DataHandler:
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.arenas_file= os.path.join(data_directory, 'Arenas.csv')
        self.parks_file = os.path.join(data_directory, 'Park Name and Addresses.csv')
        self.community_centers_file = os.path.join(data_directory, 'Community_Centres.csv')
        self.hospital_file = os.path.join(data_directory, 'Hospitals.csv')
        self.library_file = os.path.join(data_directory, 'Libraries.csv')
        self.fire_station_file = os.path.join(data_directory, 'Fire_Stations.csv')
        self.schools_file = os.path.join(data_directory, 'Schools.csv')
        
        self.arenas_data= pd.read_csv(self.arenas_file)
        self.parks_data = pd.read_csv(self.parks_file)
        self.community_centers_data = pd.read_csv(self.community_centers_file)
        self.hospital_data = pd.read_csv(self.hospital_file)
        self.library_data = pd.read_csv(self.library_file)
        self.fire_station_data = pd.read_csv(self.fire_station_file)
        self.schools_data = pd.read_csv(self.schools_file)
    
    # sort the data by a specific column
    def sort_arenas_by_name(self):
        return self.arenas_data.sort_values(by='ARENA') #sorts the arenas by arena name
    def sort_parks_by_name(self):
        return self.parks_data.sort_values(by='PARK NAME') #sorts the parks by name
    
    def sort_community_centers_by_type(self):
        return self.community_centers_data.sort_values(by='CENTRE') #sorts the community name of the center 
    
    def sort_hospitals_by_name(self):
        return self.hospital_data.sort_values(by='NAME') #sorts the hospitals by name
    
    def sort_libraries_by_name(self):
        return self.library_data.sort_values(by='NAME') #sorts the libraries by name
    
    def sort_fire_stations_by_name(self):
        return self.fire_station_data.sort_values(by='FIRE_HALL') #sorts the fire stations by fire hall number
    
    def sort_schools_by_name(self):
        return self.schools_data.sort_values(by='NAME') # sorts the schools by name
    
    # search for a keyword in the data
    def search_parks(self, keyword):
        return self.parks_data[self.parks_data['PARK NAME'].str.contains(keyword, case=False)] 
    
    def search_community_centers(self, keyword):
        return self.community_centers_data[self.community_centers_data['ADDRESS'].str.contains(keyword, case=False)]
    
    def search_hospitals(self, keyword):
        return self.hospital_data[self.hospital_data['NAME'].str.contains(keyword, case=False)]
    
    def search_libraries(self, keyword):
        return self.library_data[self.library_data['NAME'].str.contains(keyword, case=False)]
    
    def search_fire_stations(self, keyword):
        return self.fire_station_data[self.fire_station_data['ADDRESS'].str.contains(keyword, case=False)]
    
    def search_schools(self, keyword):
        return self.schools_data[self.schools_data['NAME'].str.contains(keyword, case=False)]




data_directory = 'data/CSV_data/'
data_handler = DataHandler(data_directory)


# list all fileds containing 'high'
high_schools = data_handler.search_schools('high')

# print(high_schools)

# sort parks by name 
sorted_parks = data_handler.sort_parks_by_name()
# print(sorted_parks)
