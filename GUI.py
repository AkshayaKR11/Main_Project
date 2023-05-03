# importing the libraries
from tkinter import *
import requests
import json
import time
import pyttsx3
import datetime
from PIL import ImageTk, Image


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
root.geometry("1200x700")
root['background'] = "white"
  
# Image
new = ImageTk.PhotoImage(Image.open('logo.png'))
panel = Label(root, image=new)
panel.place(x=0, y=520)
  
  
# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A'), bg='white', font=("bold", 15))
date.place(x=380, y=70)
month = Label(root, text=dt.strftime('%m %B')+" 2023", bg='white', font=("bold", 15))
month.place(x=450, y=70)
  
# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 15))
hour.place(x=600, y=70)
  
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
    mylist.insert(END, "===================== TOP NEWSES ================\n")
    for i in range(len(titlelist)):
        
        mylist.insert(END, titlelist[i])
        mylist.insert(END, "--------------------------------------------------")
        mylist.insert(END, deslist[i])
        mylist.insert(END, "=================================================")
        print("=================================================")
    

def say_newses(titlelist,deslist):
  engine.say("Reading Newses")
  engine.runAndWait()
  for i in range(len(titlelist)):

        engine.say("Reading news "+str(i+1))
        engine.runAndWait()
        engine.say("Title")
        engine.runAndWait()
        engine.say(titlelist[i]) 
        engine.runAndWait()
        engine.say("News description ")
        engine.runAndWait()
        engine.say(deslist[i])
        engine.runAndWait()

lable_head = Label(root, text="Welcome to Intellegent Mirror", width=0, 
                   bg='white',fg='red', font=("bold", 35))
lable_head.place(x=250, y=13)
  
  
# Country  
lable_citi = Label(root, text="...", width=0, 
                   bg='white', font=("bold", 15))
lable_citi.place(x=1010, y=63)
  
lable_country = Label(root, text="...", width=0, 
                      bg='white', font=("bold", 15))
lable_country.place(x=  1135, y=63)


  

mylist = Listbox(root,width=140, height=25,bg="white" ,font=('Times', 12))

mylist.place( x = 100, y = 200 )

  
maxi = Label(root, text="Max. Temp: ", width=0, 
             bg='white', font=("bold", 15))
maxi.place(x=990, y=93)
  
max_temp = Label(root, text="...", width=0, 
                 bg='white', font=("bold", 15))
max_temp.place(x=1120, y=93)
  
  
mini = Label(root, text="Min. Temp.: ", width=0, 
             bg='white', font=("bold", 15))
mini.place(x=990, y=123)
  
min_temp = Label(root, text="...", width=0, 
                 bg='white', font=("bold", 15))
min_temp.place(x=1120, y=123)


ctemp = Label(root, text="Current Temp: ", width=0, 
             bg='white', font=("bold", 15))
ctemp.place(x=990, y=153)
  
cur_lab = Label(root, text="...", width=0, 
                 bg='white',fg='red', font=("bold", 15))
cur_lab.place(x=1120, y=153)

  
# API Call
api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                           + "Kozhikode"+ "&units=metric&appid="+"ff4b49683cbccf221aa809d76b174af8")

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


from newsapi import NewsApiClient

nsapi = NewsApiClient(api_key='4c6fd07fb18c436fb078d016002977f2')

news=nsapi.get_top_headlines(sources='bbc-news')

print(news)

titlelist=[]
deslist=[]
for new in news['articles']:

    title=str(new['title'])
    description=str(new['description'])

    titlelist.append(title)
    deslist.append(description)

root.after(2000, lambda :add_news(titlelist,deslist))

root.after(5000, lambda :say_newses(titlelist,deslist))

  
  
root.mainloop()