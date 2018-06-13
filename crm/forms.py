from django import forms

class QueryForm(forms.Form):
    query_id = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
