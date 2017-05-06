from API.settings import RESULT_URL


class URL_WORKER(object):

    def __init__(self, fields=None, method=None):
        self.url = RESULT_URL
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
