from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.shortcuts import render
from .forms import QueryForm

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class Query(View):
    form_class = QueryForm
    initial = {'key': 'value'}
    template_name = 'query.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
