import os
import ssl
import configparser
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read("config.ini")


def sendMailUsingSendGrid(API, from_email, to_emails, subject, html_content):
    if API != None and from_email != None and len(to_emails) > 0:
        message = Mail(from_email, to_emails, subject, html_content)
        try:
            sg = SendGridAPIClient(API)
            response = sg.send(message)
            print(response.status_codes)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


try:
    settings = ["SETTINGS"]
except:
    settings = {}

API = settings.get("APIKEY", None)
from_email = settings.get("from", None)
to_emails = settings.get("to", "")

subject = "Simple Test Message"
html_content = "Message successfully sent through python and sendgrid"

sendMailUsingSendGrid(API, from_email, to_emails, subject, html_content)
