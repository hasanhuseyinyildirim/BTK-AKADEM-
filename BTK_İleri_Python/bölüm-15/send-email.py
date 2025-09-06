import smtplib
from email.mime.text import MIMEText

port= 587
smtp_server="smtp-relay.brevo.com"
login="deneme@smtp.brevo.com"
password="1234"

sender_email="info@hasan.com"
receiver_email="alacak_posta@email.com"

text=""" 
    Merhaba,deneme epostası
"""

message=MIMEText(text,"plain")
message["Subject"]="Merhaba"
message["From"]=sender_email
message["To"]=receiver_email

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("eposta gönderildi")
