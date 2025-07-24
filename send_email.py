import smtplib, ssl
import os

from Home import message
def sendmail(message):

    host = "smtp.gmail.com"
    port = 465
    username = "2004rayban@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "shantanu0116@gmail.com"

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)