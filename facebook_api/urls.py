from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from views import test
from views import main
from views import register


urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^register$', register, name='register'),
    url(r'^test$', test, name='test'),
]
