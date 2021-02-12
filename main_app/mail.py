import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64


def send_email(name, dest, link,state,city):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()
    server.login("EMail id", "Password")
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link,state=state,city=city)
    msg = MIMEMultipart()
    msg['Subject'] = 'EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
   
    msg['From'] = formataddr(("RESCUE ME", "EMail id"))

    server.sendmail("EMail id", dest, msg.as_string())
    server.quit()