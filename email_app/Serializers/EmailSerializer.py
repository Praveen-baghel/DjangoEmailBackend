from rest_framework_mongoengine.serializers import DocumentSerializer
from email_app.Models.EmailModel import Email


class EmailSerializer(DocumentSerializer):
    class Meta:
        model = Email
