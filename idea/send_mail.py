# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(r'reports\reports\Test_TestBank_2018-03-08_16-45-57.html', 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % 'Test_TestBank_2018-03-08_16-45-57.html'
msg['From'] = 'sp.aditya@gmail.com'
msg['To'] = 'spaditya@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login('sp.aditya@gmail.com', <enterpassword>)

server.sendmail('sp.aditya@gmail.com', ['spaditya@gmail.com'], msg.as_string())
server.quit()