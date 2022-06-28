from ctypes.wintypes import MSG
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

#read the configuration file and get all the connections
config = configparser.Configparser()
config.read('config.ini')

def sendRemainder(receiver_address, subject,msg):
    #The mail addresses and password

    #----------------edit this [only if changing the sender's mail]-------------------------------------------
    sender_address = config.get('SenderMail','sender_address')
    sender_pass = config.get('SenderMail','sender_pass')
    #--------------------------------------------------------------------

    #Setup the MIME :MIME (Multipurpose Internet Mail Extensions) is an extension of 
    #the original Simple Mail Transport Protocol (SMTP) email protocol.
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    

    #The body and the attachments for the mail
    

    #message['Subject'] = '{}: {}-{} paper printing Remainder'.format(exam_title , course_code, course)   #The subject line
    message['Subject'] = subject
    mail_content_coordinator = msg
    message.attach(MIMEText(mail_content_coordinator, 'plain'))
    

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    
    #enable security
    session.starttls() 

    #login with mail_id and password
    session.login(sender_address, sender_pass)

    #converting the message into string
    text = message.as_string()
    
    #send email
    session.sendmail(sender_address, receiver_address, text)
    
    #end the session
    session.quit()
   
    print('Mail Sent')
