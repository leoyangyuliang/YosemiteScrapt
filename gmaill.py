import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.EMAIL_PASSWARD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS,message)
        server.quit()
        print("success email sent")
    except:
        print("something wrong")

subject = "test subject"
msg = "hello i am fine"

send_email(subject, msg)
