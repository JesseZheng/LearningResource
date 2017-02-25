from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^email/subscribe/$', subscribe_email),
    url(r'^sms/subscribe/$', subscribe_sms),
]
