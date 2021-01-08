import smtplib
from email.message import EmailMessage
import getpass
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Saurav Kumar'
email['to'] = 'ehsaurav@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

print('Enter your credentials: ')
email_id = str(input('Email: '))
password = getpass.getpass('Password: ')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_id, password)
    smtp.send_message(email)
    print('All good boss!')
