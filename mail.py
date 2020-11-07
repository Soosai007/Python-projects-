# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("ssubashn8@gmail.com", "your password") 

# message to be sent 
message = "hi"

# sending the mail 
s.sendmail("ssubashn8@gmail.com", "ssubashn8@gmail.com", message) 

# terminating the session 
s.quit()
