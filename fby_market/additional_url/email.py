from django.urls import path
from django_email_verification.views import verify

from main.modules.user.email_confirmation import EmailConfirmation

urlpatterns = [
    path('<str:token>', verify),
    path('confirmation_resend/', EmailConfirmation.as_view(), name="email")
]