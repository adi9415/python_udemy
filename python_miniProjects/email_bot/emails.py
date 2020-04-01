import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os. path similarity

html = Template(Path('index.html').read_text())
#print(html)


email = EmailMessage()

email['From'] = ''
email['To'] = ''
email['Subject'] = ''

email.set_content(html.substitute({'name' : 'Aditya'}), 'html')

with smtplib .SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()         # encryption mechanism
    smtp.login()
    smtp.send_message(email)
    print('message sent !!')