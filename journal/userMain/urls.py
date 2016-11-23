from django.conf.urls import url
from . import views
app_name = 'userMain'
urlpatterns = [
        url(r'^(?:\?page=(?P<page>\d+))?$', views.index, name='index'),
    ]