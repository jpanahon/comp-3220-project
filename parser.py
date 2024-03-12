"""
Created on Tue Mar 12 14:41:27 2024

@author: Jacob Bondy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

class Parser():
    #Initializes Parser with an array of valid download file extensions
    def __init__(self):
        self.valid_extensions = ['csv', 'kmz', 'dwg', 'zip']

    #Parses website for URL containing file_type, defaulted to
    # "Uploads" for windsor opendata
    def downloadable_parser(self, url, file_type = "Uploads"):
        
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
    
    #Downloads file from specified url, this is a direct download link
    #and saves it to a directory
    def download(self, url, save_directory = ""):
        if not url:
            print("No URL entered")
            return None
        
        #checks for valid file type and url
        file_name = url.split('/')[-1]
        if len(file_name) == 0 or not (file_name.split('.')[-1] in self.valid_extensions):
            print("No file or invlaid file found in URL")
            return None
        
        #gets download information
        response = requests.get(url, allow_redirects = True)
        
        #checks if directory is created, if not, creates it
        if not os.path.exists(save_directory) and save_directory != "":
            print(f"Creating directory {save_directory}")
            os.mkdir(save_directory)
        
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
            






