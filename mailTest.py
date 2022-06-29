from ctypes.wintypes import MSG
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

#read the configuration file and get all the connections
config = configparser.Configparser()
config.read('config.ini')

def sendRemainder(receiver_address, subject,msg,departmentDetails):
    #The mail addresses and password

    #----------------Enter the email address and the password in to the config file-------------------
    sender_address = config.get('SenderMail','sender_address')
    sender_pass = config.get('SenderMail','sender_pass')
    #-------------------------------------------------------------------------------------------------

    #Setup the MIME :MIME (Multipurpose Internet Mail Extensions) is an extension of 
    #the original Simple Mail Transport Protocol (SMTP) email protocol.
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    
    #The body and the attachments for the mail
    
    #mail_content_coordinator = msg
    #message.attach(MIMEText(mail_content_coordinator, 'plain'))
    
    #------------------------------------------------customizing the message content----------------------------------------------------
    messageBody = msg.split("|")
    departmentName = ''
    departmentContactNumber =''
    departmentEmail =''
    for row in departmentDetails:
        departmentName = row[0]
        departmentEmail = row[1]
        departmentContactNumber = row[2]
    
    #---------------------------------------to-------task-----Dr.name,--message--date-----
    message.attach(MIMEText('<html><body><p>{}</p><h3>{}</h3><p>{}</p><p>{}<b>{}</b></p>Thank you.</body></html>'.format(messageBody[0],messageBody[1],messageBody[2],messageBody[3],messageBody[4],messageBody[5]), 'html', 'utf-8'))
    
    # GIF countdown timer(only for few seconds) 
    #message.attach(MIMEText('<html><body>' +
    #                            '<p><img src="https://gifcdn.com/d1g6op3cb9h68pj2d1n.gif?v=1656471377"></p>' +
    #                           '</body></html>', 'html', 'utf-8')

    #ignore message
    message.attach(MIMEText('<html><body>' +
                                '<h4><i>{}</i></h4>'.format(messageBody[5]) +
                                '</body></html>', 'html', 'utf-8'))

    message.attach(MIMEText('<html><body><p style="color:MediumSeaGreen;">This is a system generated email!</p><br><br><p>Contact:<br><b><ul><li>{}</li><li>{}</li></ul></p><br>{}<br>Faculty of Engineering<br>University of Peradeniya</b></p></body></html>'.format(departmentEmail,departmentContactNumber,departmentName), 'html', 'utf-8'))
    
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
