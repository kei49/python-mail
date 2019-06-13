import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = '' 
MY_PASSWORD = ''
SMTP_SERVER = ''
PORT =''

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send_mail(from_addr, to_addr, body_msg):
    smtpobj = smtplib.SMTP(SMTP_SERVER, PORT)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addr, body_msg.as_string())
    smtpobj.close()


from_addr = FROM_ADDRESS
to_addr = 'test@gmail.com'
subject = 'This is the title of the mail'
body = 'This is the body of the mail'

msg = create_message(from_addr, to_addr, subject, body)
send_mail(from_addr, to_addr, msg)
print('You sent a message!')

