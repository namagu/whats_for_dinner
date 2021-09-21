import numpy as np
import requests
from bs4 import BeautifulSoup

n = 100   # number of keys to make (often they will be not in english)

# generate random page keys and plug them into the url
lang = "en_US"
url = "https://cookidoo.thermomix.com/recipes/recipe/en-US/r"
links = [f"https://cookidoo.thermomix.com/recipes/recipe/en-US/r{i}" for i in np.int_(np.random.randint(9999,999999,n))]


def check_name(url): 
    # check whether there's a recipe matching random url
    req = requests.get(url) 
    
    # pass on 404s (doesn't exist)
    if req.status_code == 404:
      return None
    # grab recipe name and link if recipe is in english
    else:
      soup = BeautifulSoup(req.text, "html.parser") 
      # get language of search query for recommended recipes
      lang = soup.find("a", class_="link--subsequent core-stripe__more").attrs['href'].split('languages=')[1].split('&')[0]
      # return only english recipes
      if lang == 'en':
          return f"{soup.h1.contents[0]}  {lang}    {url}"
      else:
          # return foreign language recipes just for fun
          return f"recipe in {lang} " #({url})"

for i in links:
    recipe = check_name(i)
    if recipe:
      print(recipe)
    else:
      pass



