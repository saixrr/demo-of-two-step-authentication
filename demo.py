from tkinter import *
from tkinter import messagebox
import random as r
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import pyqrcode
import png
import os
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
ws=Tk()
ws.title('student Registration')
ws.geometry('1400x1400')
ws.config(bg='#04B2D9')
def validation():
    def nextpage():
        ws.destroy()
        wk=Tk()
        wk.title('Login using credentials')
        wk.geometry('1400x1400')
        wk.config(bg='#04B2D9')
        frame=Frame(wk,padx=10,pady=10)
        frame.pack(pady=30)
        def allow():
            def qr():
                s="The password is: "+str(b2)
                ur1=pyqrcode.create(s)
                ur1.svg("img2.svg",scale=8)
                ur1.png('img2.png',scale=6)
                img=cv2.imread("img2.png")
                det=cv2.QRCodeDetector()
                val,pts,st_code=det.detectAndDecode(img)
                I1=open('img2.png','rb').read()
                msg=MIMEMultipart()
                msg['Subject']='qrcodeforlogin'
                msg['From']='mail@gmail.com'
                msg['To']=a4
                text=MIMEText("qr to see your details: ")
                image=MIMEImage(I1,'jpg')
                msg.attach(text)
                msg.attach(image)
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.login("mail@gmail.com","")
                s.sendmail("mail@gmail.com",a4,str(msg))
                s.quit()
                cap=cv2.VideoCapture(0)
                cap.set(3,640)
                cap.set(4,480)
                camera=True
                L1=[]
                while camera ==True:
                    success,frame=cap.read()
                    for code in decode(frame):
                        if code.data.decode('utf-8') not in L1:
                            print('Approved,you can enter')
                            c1=(code.data.decode('utf-8'))
                            L1.append(c1)
                            time.sleep(5)
                        elif code.data.decode('utf-8')  in L1:
                            print('Not approved')
                            time.sleep(5)
                        print(code.type)
                        print(c1)
                        cv2.imshow('testing-code-scan',frame)
                        cv2.waitKey(0)
                        break
                        if(c1==val):
                            wm=Tk()
                            wm.title('Login using credentials')
                            wm.geometry('1400x1400')
                            wm.config(bg='#04B2D9')
                            frame=Frame(wm,padx=10,pady=10)
                            frame.pack(pady=30)
                            Label(frame,text='User Name: ').grid(row=0,column=1)
                            Label(frame,text=b1).grid(row=0,column=2)
                            Label(frame,text='password: ').grid(row=1,column=1)
                            Label(frame,text=b2).grid(row=1,column=2)
                            Label(frame,text='email:  ').grid(row=2,column=1)
                            Label(frame,text=a4).grid(row=2,column=2)
                            Label(frame,text='mobilenumber: ').grid(row=3,column=1)
                            Label(frame,text=a5).grid(row=3,column=2)
                        else:
                            print("unsuccessfull")
                        break
            def otp():
                  def verify():
                      msg=''
                      c2=c1.get()
                      print(c2)
                      print(l)
                      if(str(c2)==str(l)):
                          wn.destroy()
                          wm=Tk()
                          wm.title('verify')
                          wm.geometry('1400x1400')
                          wm.config(bg='#04B2D9')
                          frame=Frame(wm,padx=10,pady=10)
                          frame.pack(pady=30)
                          Label(frame,text='User Name: ').grid(row=0,column=1)
                          Label(frame,text=b1).grid(row=0,column=2)
                          Label(frame,text='password: ').grid(row=1,column=1)
                          Label(frame,text=b2).grid(row=1,column=2)
                          Label(frame,text='email:  ').grid(row=2,column=1)
                          Label(frame,text=a4).grid(row=2,column=2)
                          Label(frame,text='mobilenumber: ').grid(row=3,column=1)
                          Label(frame,text=a5).grid(row=3,column=2)
                      else:
                            msg="enter correct otp"
                            messagebox.showinfo('message',msg)
                  def otpgen():
                      otp=""
                      for i in range(4):
                          otp+=str(r.randint(1,9))
                      return otp
                  import os
                  from PIL import Image
                  import smtplib
                  from email.mime.text import MIMEText
                  from email.mime.image import MIMEImage
                  from email.mime.multipart import MIMEMultipart
                  msg=MIMEMultipart()
                  msg['Subject']='qrcodeforlogin'
                  msg['From']='mail@gmail.com'
                  msg['To']=a4
                  l=otpgen()
                  text=MIMEText("otp to see your details: "+ l)
                  msg.attach(text)
                  s=smtplib.SMTP('smtp.gmail.com',587)
                  s.ehlo()
                  s.starttls()
                  s.login("mail@gmail.com","")
                  s.sendmail("mail@gmail.com",a4,str(msg))
                  s.quit()
                  wk.destroy()
                  wn=Tk()
                  wn.title('Login using credentials')
                  wn.geometry('1400x1400')
                  wn.config(bg='#04B2D9')
                  frame=Frame(wn,padx=10,pady=10)
                  frame.pack(pady=30)
                  Label(frame,text='enter otp: ').grid(row=0,column=1)
                  c1=Entry(frame,font=('sans-sherif',14))
                  c1.grid(row=0,column=2)
                  Button(frame,text='verify',pady=10,padx=20,command=verify).grid(row=2,columnspan=3)
            b1=username1.get()
            b2=passwd1.get()
            b3=name
            b4=a2
            msg=" "
            if(b1!=b3):
                msg="no user with this name"
                messagebox.showinfo('message',msg)
            elif(b2!=b4):
               msg="incorrect password"
               messagebox.showinfo('message',msg)
            else:
                Button(frame,text='qrcode',pady=10,padx=20,command=qr).grid(row=3,column=0)
                Button(frame,text='otp',pady=10,padx=20,command=otp).grid(row=3,column=2)
                
        Label(frame,text='User Name: ').grid(row=0,column=1)
        username1=Entry(frame,font=('sans-sherif',14))
        username1.grid(row=0,column=2)
        Label(frame,text='Password: ').grid(row=1,column=1)
        passwd1=Entry(frame,show='*',font=('sans-sherif',14))
        passwd1.grid(row=1,column=2)
        Button(frame,text='Submit',pady=10,padx=20,command=allow).grid(row=2,columnspan=3)
        ws.mainloop()
    name=username.get()
    a2=passwd.get()
    a3=passwd1.get()
    a4=email.get()
    a5=mob.get()
    msg=" "
    if(len(name)==0):
        msg='name cant be empty'
        messagebox.showinfo('message',msg)
    elif any(ch.isdigit() for ch in name):
        msg='Name cant have numbers'
        messagebox.showinfo('message',msg)
    elif len(name)<=2:
        msg='name is too short'
        messagebox.showinfo('message',msg)
    elif len(name)>10:
        msg='name is too long'
        messagebox.showinfo('message',msg)
    elif(a2!=a3):
        msg='both password are not matching'
        messagebox.showinfo('message',msg)
    elif(len(a4)==0):
         msg='email is mandatory'
         messagebox.showinfo('message',msg)
    elif(a4[-10:]!="@gmail.com"):
        msg='enter valid email'
        messagebox.showinfo('message',msg)
    elif any(ch.isalpha() for ch in a5):
        msg='mobile cant have alphabets'
        messagebox.showinfo('message',msg)
    elif(len(a5)!=10):
        msg='enter valid mobile number'
        messagebox.showinfo('message',msg)
    else:
        msg='success'
        messagebox.showinfo('message',msg)
        Button(frame,text="Login",command=nextpage).grid(row=5,columnspan=3)
frame=Frame(ws,padx=10,pady=10)
frame.pack(pady=30)
Label(frame,text='User Name: ').grid(row=0,column=1)
username=Entry(frame,font=('sans-sherif',14))
username.grid(row=0,column=2)
a1=len(username.get())
Label(frame,text='Password: ').grid(row=1,column=1)
passwd=Entry(frame,show='*',font=('sans-sherif',14))
passwd.grid(row=1,column=2)
a2=passwd.get()
Label(frame,text='Confirm Password: ').grid(row=2,column=1)
passwd1=Entry(frame,show='*',font=('sans-sherif',14))
passwd1.grid(row=2,column=2)
a3=passwd1.get()
Label(frame,text='email: ').grid(row=3,column=1)
email=Entry(frame,font=('sans-sherif',14))
email.grid(row=3,column=2)
a4=email.get()
Label(frame,text='mobilenumber: ').grid(row=4,column=1)
mob=Entry(frame,font=('sans-sherif',14))
mob.grid(row=4,column=2)
a5=mob.get()
Button(frame,text='Submit',pady=10,padx=20,command=validation).grid(row=5,columnspan=3)
ws.mainloop()
