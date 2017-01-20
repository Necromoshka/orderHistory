from django.shortcuts import render
#from django.http import Http404
#from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator, InvalidPage
from .models import userMainTeble
from django.views import generic
from django.forms import formset_factory
from .forms import ArticleFormSet
from django.http import HttpResponseRedirect
import datetime


formset = ArticleFormSet(initial=[{'title': 'Django is now open source', 'pub_date': datetime.date.today(),}])



class Create_user_main(generic.CreateView):
    model = userMainTeble
    template_name = 'userMain/usermaincreate.html'
    fields = '__all__'



def create(request):
    tytle = "Create"
    context = {'formset': formset,"tytle":tytle}
    return render(request, 'userMain/usermaincreate.html', context)






def index(request):
    tytle = "Main"
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1
    #rows = userMainTeble.objects.order_by('id')
    paginator = Paginator(userMainTeble.objects.all(), 10)
    try:
        pg = paginator.page(page_num)

    except InvalidPage:
        pg = paginator.page(1)
    context = {"pg": pg, "tytle":tytle}

    return render(request,'userMain/index.html', context)

