import telebot
import random
from telebot import types
from pytube import YouTube

token='5490598355:AAGobFjSfKbEEFwrDlXfH58CohurNHbJmQI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Отправьте ссылку' )

@bot.message_handler(content_types=['text'])
def get_video(msg):
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename, 'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id, 'Приятного просмотра')

bot.polling()

'''
import telebot
from googletrans import Translator
from telebot import types

token = '5436717411:AAFzo36HZcP3ILr4ibU84CJj-NuwWyj8Uqw'

bot = telebot.TeleBot(token)
lang = ''
@bot.message_handler(commands=['start'])
def start(message):
    k = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_1 = types.KeyboardButton('English')
    button_2 = types.KeyboardButton('France')
    k.add(button_1, button_2)
    bot.send_message(message.chat.id, 'Привет', reply_markup=k )

@bot.message_handler(content_types=['text'])
def answer(message):
    global lang
    if message.text == 'English':
        lang = 'en'
    elif message.text == 'France':
        lang = 'fr'
    m = bot.reply_to(message, 'Текст!')
    bot.register_next_step_handler(m, translator_text_ai)

def translator_text_ai(message):
    global lang
    translator = Translator()
    text = translator. translate(message.text, dest=lang)
    bot.send_message(message.chat.id, text.text)

bot.polling()
'''



'''import requests
import bs4
import lxml
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.wildberries.ru/')

headers = {
    "Accept": "/",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
}

link = 'https://www.wildberries.ru/'
data = requests.get(link)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#prices = soup.findAll('span', class_='lower-price')
print(soup)
'''


'''a = int(input(':'))
b = int(input(':'))
c = int(input(':'))
s = int(input(':'))

print(a*a*a+b*b*b+c*c*c+s*s*s)
'''



'''a = input(':')
b = input(':')
c = input(':')
if a== b==c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
    '''



'''a=input(':')
b=input(':')
if a>=b:
    print(a)
elif b>=a:
    print(b)
    '''


'''def even_odd(num):
    if num%2==0:
        print('Равно', num)
    elif num%2!=0:
        print('Не равно',num)


even_odd(10)
even_odd(7)
even_odd(19)
'''

'''def sayHello(name, age):
    print('Hello, ' +name, '.You are', age)

sayHello('Erasyl', 15)
'''


'''while True:
    a = int(input('a:'))
    b = int(input('b:'))
    c = int(input('c:'))
    if c<a<b:
        print(a)
    elif c<b<a:
        print(b)
    elif a<c<b:
        print(c)
        '''

'''
a = 204290
b = 539224
c = 29990
f = 11990
print(3*(a+b+c+f))
'''



'''
while True:
    me = int(input('me:'))
    you = int(input('you:'))
    sign = input('sign:')
    if sign == '+' :
        print(me+you)
    elif sign == '-':
        print(me-you)
    elif sign == '*':
        print(me*you)
    elif sign == '//':
        print(me//you)
'''
        
    

'''import random
import time
compScore=0
meScore=0
while True:
    # если сгенерировалось число 1
        comp = 'Камень'
    elif n == 2:
        comp = 'Ножницы'
    else:
        comp = 'Бумага'
    print('__________________________________')    
    me = input('Камень, Ножницы или Бумага: ')
    print('Компьютер думает . . .')
    time.sleep(3)
    print('Компьютер выбрал:', comp)
    if comp == 'Камень': # для камня
        if me == 'Камень':
            print('Ничья')
        elif me == 'Ножницы':
            print('Компьютер победил')
            compScore+=1
        else:
            print('Ты победил')
            meScore+=1
    elif comp == 'Ножницы': # для ножниц
        if me == 'Ножницы':
            print('Ничья')
        elif me == 'Бумага':
            print('Компьютер победил')
            compScore+=1
        else:
            print('Ты победил')
            meScore+=1
    elif comp == 'Бумага': # для бумаги
        if me == 'Бумага':
            print('Ничья')
        elif me == 'Камень':
            print('Компьютер победил')
            compScore+=1
        else:
            print('Ты победил')
            meScore+=1
    print('Компьютер:',compScore, '-', meScore,':ты')
    if compScore==3:
            print('Игра завершена. Компьютер победил')
            break
    elif meScore==3:
            print('Игра завершена.Ты победил')
            break
    want=input('did you want to stop:')
    '''

'''
import random

import time
n=random.randint(1,10)
while True:
 n=random.randint
 comp=
        me = int(input('Выберите число: '))
        print('Компьютер думает . . .')
        time.sleep(3)
        print('Компьютер выбрал:',comp)
        if me == 'n':
                print('Ты победил')
        elif me!='n':
                print('у тебя еще 2 попытки')
        if me == 'n':
                print('ты победил')
        elif me!='n':
                print('у тебя еще 1 попытка')
        if me == 'n':
                print('ты победил')
        elif me != 'n':
                print('конец')
'''                '''
count=0
while count <= 10:
    if count %2!=0:
      print(count)
    count+=1
'''
'''
while True:
        score=int(input('score:'))
        if score<50:
           print('F')
        elif score<= 74:
           print('C')
        elif score<= 89:
           print('B')
        elif score<=100:
            print('A')
        else:
            print('not found')
'''
'''
login=input('login:')
password=int(input('password:'))

if login=='qwerty' and password==123:
    print('welcome')
else:
    print('incorrect')
'''

'''while True:
    month=int(input('Month:'))
    if month==1 or month== 2 or month== 12:
       print('winter')
    elif month== 3 or month== 4 or month== 5:
         print('vesna')
    elif month== 6 or month== 7 or month== 8:
        print('leto')
    elif month== 9 or month==10 or month== 11:
        print('osen')
    else:('not found')    
 '''

'''while True:
    month=int(input('Month:'))
    if month%4 and month%400 or not(month%100):
        print('год високосный')
    else:
        print('год не високосный')
 '''             '''
for i in range(2,11,2):
    print(i)
'''

'''s=['bread','milk','water','chocolate']
for i in range (len(s))
 del s[i]
 print(s[i])
    
contacts=['Alina','Kira','Amina']
for element in contacts
    print(element) 
while True:
    print('1.Add')
    print('2.Delete')
    print('3.Edit')
    print('4.Find')
    print('5.Show all contacts')

    option=int(input('Choose option:'))
    if option==1:
        name= input('Contact to add:')
        contacts.insert(0,name)
        print('Added', contacts)
    elif option==2:
        name=input('Choose to delete:')
        for i in range(len(contacts)):
          if contacts[i]==name:
           contacts.remove(name)
           print('deleted', name)
           break
        else:
          print('Not found')
    elif option==3:
        name=input('Contact to edit:')
        if name in contacts:
            newname=input('new name:')
            contacts[index]=newname
            print('Edited',contacts)
        else:
           print('Not found',name)
    elif option==4:
        name=input('Choose to find:')
        for i in range(len(contacts)):
          if contacts[i]==name:
              print(name)
              break
        else:
             print('Not found')
             
    elif option==5:     
       for i in range(len(contacts)):
          print(contacts[i])

s=[1,2,3,4,5,6,8,14,19,2,2]
for i in range(len(s)):
 if s[i]%2==0:
    print(s[i])
 
s=[1,2,3,4,5,6,7]
a=[]
for i in range(len(s)-1,-1,-1):
 a.append(s[i])
print(a)

s[1,2,3,4,5,6,7]

word='hello'
a=0
for letter in word:
 if  'l'==letter:
     a+=1
   
print(a)


s='Monsdfday'
a='Tueasdfsday'
b=[]
for i in s:
    if i in a:
       b.append(i)
print(b)









s='world is big'.split()
for i in s:
 if i=='big':
  print(i)

name='madina'
age=25
print(f'my name is {name}.i am {age} ')
     
import requests

city=input('city:')
link=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d'
data=requests.get(link).json()
temp=round(data['main']['temp'])
desc=data['weather'][0]['description']
print(f'Temp in city: {temp},{desc}')

a=4
b=5
a,b=b,a
print(a,b)

import requests

link='https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40'
a=requests.get(link).json()
b=a['rates']['KZT']
tenge=int(input('tenge:'))
c=tenge//b
print(c)

from tkinter import * #import everything

def click():
    print('ТЫ ЛОХ')

wn=Tk()# create window
wn.title('ты лох') #title
wn.geometry('200x200') #size of window
#wn.rezible(False,False)
wn.config(bg='#99ccff')

#VIDGET
text=Label(text='ТЫ ЛОХ',bg='#99ccff',fg='white',font=('Ariel',100,'bold'))
text.pack()#метод распаковщик

#поле


from tkinter import *
import requests
import bs4
import os
os.makedirs('images',exist_ok=True)
def click():
    link=entry.get()
    data=requests.get(link)
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    images=soup.findAll('img')
   
    s=[]
    for i in images:
        src=i.get('src')
        if src!='':
         name=src.split('=')
         if len(name)>1:
             data2=requests.get(src)
             file=open('images/'+name[1]+'.jpg','wb')
             file.write(data2.content) 
             file.close
    print('Done')         
wn=Tk()# create window
wn.title('недо пинтерест') #title

wn.config(bg='#99ccff')
text=Label(text='Введите ссылку',bg='#99ccff',fg='white',font=('Ariel',100,'bold'))
text.pack()
entry=Entry(width=20,borderwidth=5,font=16)
entry.pack()
button=Button(text='Скачать',command=click)
button.pack(pady=5)

'''
'''
import requests
from tkinter import*

link='https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40'
data=requests.get(link).json()
rates=data['rates']

def c_kzt():
    kzt=float(kztentry.get())
    usd=round(kzt/rates['KZT'],2)
    eur=round(usd/rates['EUR'],2)
    USD.set(usd)
    EUR.set(eur)
    


wn=Tk()
wn.title('currency')
wn.geometry('250x100')
kztlabel=Label(text='KZT',font=('Arial',16,'bold'))
kztlabel.grid(column=0,row=0)

KZT=StringVar()
kztentry=Entry(textvariable=KZT)
kztentry.grid(column=1,row=0)

kztbutton=Button(text='convert',command=c_kzt)
kztbutton.grid(column=2,row=0,padx=10)

usdlabel=Label(text='USD',font=('Arial',16,'bold'))
usdlabel.grid(column=0,row=1)

USD=StringVar()
usdentry=Entry(textvariable=USD)
usdentry.grid(column=1,row=1)

usdbutton=Button(text='convert')
usdbutton.grid(column=2,row=1)

eurlabel=Label(text='EUR',font=('Arial',16,'bold'))
eurlabel.grid(column=0,row=2)

EUR=StringVar()
eurentry=Entry(textvariable=EUR)
eurentry.grid(column=1,row=2)

eurbutton=Button(text='convert')
eurbutton.grid(column=2,row=2)

wn.bind('<Return>',c_kzt)
'''




          
    
