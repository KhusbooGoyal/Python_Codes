import requests
from bs4 import BeautifulSoup as bs

url ='https://www.instagram.com/{}/'

def pic_download(username):
    r=requests.get(url.format(username))
    s=bs(r.text,"html.parser")

    p=s.find("meta", property="og:image").attrs['content']

    with open(username+".jpg","wb") as pic:
        binary=requests.get(p).content
        pic.write(binary)

if __name__=="__main__":
    username="enter any existing username"

    pic_download(username)
