from django.conf.urls import url, include
from .views import *

urlpatterns=[
    url('^register/$', Register.as_view()),
]
