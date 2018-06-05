from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.shortcuts import render

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class Query(View):
    def get(self, request):
        return