from django.core.management.base import BaseCommand
from EmailBackend.config import *
import imaplib
import email
from email.utils import parseaddr
from email.header import decode_header
import webbrowser
import os
import time
from email_app.Managers.EmailManager import EmailManager

email_mgr = EmailManager()

# IMAP server settings
IMAP_SERVER = IMAP_SERVER
EMAIL = USERNAME
PASSWORD = PASSWORD


def consume_emails():
    # Search for unseen emails
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)

    # Select the mailbox (inbox)
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    if data != [b'']:
        for num in data[0].split():
            result, data = mail.fetch(num, '(RFC822)')
            if result == 'OK':
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                subject = msg['subject']
                sender = msg['from']
                sender_name, sender_address = parseaddr(sender)
                body = ''
                # Iterate through email parts to find the body
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode()
                        break
                email_mgr.create_email({
                    'subject': subject,
                    'description': body,
                    'sender': sender_address
                })
    else:
        print('No unseen emails')


class Command(BaseCommand):
    help = 'Description of my custom command'

    def handle(self, *args, **options):
        print("Consuming emails")
        while True:
            consume_emails()
            time.sleep(5)
