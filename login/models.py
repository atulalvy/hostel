from email.message import EmailMessage

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

import smtplib, ssl
from random import choice


# creates SMTP session
def send_email(message, reciver):
    emails = ["cusathostel@gmail.com", "cusatuniversityhostel@gmail.com", "cusatuniversityhostels@gmail.com"]
    # context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = choice(emails)
    # start TLS for security
    # s.starttls()
    # Authentication
    s.login(email, "hostelmanagement@cusat")
    msg = EmailMessage()
    msg['Subject'] = 'Login OTP'
    msg['From'] = email
    msg['To'] = reciver
    msg.set_content(message)
    # message to be sent
    print(message)
    # sending the mail
    s.send_message(msg)

    # terminating the session
    s.quit()


class VerifiedUser(AbstractUser):
    userhash = models.TextField(max_length=512, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    Department_portal = models.TextField(max_length=255, blank=True, default='student')
    Accessible = models.TextField(max_length=512, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = self.username

    def set_hash(self):
        hash_user = make_password(self.username)
        self.userhash = hash_user[34:]
        self.save()
        msg = "your  verification otp    " + settings.CURRENT_DOMAIN_NAME_MAIN + 'auth/otp' + self.userhash
        send_email(msg, self.username)
        return self.userhash

    def reset_hash(self):
        hash_user = make_password(self.username)
        self.userhash = hash_user[34:]
        self.save()
        msg = "your password reset otp    " + settings.CURRENT_DOMAIN_NAME_MAIN + 'auth/reset' + self.userhash
        send_email(msg, self.username)
        return self.userhash


class ApplicationSettings(models.Model):
    active_applications = models.BooleanField(default=False)
    first_years = models.BooleanField(default=True)
    senior_or_first_year = models.BooleanField(default=True)
    show_allotment = models.BooleanField(default=False)