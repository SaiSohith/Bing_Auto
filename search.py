import webbrowser
import random
from time import sleep
import os



url = 'https://docs.python.org/'

edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))


key="nice"
search_url="https://www.bing.com/search?q={}".format(key)


search_keywords=["computerscience","Java","Javascript","machinelearning","deeplearning",
"nlp","computervision","quantumn ","quantumnmachine","qbits","qunatumnsuperposition","quantumnrelativity"
,"quantumnwhatever","javascript","top10programmin","top10keywordsresume","networking","OS","programming",
"Python","SDLC","software development","SQL","Unix","softwareengineering","routing","linux","linux programming","learntodevelop"
"okk nice","ok whatever","SaaS","scrum","scripting","UI","Unix","usability","user experience","variances",
"web services","SQL server","git","git hub","heroku","android","ios","mac","windows","something","c","c++","codechef",
"dependencyinjection","inversionofcontrol","hibernate","javase","javaee","microservices","python","beyondpython",
"beyondjava","nicesites","boring","popularlanguagesfroprogramming","nice","ok","uwu","idfk","lol","idfk","idfc","ironman"
,"theinfinityproject","bestwaytobecomebillionaire","bestwaytobecomemillionaire","bestwaytobecometrillionaire","blogs","getintomicrosoft","bingbangbangbing",
"letsseethesearch","redeem","why did you","do this","you did not"]

print(len(search_keywords))

c=0

query=0
for i in range(0,40):
    query+=1
    if query%15==0:
        sleep(10)
        os.system("taskkill /f /im msedge.exe")
        sleep(30)
    keyword=search_keywords[random.randint(0,78)]
    print(keyword)
    search_url="https://www.bing.com/search?q={}".format(keyword)
    webbrowser.get('edge').open(search_url)
    sleep(1)

mob_query="https://www.bing.com/search?q=adsadwad&qs=n&form=QBRE&pc=LCTS&sp=-1&lq=1&pq=adsadwad&sc=1-8&sk=&cvid=326684A9ED424E3D8894A3F21D6F7FF4&ghsh=0&ghacc=0&ghpl="




os.system("taskkill /f /im msedge.exe")

webbrowser.open("https://unstop.com/home")