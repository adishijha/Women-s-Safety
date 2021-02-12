import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64


def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()
    server.login("adishiritwickjha@gmail.com", "Adishijha@1908")
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = 'EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
   
    msg['From'] = formataddr(("TEAM RESCUE", "adishiritwickjha@gmail.com"))

    server.sendmail("adishiritwickjha@gmail.com", dest, msg.as_string())
    server.quit()