from django.conf.urls import url, include

from .views import test


urlpatterns = [
    url(r'^test$', test, name='test'),
]