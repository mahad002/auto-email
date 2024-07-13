import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import os # add this line if you want to use the environment variables

# This script can be used for various tasks such reminders, sending daily reports, scheduling tasks, etc.

# In fact this can also be used to perform cold emails if you csv's through the script with names and email and repspective information

# Email configuration
# Load the email configuration from environment variables
# If you are running the script on your local machine, you can set the environment variables in your terminal
# export EMAIL_ADDRESS='your_email_address'
# export EMAIL_PASSWORD='your_email_password'
# If you are running the script on a server, you can set the environment variables in the server's configuration
# If you are using a service like Heroku, you can set the environment variables in the app settings

# Also in order to perform the email you'll need to enable the less secure apps in your google account 
# 1- Go to your Google Account.
# 2- Navigate to the Security section.
# 3- Scroll down to Less secure app access and turn it on.

# EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

EMAIL_ADDRESS='' # add your email address
EMAIL_PASSWORD='' # add your email password

print(EMAIL_ADDRESS)
SMTP_SERVER = 'smtp.gmail.com' # I have added smtp for gmail you can add the smtp server of your email provider
SMTP_PORT = 587  # typically 587 for TLS, 465 for SSL and 25 for non-secure connection 

# email content configuration
TO_EMAIL = '' # add the email address you want to send the email to
SUBJECT = 'Test Subject' # add the subject of the email
BODY = 'Hello, this is a test email sent from a Python script.' # add the body of the email

def send_email():
    # create message container
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # attach the body of the email to the MIME message
    msg.attach(MIMEText(BODY, 'plain'))

    try:
        # connect to the server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

# schedule the email to be sent daily at a specific time
# schedule.every().day.at("08:00").do(send_email)

send_email()

while True:
    schedule.run_pending()
    time.sleep(1)


# to start the script in the background run the following command
# nohup python send_daily_report.py &
# to stop the script run the following command
# ps -ef | grep send_daily_report.py

# to kill the process
# kill -9 PID
# PID is the process id of the script
# to get the process id run the following command

