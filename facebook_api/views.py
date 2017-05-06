import requests

from django.http import JsonResponse

from .url_worker.url_worker import URL_WORKER
from .services.unicode_worker import convert_object


def get_me(request):
    url = URL_WORKER()
    result = requests.get(url.url).json()

    return JsonResponse(result)
