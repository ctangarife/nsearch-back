import sys,re

from datetime import datetime, timedelta
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
from app.models.script import Script
from app.models.category import Category
from app.models.author import Author
from app.models.script_x_category import ScriptXCategory
from app.models.script_data import ScriptData
from app import app, db_pgl as db
DOMAIN = "https://nmap.org/nsedoc"


class nsearchModule:
    def verify_script_exist(self, name, url):
        return Script.query.filter_by(name=name, url=url).first()

    def verify_category_exist_by_name(self, name):
        return Category.query.filter_by(name=name).first()

    def get_module_data_from_page(self, requested_url):
        modules = dict()
        try:
            source = requests.get(f"{requested_url}").text
            soup = BeautifulSoup(source, "html.parser")
            module_name = soup.find('code').text
            description_h2 = soup.find('h2', {"id": "summary"})
            description = description_h2.find_next("p").text
            authors = [author.text for author in soup.find(
                "ul", {"class": "authors_list"}).find_all('li')]
            types = soup.find("a", text="Script types").next_sibling.strip()
            types = re.sub(r':\n', '', types)
            category_list = [i.text for i in soup.find_all(
                "a") if i.parent.name == "i"]
            url = f"https://nmap.org/nmap/scripts/{module_name}.nse"
            download_url = f"https://svn.nmap.org/nmap/scripts/{module_name}.nse"
            module = {'name': module_name, 'type': types, 'category': category_list, 'url': url,
                      'url_download': download_url, 'description': description, 'author': authors}
            self.add_module(module)
            return
        except Exception as e:
            print(e, "error from page1")
            return modules

    def add_module(self, module):
        exist = self.verify_script_exist(module['name'], module['url'])
        if exist == None:
            auth = self.verify_author(module['author'][0])
            script_insert = Script(module['name'],auth,module['url'],module['url_download'])
            db.session.add(script_insert)
            db.session.commit()
            script_id = db.session.scalar(db.session.query(Script.id).filter_by(name=module['name'], url=module['url']))
            for ct in module['category']:
                cat = self.verify_category_exist_by_name(ct)
                if cat != None:
                    db.session.add(ScriptXCategory(script_id,cat.id))
                    db.session.commit()
            db.session.add(ScriptData(script_id,module['type'].strip(),module['description']))
            db.session.commit()
            return script_id
        for ct in module['category']:
                cat = self.verify_category_exist_by_name(ct)
                if cat != None:
                    db.session.add(ScriptXCategory(exist.id,cat.id))
                    db.session.commit()
        db.session.add(ScriptData(exist.id,module['type'].strip(),module['description']))
        db.session.commit()
        return exist.id

    def verify_author(self, author):
        author = author.strip()
        auth = Author.query.filter_by(name=author).first()
        if auth is None:
            auth = Author(author)
            db.session.add(auth)
            db.session.commit()
            id = db.session.scalar(db.session.query(Author.id).filter_by(name=author))
            return id
        return auth.id
