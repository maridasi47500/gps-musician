from country import Country
from user import User
from post import Post
from musicalinstrument import Musicalinstrument
from song import Song
from somepic import Somepic
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.Musicalinstrument=Musicalinstrument()
    self.User=User()
    self.Song=Song()
    self.Post=Post()
    self.Somepic=Somepic()
