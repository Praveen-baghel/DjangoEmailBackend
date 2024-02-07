from django.urls import path
from email_app.Views.EmailView import *

urlpatterns = [
    path('email/detail/', EmailDetailView.as_view()),
    path('email/', EmailView.as_view()),
]
