import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Akshay Reddy'
email['to'] = 'sakshayreddy66@gmail.com'
email['subject'] = 'design patterns lab manual'

email.set_content(html.substitute({'name':'Akshay'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sakshayreddy333@gmail.com', 'Akshay.pika')
    smtp.send_message(email)
    print('all done bosss!!!!!!!!!!!1111')
