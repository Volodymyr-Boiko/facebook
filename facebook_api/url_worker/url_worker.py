import urllib
from json import loads

import requests

from API.settings import SOCIAL_AUTH_FACEBOOK_KEY
from API.settings import SOCIAL_AUTH_FACEBOOK_SECRET
from API.settings import EXISTING_ACCESS_TOKEN
from API.settings import RESULT_URL


class URL_WORKER(object):

    def __init__(self, fields=None, method=None):
        self._url = self._get_url()
        self._fields = fields
        self._method = method

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        self._fields = fields

    @property
    def method(self):
        return self.method

    @method.setter
    def method(self, method):
        self._method = method

    def get_result_url(self):
        return self._url_maker()

    def _url_maker(self):
        if self._fields:
            pass
        else:
            pass

    @property
    def url(self):
        # if not self._fields:
        #     return self._url
        return self._url

    def _get_url(self):
        access_token = self.fetch_app_access_token()
        if access_token:
            url = 'https://graph.facebook.com/v2.9/me?access_token={}' \
                  '&debug=all&format=json' \
                  '&method=get&pretty=0' \
                  '&suppress_http_code=1'.format(
                access_token
            )
            return url
        return None

    @staticmethod
    def fetch_app_access_token():
        # res = requests.get('https://graph.facebook.com/oauth/access_token?' \
        #                    'client_id={APP_ID}&' \
        #                    'client_secret={APP_SECRET}&' \
        #                    'grant_type=client_credentials'.format(
        #     APP_ID=SOCIAL_AUTH_FACEBOOK_KEY,
        #     APP_SECRET=SOCIAL_AUTH_FACEBOOK_SECRET
        # ))
        # result = loads(res.text)['access_token']
        result_url = 'https://graph.facebook.com/{APP_ID}/' \
                     'accounts?access_token={APP_ID}|{APP_SECRET}'.format(
            APP_ID=SOCIAL_AUTH_FACEBOOK_KEY,
            APP_SECRET=SOCIAL_AUTH_FACEBOOK_SECRET
        )
        response = requests.get(result_url)
        # return response.json()['data'][0]['access_token']
        return 'EAAB4y9SatmcBAPR1OnVGGbtflq7KwhNsNTjM9GZCLmOkdNwZA0bcf2l1spvQR4B2C7lpEvNJUHsgGXeotVhx4Kcp5hUlH2f3buoABRcHJpIlGAUo5qKnuZBdBaYuIWcAjGGIHvlTB6VgkMWZAvkvcfr8jNNeP5eZACmPIf6EvYv8fCQtAx2QJRTAd2eDBpRIZD'
