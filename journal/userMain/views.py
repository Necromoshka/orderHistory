from django.shortcuts import render
#from django.http import Http404
#from django.http import HttpResponse
# Create your views here.

from .models import userMainTeble
#from .forms import

def index(request):
    rows=userMainTeble.objects.order_by('id')
    context={'rows':rows}
    return render(request,'userMain/index.html', context)