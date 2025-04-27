import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
from date time import datetime

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

from_email_addr = "3568958292@qq.com"
from_email_pass = "zcrtuleqlsigdagg"
to_email_addr = "3251995934@qq.com"

for _ in range(4):
	if GPIO.input(channel):
		plant_status = "Water NOT needed"
	else:
		plant_status = "Please water your plant"

msg = EmailMessage()
msg.set_content(f"Plant status: {plant_status}")
msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'Plant watering Status'

server = smtplib.SMTP('smtp.qq.com',587)
server.starttls()
server.login(from_email_addr)
server.send_message(msg)
print(f"Email sent: {plant_status}")
server.quit()

time.sleep(6 * 60 * 60)
