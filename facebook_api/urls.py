from django.conf.urls import url, include

from django.contrib.auth import views as auth_views

from views import test
from views import home
from views import main
from views import register


urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^home$', home, name='home'),
    url(r'^register$', register, name='register'),
    url(r'^test$', test, name='test'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
