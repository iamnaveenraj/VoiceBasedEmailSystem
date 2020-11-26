import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import sys


#Project Name

print("-"*60)
print("Voice Based Email System For Visually Impaired People")
print("-"*60)
tts = gTTS(text="Voice Based Email System For Visually Impaired People", lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)


#login from os
login = os.getlogin
print("-"*60)
print ("You are logging from : "+login())
print("-"*60)
tts = gTTS(text="You are logging from :  "+login(), lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#choices
print("\n")
print("-"*60)
print ("1. Composed A Mail")
tts = gTTS(text="option 1. composed a mail", lang='en')
ttsname=("hello.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

print ("2. Check Your Inbox")
print("-"*60)
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=("second.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

#this is for input choices
print("\n")
print("-"*60)
print("Your Choice")
tts = gTTS(text="Your choice ", lang='en')
ttsname=("hello.mp3") 
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(ttsname)

r = sr.Recognizer()      #voice recognition part
with sr.Microphone() as source:
    audio=r.listen(source)
    print ("OK Done!!")
    tts = gTTS(text="OK Done", lang='en')
    ttsname=("ok.mp3") 
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

try:
    text=r.recognize_google(audio)
    print ("You Said : "+text)
    tts = gTTS(text="You Said"+text, lang='en')
    ttsname=("said.mp3") 
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)
    
except sr.UnknownValueError:
    print("Google Speech Recognition Could Not Understand Your Voice")
    tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice.", lang='en')
    ttsname=("except.mp3") 
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)
    os._exit(0)
    
print("-"*60)
print("\n")
    

#choices details
if text == '1' or text == 'One' or text == 'one' or text =='option one' or text =='van':
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        print("\n")
        print("-"*60)
        print ("Your Message :")
        tts = gTTS(text="Your Message", lang='en')
        ttsname=("msg.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
        print ("OK Done!!")
        tts = gTTS(text="OK Done", lang='en')
        ttsname=("ok1.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
    try:
        text1=r.recognize_google(audio)
        print ("You Said : "+text1)
        tts = gTTS(text="You Said"+text1, lang='en')
        ttsname=("said1.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)

    print("-"*60)

    print("\n")
    
    print("-"*60)
    
    mail = smtplib.SMTP('smtp.gmail.com',587)                   #host and port area
    mail.ehlo()                                                 
    mail.starttls()                                             #security connection

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Email")
        
        tts = gTTS(text="You Email",lang='en')
        ttsname=("ueamil.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
    try:
        emailtext=r.recognize_google(audio)
        emailtext1=emailtext.replace(" ","")
        emailtext2=emailtext1.lower()
        print ("You Email is :"+emailtext2)
        tts = gTTS(text="You Email is"+emailtext,lang='en')
        ttsname=("usersaid.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)
        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Password")
        
        tts = gTTS(text="Your Password :",lang='en')
        ttsname=("upassword.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
    try:
        pswrdtext=r.recognize_google(audio)
        pswrdtext1=pswrdtext.replace(" ","")
        print ("You Password is :"+pswrdtext1)
        tts = gTTS(text="You Password is"+pswrdtext1,lang='en')
        ttsname=("pwdsaid.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)

        
    mail.login(emailtext2,pswrdtext1)#login part

    
    r = sr.Recognizer()           #Sender part
    with sr.Microphone() as source:
        print("Reciver Email")
        
        tts = gTTS(text="Reciver Email :",lang='en')
        ttsname=("seamil.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
    try:
        rtext=r.recognize_google(audio)
        rtext1=rtext.replace(" ","")
        rtext2=rtext1.lower()
        print ("Reciver Email is : "+rtext2)
        tts = gTTS(text="Reciver Email is "+rtext2,lang='en')
        ttsname=("ssaid.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)
        
    mail.sendmail(emailtext2,rtext2,msg) #send part
    
    print ("Congratulations! Your mail has send successfully. ")
    
    tts = gTTS(text="Congratulations! Your mail has send successfully. ", lang='en')
    ttsname=("send.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    os._exit()

if  text == 'to' or text == 'Two' or text =='Tu' or text =='tu' or text =='Two' or text=='Option two' or text=='option 2' or text == 'option tu':
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)#this is host and port area.... ssl security

    print("-"*60)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Email")
        
        tts = gTTS(text="You Email",lang='en')
        ttsname=("ueamil.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
    try:
        emailtext=r.recognize_google(audio)
        emailtext1=emailtext.replace(" ","")
        emailtext2=emailtext1.lower()
        print ("You Email is :"+emailtext2)
        tts = gTTS(text="You Email is"+emailtext,lang='en')
        ttsname=("usersaid.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)
        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Password")
        
        tts = gTTS(text="Your Password :",lang='en')
        ttsname=("upassword.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
        audio=r.listen(source)
    try:
        pswrdtext=r.recognize_google(audio)
        pswrdtext1=pswrdtext.replace(" ","")
        print ("You Password is :"+pswrdtext1)
        tts = gTTS(text="You Password is"+pswrdtext1,lang='en')
        ttsname=("pwdsaid.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition Could Not Understand Your Voice")
        tts = gTTS(text="Google Speech Recognition Could Not Understand Your Voice", lang='en')
        ttsname=("except.mp3") 
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)
        os._exit(0)
        
    print("-"*60)

    print("\n")
    print("-"*60)
    mail.login(emailtext2,pswrdtext1)
    
    stat, total = mail.select('Inbox')                                                      #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    ts = gTTS(text="Total mails are :"+str(total), lang='en')                              #voice out
    tsname=("total.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    print("-"*60)
    print("\n")

    #search mails

    print("-"*60)
    
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=("mail.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    ts = gTTS(text="Body: "+txt, lang='en')
    tsname=("body.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()
    mail.logout()
    print("-"*60)
    os._exit(0)

else :
    os._exit(0)
