"""
Created on Tue Mar 12 14:41:27 2024

@author: Jacob Bondy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import pickle
import datetime

class Parser():
    #Initializes Parser with an array of valid download file extensions
    def __init__(self):
        self.valid_extensions = ['csv', 'kmz', 'dwg', 'zip']
    
    def downloader(self, url, save_directory):
        
        #checks if directory is created, if not, creates it
        if not os.path.exists(save_directory) and save_directory != "":
            print(f"Creating directory {save_directory}")
            os.mkdir(save_directory)
        
        path_to_dict = fr"{save_directory}\{save_directory.split('/')[-1]}_dict.pkl"
        if os.path.exists(path_to_dict):
            with open(path_to_dict, 'rb') as f:
                download_dict = pickle.load(f)
        else:
            download_dict = dict()
            
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        sel = soup.select('span', class_ = '.ml-3')
        
        dates = []

        for element in sel:
            try:
                element = element.get_text()
                rfmt = (element.replace("(", "")).replace(")", "")
                dates.append(datetime.datetime.strptime(rfmt, "%m/%d/%Y").strftime("%Y-%m-%d"))
            except:
                continue
    
        
        download_links = self.__downloadable_parser__(url)
        # print(download_links)
        # print(dates)
        
        for i in range(len(dates)):
            file_name = ""
            d = download_links[i]
        
            if file_name == "":
                file_name = self.__get_file_name__(f"{url}{d}")
        
            if file_name == None:
                print(f"Invalid file name for link {url}{d}")
                continue
            
            abs_path = f"{save_directory}/{file_name}"
            try:
                last_updated = download_dict[abs_path]
                if last_updated < dates[i]:
                    self.__download__(f"{url}{d}", file_name, save_directory)
                    print("downloading!")
            except KeyError:
                download_dict[abs_path] = dates[i]
                self.__download__(f"{url}{d}", file_name, save_directory)
                print("downloading!")
        
        with open(path_to_dict, 'wb') as f:
            pickle.dump(download_dict, f)
        
    #Parses website for URL containing file_type, defaulted to
    # "Uploads" for windsor opendata
    def __downloadable_parser__(self, url, file_type = "Uploads"):
         
        #Tries to query the website and will print error message if
        #exception is raised
        try:
            response = requests.get(url)
        except:
            print("invalid URL")
            return []
        
        #Uses beautiful soup library to parse html
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #looks for any html containing the href tag (links)
        links = soup.select('[href]')
        if not(links):
            print("No links found")
            return []
        
        out = []
        
        #gets each link from all elements and appends to list
        for element in links:
            l = element.get("href")
            if file_type in l:
                out.append(l)
        return out

    
    def __get_file_name__(self, url):
        if not url:
            print("No URL entered")
            return None
        
        #checks for valid file type and url
        file_name = url.split('/')[-1]
        if len(file_name) == 0 or not (file_name.split('.')[-1] in self.valid_extensions):
            print("No file or invlaid file found in URL")
            return None
        
        return file_name
    
    #Downloads file from specified url, this is a direct download link
    #and saves it to a directory
    def __download__(self, url, file_name, save_directory = ""):
        
        #gets download information
        response = requests.get(url, allow_redirects = True)
        
        #writes downloaded data to file
        open(fr"{save_directory}\{file_name}", 'wb').write(response.content)
        
    #gets all open data titles and corresponding links from windsor open data
    def __get_data_links__(self):
        url = "https://opendata.citywindsor.ca/"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.select('div', class_ ="opendata-item")
        
        urls = []
        titles = []
        
        for element in items:
            url = element.get("data-url")
            title = element.find('div', class_="card-title")
            if url:
                urls.append(url)
                title = title.get_text()
                if "\xa0" in title:
                    title = title.replace(u"\xa0", '')
                if title[-1] == ' ':
                        title = title[:-1]
                titles.append(title)
        return dict(zip(titles, urls))
            

# url = "https://opendata.citywindsor.ca/details/207"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# sel = soup.select('span', class_ = '.ml-3')

parser = Parser()

parser.downloader("https://opendata.citywindsor.ca/details/207", "data/Parks")



