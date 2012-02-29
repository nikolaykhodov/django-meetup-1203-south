# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic.base import View

class Index(View):

    def get(self, request):
        return HttpResponse('Hello world!')
