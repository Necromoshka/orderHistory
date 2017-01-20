from django import forms
from django.forms import formset_factory



class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()



ArticleFormSet = formset_factory(ArticleForm)