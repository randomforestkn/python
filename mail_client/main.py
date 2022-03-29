import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import ktp

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.login("example@gmail.com", ktp.password )

msg = MIMEMultipart()
msg['From'] = 'Charlie'
msg['To'] = 'example@hotmail.com'
msg['Subject'] = 'hello'

with open('hello.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

text = msg.as_string()
server.sendmail("example@gmail.com",'example@hotmail.com',text)
