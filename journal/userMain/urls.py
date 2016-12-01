from django.conf.urls import url
from . import views




app_name = 'userMain'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^$', views.Create_user_main.as_view(), name='add')
    ]