import sys, os, re

from datetime import datetime, timedelta
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests, json, uuid, pathlib, os
from app.models.category import Category
from app.controllers.nsearchModule import nsearchModule



from app import app, db_pgl as db

from app.utils.response import (
    not_acceptable,
    success_request,
    error_transacction,
    bad_request,
    not_found,
)

DOMAIN = "https://nmap.org/nsedoc"
MODULE = nsearchModule();
class nsearchCategory:
    def get_categories(self):
        try:
            categories = self.get_category_from_page("categories/", "dl > dt", DOMAIN)
            if categories is not None:
                insert_cat = list()
                for cat in categories:
                    category = Category(cat["text"], cat["url"])
                    verify = self.verify_category_exist(name=cat["text"],url=cat["url"])
                    if verify is None:
                        insert_cat.append(category)
                if len(insert_cat) > 0:
                    db.session.add_all(insert_cat)
                    db.session.commit()
            ret = success_request(
                {"message": "Consult categories", "categories": categories}
            )
        except Exception as e:
            print(e, "El Error")
            ret = error_transacction("error geting Categorie")
        return ret

    def get_category_from_page(self, requested_url, find, domain):
        categories = []
        try:
            source = requests.get(f"{domain}/{requested_url}").text
            soup = BeautifulSoup(source, "html.parser")
            specific_element = soup.select(find)
            for ct in specific_element:
                for tag in ct.find_all("a", href=True):
                    category_data = dict(url=tag.get("href"), text=tag.text)
                    category_data["url"] = category_data["url"].replace("..", domain)
                    categories.append(category_data)
            return categories
        except Exception as e:
            print(e, "error from page")
            return categories

    def verify_category_exist(self, name, url):
        return Category.query.filter_by(name=name, url=url).first()
    
    def get_modules_from_category(self, name_module):
        module_name = f"categories/{name_module}"
        module = self.get_modules_from_page(module_name, "dl.list > dt", DOMAIN)
        try:
            if module is not None:
                print(module,'Module')
                insert_cat = list()
                for mdl in module:
                    categroy = Category(mdl["text"], mdl["url"])
                    verify = self.verify_category_exist(name=mdl["text"],url=mdl["url"])
                    if verify is None:
                        insert_cat.append(categroy)
                if len(insert_cat) > 0:
                    db.session.add_all(insert_cat)
                    db.session.commit()
            ret = success_request(
                {"message": "Consult Category", "Category": module_name}
            )
        except Exception as e:
            print(e, "El Error")
            ret = error_transacction("error geting Categorie")
        return ret
    
    def get_modules_from_page(self, requested_url, find, domain):
        modules = []
        try:
            source = requests.get(f"{domain}/{requested_url}").text
            soup = BeautifulSoup(source, "html.parser")
            specific_element = soup.select(find)
            for ct in specific_element:
                for tag in ct.find_all("a", href=True):
                    category_data = dict(url=tag.get("href"), text=tag.text.strip())
                    category_data["url"] = category_data["url"].replace("..", domain)
                    MODULE.get_module_data_from_page(category_data["url"])
                    #sys.exit(0)
                    modules.append(category_data)
            return modules
        except Exception as e:
            print(e, "error from page")
            return modules
