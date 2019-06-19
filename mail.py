import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import csv
from time import sleep

FROM_ADDRESS = 'test@test.com' 
MY_PASSWORD = 'test'
SMTP_SERVER = ''
PORT ='587'
ADDRESSFILE = 'list_address.csv'
ATTACHFILE = 'test.pdf'

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    body = MIMEText(body)
    msg.attach(body)

    fo = open(ATTACHFILE, 'rb')
    attach = MIMEApplication(fo.read(), _subtype="pdf", filename=ATTACHFILE)
    fo.close()
    # encoders.encode_base64(attachment)
    # attach.add_header('Content-Dispositon','attachment',filename=ATTACHFILE)
    msg.attach(attach)

    return msg

def send_mail(from_addr, to_addr, body_msg):
    smtpobj = smtplib.SMTP(SMTP_SERVER, PORT)
    smtpobj.ehlo()
    # smtpobj.starttls()
    # smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addr, body_msg.as_string())
    smtpobj.close()

def get_address():
	f = open(ADDRESSFILE, 'r')
	reader = csv.reader(f)
	address = []
	for row in reader:
		address.append(row)
	return address

from_addr = 'fromtest@test.com'
to_addr = 'totest@test.com'
subject = 'こちらはメッセージのタイトルになります。' 
body = '''御中

ここにはメールの内部に記載するメッセージを複数行に渡って記入することが可能です。

改行や空白も反映されます。

'''

def mails(from_addr, company_address, subject, body):
	to_addr = company_address[1]
	body = company_address[0] + body

	msg = create_message(from_addr, to_addr, subject, body)
	send_mail(from_addr, to_addr, msg)
	print(from_addr)
	print(to_addr)
	print('You sent this mail!')
	# print(msg)
	sleep(10) # メール送るときのインターバルの時間を設定可能


address_list = get_address()

for a_l in address_list:
	mails(from_addr, a_l, subject, body)
