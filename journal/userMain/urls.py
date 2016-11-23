from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^(?:\?page=(?P<page>\d+))?$', views.index, name='index'),
    ]