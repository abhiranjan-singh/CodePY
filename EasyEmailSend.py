import pip
import socketserver
import socket
import _socket
import smtplib
import requests
EMAIL_ADD = 'abhiranjansingh786@gmail.com'
EMAIL_PASS = 'Kartar@bhi1'
r = requests.get('https://mcacms.gov.in')
w =requests.get('https://api.mcacms.gov.in')
print (w)


print(r)
if r.status_code == 200:
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADD, EMAIL_PASS)
        subject = 'YOUR SITE IS UP'
        body = "Make Sure Site is UP"
        msg = f'Subject:  {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADD, 'abhiranjan.singh@nisg.org' , msg)