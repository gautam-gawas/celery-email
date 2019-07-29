from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import celery_send_email

class Notification(APIView):

	def post(self, request):
		"""
		Sending emails.
		"""
		#expecting email_html to be string if not we can use "render_to_string(email_html)"
		celery_send_email.apply_async(kwargs={"recipient_list":request.data['email_to'],
			"html_message":request.data['email_html']})
		return Response({"status":"In Progress"})
