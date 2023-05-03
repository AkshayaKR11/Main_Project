# importing the libraries
from tkinter import *
import requests
import json
import time
import pyttsx3
import datetime
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText

from newsapi import NewsApiClient

nsapi = NewsApiClient(api_key='4c6fd07fb18c436fb078d016002977f2')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
  
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)
  
sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')

# necessary details
root = Tk()
root.title("Weather App")
root.geometry("1000x700")
root['background'] = "white"
  
# Image
new = ImageTk.PhotoImage(Image.open('logo.png'))
panel = Label(root, image=new)
panel.place(x=0, y=520)
  
  
# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%d %A'), bg='white', font=("bold", 16))
date.place(x=180, y=20)
month = Label(root, text=dt.strftime(' %B')+" 2023", bg='white', font=("bold", 16))
month.place(x=330, y=20)
  
# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 16))
hour.place(x=437, y=20)
  
# Theme for the respective time the application is used
if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:


    image = Image.open('moon.png')
    image = image.resize((62, 62), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(image)
    panel = Label(root, image=img)
    panel.place(x=10, y=10)
else:
    image = Image.open('sun.png')
    image = image.resize((62, 62), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(image)
    panel = Label(root, image=img)
    panel.place(x=10, y=10)
  

def insert_news(a):
    global mylist
    # root.after(cntval, lambda : insert_news(title))
    mylist.insert(END, a)


def add_news(titlelist,deslist):
    global mylist,root
    print("titles-->",titlelist)
    print("description-->",deslist)
    mylist.config(font=("Arial 20 bold"))
    mylist.insert(INSERT, "=================================== TOP NEWSES =====================================\n\n")
    
    for i in range(len(titlelist)):
        mylist.config(font=("Arial 12 bold"))
        mylist.insert(INSERT, titlelist[i]+"\n")
        mylist.insert(INSERT, "------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        # mylist.config(font=("Arial 10 bold"))
        # mylist.insert(INSERT, deslist[i]+"\n")
        # mylist.insert(INSERT, "==========================================================================\n")
        print("=================================================")
        # mylist.see(END)
    mylist.config(state="disabled")

def say_newses(titlelist,deslist):
  engine.say("Reading Newses")
  engine.runAndWait()
  for i in range(len(titlelist)):

        engine.say("Reading news "+str(i+1))
        engine.runAndWait()
        # engine.say("Title")
        # engine.runAndWait()
        engine.say(titlelist[i]) 
        engine.runAndWait()
        # engine.say("News description ")
        # engine.runAndWait()
        # engine.say(deslist[i])
        # engine.runAndWait()

# lable_head = Label(root, text="Welcome to Smart Mirror", width=0, 
#                    bg='white',fg='red', font=("bold", 35))
# lable_head.place(x=130, y=13)

  
# Country  
lable_citi = Label(root, text="...", width=0, 
                   bg='white', font=("bold", 15))
lable_citi.place(x=620, y=20)
  
lable_country = Label(root, text="...", width=0, 
                      bg='white', font=("bold", 15))
lable_country.place(x=  740, y=20)


  

mylist =ScrolledText(root,width = 85,height=35,font=("Arial 10 bold")); mylist.grid(row=1, column=1)

mylist.place( x = 0, y = 150 )

  
maxi = Label(root, text="Max. Temp: ", width=0, 
             bg='white', font=("bold", 15))
maxi.place(x=605, y=50)
  
max_temp = Label(root, text="...", width=0, 
                 bg='white', font=("bold", 15))
max_temp.place(x=730, y=50)
  
  
mini = Label(root, text="Min. Temp.: ", width=0, 
             bg='white', font=("bold", 15))
mini.place(x=605, y=80)
  
min_temp = Label(root, text="...", width=0, 
                 bg='white', font=("bold", 15))
min_temp.place(x=730, y=80)


ctemp = Label(root, text="Current Temp: ", width=0, 
             bg='white', font=("bold", 15))
ctemp.place(x=605, y=110)
  
cur_lab = Label(root, text="...", width=0, 
                 bg='white',fg='red', font=("bold", 15))
cur_lab.place(x=730, y=110)

  
# API Call
api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                           + "Angamaly"+ "&units=metric&appid="+"ff4b49683cbccf221aa809d76b174af8")

api = json.loads(api_request.content)

# Temperatures
y = api['main']
current_temprature = y['temp']
humidity = y['humidity']
tempmin = y['temp_min']
tempmax = y['temp_max']



# Country
z = api['sys']
country = z['country']
citi = api['name']

# Adding the received info into the screen
cur_lab.configure(text=str(current_temprature)+"°C")
max_temp.configure(text=str(tempmax)+"°C")
min_temp.configure(text=str(tempmin)+"°C")

lable_country.configure(text=country)
lable_citi.configure(text=citi)


from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

nsapi = NewsDataApiClient(apikey="pub_182078d6fbe086eaa15206b54e7054c52f176")


news = nsapi.news_api(country = "in",language="en")


print(news)

titlelist=[]
deslist=[]
for new in news['results']:

    title=str(new['title'])
    description=str(new['content'])

    titlelist.append(title)
    deslist.append(description)

root.after(1000, lambda :add_news(titlelist,deslist))

root.after(30000, lambda :say_newses(titlelist,deslist))

  
  
root.mainloop()