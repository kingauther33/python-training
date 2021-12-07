from datetime import datetime, date
import os
import smtplib
import pathlib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.base import MIMEBase

# Save the plot with date as filename in ./results/
filename = str(date.today()) + ".png"

# Working directory
dir = pathlib.Path(__file__).parent.absolute()

# Folder plot should be saved
folder = r"/results/"

# Path to image
path_plot = str(dir) + folder + filename

os.environ['FROM_MAIL'] = "ilovemamals2001@gmail.com"
os.environ['FROM_PASSWORD'] = "486215379s"
os.environ['TO_MAIL'] = "huavinhvietanh@myrmicatech.com"

# Settings
from_mail = os.environ['FROM_MAIL']
from_password = os.environ['FROM_PASSWORD']

to_mail = os.environ['TO_MAIL']

smtp_server = "smtp.gmail.com"
smtp_port = 465


def send_email(path_plot, smtp_server, smtp_port, from_mail, from_password, to_mail):
    '''
      Send results via mail
    '''

    # Create the email message
    msg = MIMEMultipart()

    msg['Subject'] = 'Data Report: Example Chart'
    msg['From'] = from_mail
    COMMASPACE = ', '
    msg['To'] = COMMASPACE.join([from_mail, to_mail])
    msg.preamble = 'Data Report: Example Chart'

    # Open the files in binary mode and attach to mail
    with open(path_plot, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header("Content-Disposition", 'attachment',
                       filename='example_plot.png')
        img.add_header("X-Attachment-Id", '0')
        img.add_header('Content-ID', '<0>')
        fp.close()
        msg.attach(img)

    # Attach HTML Body
    msg.attach(MIMEText(
        '''
        <html>
          <body>
            <h1 style="text-align: center;">Example Chart</h1>
            <p>This is a demo</p>
            <p><img src="cid:0" style="width: 100%;" /></p>
          </body>
        </html>
      ''',
        'html', 'utf-8'
    ))

    # Send mail
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(from_mail, from_password)

    server.sendmail(from_mail, [from_mail, to_mail], msg.as_string())
    server.quit()


send_email(path_plot, smtp_server, smtp_port,
           from_mail, from_password, to_mail)
