from rest_framework.views import APIView
from email_app.Managers.EmailManager import EmailManager
from django.http import JsonResponse


class EmailView(APIView):
    def __init__(self):
        self.mgr = EmailManager()

    def get(self, request):
        page = int(request.GET.get('page', 1))
        res = self.mgr.get_all_emails(page)
        return JsonResponse(res)

    def post(self, request):
        data = request.data
        self.mgr.send_email(data)
        return JsonResponse({"message": "Email Sent"})


class EmailDetailView(APIView):
    def __init__(self):
        self.mgr = EmailManager()

    def get(self, request):
        email_id = request.GET.get('email_id')
        print(email_id)
        res = self.mgr.get_email_details(email_id)
        return JsonResponse(res)
