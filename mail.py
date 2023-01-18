import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:

    def __init__(self, smtp, imap, login, password):
        self.imap = imap
        self.smtp = smtp
        self.login = login
        self.password = password

    def send_mail(self, recipients, subject):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message))
        send_message = smtplib.SMTP(self.smtp, 587)
        send_message.ehlo()
        send_message.starttls()
        send_message.ehlo()
        send_message.login(self.login, self.password)
        send_message.sendmail(self.login, send_message, message.as_string())
        send_message.quit()

    def recieve_mail(self, header):
        connect_imap = imaplib.IMAP4_SSL(self.imap)
        connect_imap.login(self.login, self.password)
        connect_imap.list()
        connect_imap.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = connect_imap.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = connect_imap.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        connect_imap.logout()


if __name__ == '__main__':
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None
    gmail = Mail(gmail_smtp, gmail_imap, login, password)
    gmail.send_mail(recipients, subject)
    gmail.recieve_mail(header)
