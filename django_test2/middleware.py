class SimpleMiddleware(object):
    def _init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response

        return response


###
###class BlockedIpMiddleware(object):
###    def process_request(self, request):
###            http.HttpResponseForbidden('<h1>sdfsdf</h1>')
