from django.db.models.expressions import OrderBy
from django.shortcuts import render
from .models import Donvi, QLTB, Tenmien
from matplotlib import pyplot

# Create your views here.
def index(request):
    # data = Donvi.objects.filter(active=True).order_by().values()
    # for 
    tenmien = Tenmien.objects.all().values_list('MAC_TB')
    lst = set(*tenmien)
    for item in lst:
        print(item[0])
    
    context = {
        'tenmien':tenmien
    }
    return render(request, 'firstapp/dashboard.html', context)
    