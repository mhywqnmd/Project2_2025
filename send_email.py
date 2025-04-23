import smtplib
from email.message import EmailMessage
#set the sender email and password and recipient emaic
from_email_addr = "3568958292@qq.com"
from_email_pass = "zcrtuleqlsigdagg"
to_email_addr = "3251995934@qq.com"
# Creat a message object
msg = EmailMessage()
#Set the email body
body ="Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr

msg['Subject'] = 'TEST EMAIL'
server = smtplib.SMTP('smtp.qq.com', 587)

server.starttls()

server.login(from_email_addr,from_email_pass)
server.send_message(msg)

print('Email sent')

server.quit()
