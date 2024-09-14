#Program in python to automate mails in python using smtp library

import smtplib

def automate_mail():

    #Email configuration
    sender_email = "example@gmail.com"
    password = "PASSWORD"
    receiver_email = "reciever.mail@gmail.com"
    subject= "this is the subject"
    body= "this is the body of the automated mail sent using python"

    #create message
    message= f"Subject: {subject}\n\n{body}"

    #server configuration(for gmail)
    smtp_server= "smtp.gmail.com"
    smtp_port= 587


    #establish a secure connection with the server
    server= smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    #send the mail
    server.sendmail(sender_email, receiver_email, message)


    #quit the smtp server connection
    server.quit()


                