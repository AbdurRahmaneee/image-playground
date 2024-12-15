import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Abdur Rahman'
email['to'] = 'ar.abdurrahman.ar@outlook.com'
email['subject'] = 'Learning to send email using python'

email.set_content(html.substitute({'name':'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ar.abdurrahmaneee@gmail.com', 'cwss orth anwg zaxw')
    smtp.send_message(email)
    print('all good boss')