from django.conf.urls import url
from . import views
<<<<<<< HEAD
from .forms import userMainView, userMainCreate

=======
app_name = 'userMain'
>>>>>>> 504da92d89a862863506c88380ade7abd54a4ac0
urlpatterns = [
        url(r'^(?:\?page=(?P<page>\d+))?$', views.index, name='index'),
       # url(r'^(?:\?page=(?P<page>\d+))?$', userMainView.as_view(), name='index'),
       # url(r'add/$', userMainCreate.as_view(), name='user_create'),
    ]