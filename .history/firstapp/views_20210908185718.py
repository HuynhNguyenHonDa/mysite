from django.db.models.expressions import OrderBy
from django.shortcuts import render
from .models import Donvi, QLTB, Tenmien
from matplotlib import pyplot

# Create your views here.
def index(request):
    # data = Donvi.objects.filter(active=True).order_by().values()
    # for 
    tenmien = Tenmien.objects.all().values_list('MAC_TB')
    list_tenmien = [*tenmien]
    lst = []
    for item in list_tenmien:
        lst.append(item[0])
    
    qltb = QLTB.objects.filter(id__in=lst)
    print(qltb)
    for item in qltb:
        item.is_query_DNS = True

    qltb_have_    
    
    context = {
        'tenmien':tenmien
    }
    return render(request, 'firstapp/dashboard.html', context)
    