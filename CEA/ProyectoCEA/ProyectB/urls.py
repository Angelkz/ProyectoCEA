from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *


urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^index/$', home, name='home'),
    url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
]