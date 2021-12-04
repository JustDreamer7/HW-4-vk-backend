import time

from celery import shared_task
# from django.core.mail import send_mail
from django.core.mail import EmailMessage

from application import local_settings
# from application import celery_app
from application.celery import app


@app.task()
def admin_informer():
    msg = EmailMessage('Alert. Database object was created',
                       'If you dont know about it, check you project.', local_settings.EMAIL_HOST_USER,
                       local_settings.ADMINS)
    msg.send()
