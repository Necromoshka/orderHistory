from django.shortcuts import render
#from django.http import Http404
#from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator, InvalidPage
from .models import userMainTeble
from django.views import generic
from django.forms import formset_factory

class Create_user_main(generic.CreateView):
    model = userMainTeble
    template_name = 'userMain/index.html'
   # template_name = 'userMain/index.html'
    fields = '__all__'

User_formset = formset_factory(Create_user_main, can_order=True, can_delete=True, extra=2)

def index(request):
    formset = User_formset()
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
    context = {"pg": pg, 'formset': formset}
    return render(request,'userMain/index.html', context)

