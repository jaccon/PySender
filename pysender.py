import json
import smtplib
import email.message
import os
import sys
import urllib, json
import time
import datetime
import HTMLParser

content = ('Apenas um teste de ')
msg = email.message.Message()
msg['Subject'] = 'Teste de envio subject'
msg['From'] = ' Gmail Sender <sender@gmail.com>'
msg['Reply-to'] = 'sender@gmail.com'
msg['To'] = 'sender@gmail.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(content)

user = 'sender@gmail.com'
password = "BDrt0ekFx5m9ZffH7LYhSZF+PIUHmi0UCITagY/aqsDe"
smtpServer = 'smtp.gmail.com'
smtpPort = '587'
s = smtplib.SMTP(smtpServer + ':' + smtpPort)

s.starttls()
s.login(user, password)
s.sendmail(msg['From'], [msg['To']], msg.as_string())