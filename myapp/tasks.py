from celery import task
from rest_framework.exceptions import ValidationError
import logging
logger = logging.getLogger("main")
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


@task()
def celery_send_email(**kwargs):
	recipient_list = kwargs['recipient_list']
	html_message = kwargs['html_message']
	try:
		send_mail("Test mail", "Test Welcome", settings.EMAIL_HOST_USER, recipient_list,
			html_message=html_message)
	except Exception as e:
		return 'Email Not Sent'
	return 'Email Sent'