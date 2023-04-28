import sys, os, re

from datetime import datetime, timedelta
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests, validators, json, uuid, pathlib, os
from app.models.script import Script
from app.models.category import Category
DOMAIN = "https://nmap.org/nsedoc"

class nsearchModule:
    def verify_script_exist(self, name, url):
        return Script.query.filter_by(name=name, url=url).first()
    
    def verify_category_exist_by_name(self, name):
        return Category.query.filter_by(name=name).first()
    
    def get_module_data_from_page(self, requested_url, name):
        modules = dict()
        try:
            source = requests.get(f"{requested_url}").text
            soup = BeautifulSoup(source, "html.parser")
            module_name = soup.find('code').text
            description_h2 = soup.find('h2', {"id":"summary"})
            description = description_h2.find_next("p").text
            authors = [author.text for author in soup.find("ul", {"class": "authors_list"}).find_all('li')]
            types = soup.find("a", text="Script types").next_sibling.strip()
            category_list = categories = [i.text for i in soup.find_all("a") if i.parent.name == "i"]
            download_url = f"https://svn.nmap.org/nmap/scripts/{module_name}.nse"
            module = {'name':module_name,'type':types,'category':category_list,'url':download_url,description:description,'author':authors}
            print(module,'MOdulo1')
            return module
        except Exception as e:
            print(e, "error from page")
            return modules