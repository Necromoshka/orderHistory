from django.conf.urls import url
from . import views
from .forms import userMainView, userMainCreate

urlpatterns = [
        url(r'^(?:\?page=(?P<page>\d+))?$', views.index, name='index'),
       # url(r'^(?:\?page=(?P<page>\d+))?$', userMainView.as_view(), name='index'),
       # url(r'add/$', userMainCreate.as_view(), name='user_create'),
    ]