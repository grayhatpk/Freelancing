
"""First Set the passwords for the email and Outlook server, then run the code. """

import pandas as pd
import smtplib
from time import sleep
from email.mime.text import MIMEText

'''Change these to your credentials and name '''

your_name = "Under the Water"           # This Name will appear on the Email Sender Name
your_email = "abc@gmail.com"            # This is My Email from which I will send the Emails   
your_password = "123"                   # This is Password of Email account 
server_password= "serer123"              # THis is the password of the Outlook SMTP Sever    

subject = "Greetings!"
message= ""


""" If you are using something other than gmail then change the 'smtp.gmail.com' and 465 in the line below"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo() 
server.starttls() 
server.login(your_email, server_password)


# Read the file. 
email_list = pd.read_excel("EmailList.xlsx")  

# Get all the Names, Email Addreses, Subjects and Messages
all_names = email_list['Name']
all_emails = email_list['Email']

msg_type=email_list["MSJTYPE"]     


# Loop through the emails
for idx in range(len(all_emails)):

    # Get each records name, email, subject and message
    name = all_names[idx]
    email = all_emails[idx]
    msg_type_value = msg_type[idx]

    name = "message" + str(msg_type_value) + ".html"
    
    #Now Reading the Email from the text file based on the msg value.The message is in the seprate file.
     
    with open(name,'r') as msg: 
        message=msg.read()
        

    """   You must this code if you want to send the code of the html in the message. """
    """
    full_email = ("From: {0} <{1}>\n"
    "To: {2} <{3}>\n"
    "Subject: {4}\n\n"
    "{5}"
    .format(your_name, your_email, name, email, subject, message)) """

    
    
    """creating the html message in the running code and sends the output of the code. 
     Now if you want to send the output of the html code, then you must use this code. """
    
    msg = MIMEText(message, 'html')
    msg['From'] = your_email
    msg['To'] = email
    msg['Subject'] = subject 
    
    
    # In the email field, you can add multiple other emails if you want
    # all of them to receive the same text
    try:
        # If you are sending the code of the html in the message, then run this code line and commant the 76 line code. 
        #server.sendmail(your_email, [email], full_email) 
        
        server.send_message(msg)  
        
        sleep(6)
        print('Email to {} successfully sent!'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))

# Close the smtp server
server.close()