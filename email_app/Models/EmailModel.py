from mongoengine import fields, Document
from datetime import datetime


class Email(Document):
    sender = fields.EmailField()
    subject = fields.StringField()
    description = fields.StringField()
    created_at = fields.DateTimeField(default=datetime.utcnow)

    class Meta:
        db_alias = 'default'
        collection = 'email'
