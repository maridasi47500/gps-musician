import requests
from bs4 import BeautifulSoup
from somepic import Somepic

class Chercherimage():
    def __init__(self,q):
       self.someparams={"q":q,"tbm":"isch"}
    def search(self):
       html = requests.get("https://www.google.com/search", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("img")
       malist.pop(0)
       return malist

for x in ("france", "england", "cat","dog","boy","girl"):
    j=Chercherimage(x).search()
    Somepic().create({"name":x,"pic":j[0]["src"]})

