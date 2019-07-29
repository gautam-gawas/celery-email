from django.urls import path
from .views import Notification


urlpatterns = [
    path('send-email', Notification.as_view(), name="notify-user"),

]