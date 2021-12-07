import smtplib
from email.mime.multipart import MIMEMultipart

# Settings
from_mail = "ilovemamals2001@gmail.com"
from_password = "486215379s"

to_mail = "ilovemamals2002@gmail.com"

smtp_server = "smtp.gmail.com"
smtp_port = 465

# Create the email message
msg = MIMEMultipart()
msg['Subject'] = 'Test Mail 1'
msg['From'] = from_mail
msg['To'] = to_mail
msg.preamble = 'Simple Test One: Time Analysis'

# Send mail
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.ehlo()
server.login(from_mail, from_password)
server.sendmail(from_mail, to_mail, msg.as_string())
server.quit()
