from email_app.Serializers.EmailSerializer import EmailSerializer
from email_app.Stores.EmailStore import EmailStore
from rest_framework.exceptions import ValidationError
import smtplib
from EmailBackend.config import *
from email.mime.text import MIMEText

SMTP_SERVER = SMTP_SERVER
SMTP_PORT = SMTP_PORT


class EmailManager:
    def __init__(self):
        self.store = EmailStore()

    def get_all_emails(self, page):
        limit = 10
        offset = (page - 1) * limit
        emails = self.store.get_all_emails(offset, limit)
        emails_data = EmailSerializer(emails, many=True).data
        return {'data': emails_data}

    def get_email_details(self, email_id):
        data = self.store.get_email(email_id)
        email = EmailSerializer(data).data
        return {'data': email}

    def create_email(self, data):
        serializer = EmailSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError({"error": serializer.errors})
        serializer.save()
        email = serializer.data
        print('Created Email:', email)

    def send_email(self, message):
        email_id = message['email_id']
        sender_email = message['sender']
        subject = message['subject']
        description = message['description']
        print(f'Sending response to {sender_email}')
        template_subject = subject
        template_body = description

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(USERNAME, PASSWORD)

        msg = MIMEText(template_body)
        msg['Subject'] = template_subject
        msg['From'] = USERNAME
        msg['To'] = sender_email

        # Send the email
        server.sendmail(USERNAME, sender_email, msg.as_string())
        print('Email sent, Yooooo !!')
        self.store.delete_email(email_id)
        server.quit()
