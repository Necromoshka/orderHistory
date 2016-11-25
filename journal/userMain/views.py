from django.shortcuts import render
#from django.http import Http404
#from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator, InvalidPage
from .models import userMainTeble




def index(request, page):
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
    context = {"pg": pg, "p": page}
    return render(request,'userMain/index.html', context)