from django.conf.urls import url, include

from .views import get_me


urlpatterns = [
    url(r'^get_me$', get_me, name='test'),
]