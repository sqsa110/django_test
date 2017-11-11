# from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.utils import deprecation

class M1(deprecation.MiddlewareMixin):
    def process_request(self, request):
        print('M1.process_req')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m1.process_view')

    def process_exception(self, request, exception):
        print('m1.process_exception')

    def process_response(self, request, response):
        print('M1.process_response')
        return response

    def process_template_response(self, request, response):
        print('template')

class M2(deprecation.MiddlewareMixin):
    def process_request(self, request):
        print("m2.process_request")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("m2.process_view")

    def process_exception(self, request, exceptioin):
        print("m2.process_exception")

    def process_response(self, request, response):
        print("m2.process_response")
        return response


