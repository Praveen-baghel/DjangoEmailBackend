from email_app.Models.EmailModel import Email


class EmailStore:
    def get_all_emails(self, offset, limit):
        emails = list(Email.objects.filter().order_by('-id').all()[offset:offset + limit])
        return emails

    def get_email(self, id):
        email = Email.objects.filter(id=id).first()
        return email

    def delete_email(self, email_id):
        Email.objects.filter(id=email_id).delete()
