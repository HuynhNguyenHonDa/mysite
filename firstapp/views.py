from django.db.models.expressions import OrderBy
from django.shortcuts import render
from .models import Donvi, QLTB, Tenmien
from matplotlib import pyplot
from django.db.models import Count

# Create your views here.
def index(request):
    # data = Donvi.objects.filter(active=True).order_by().values()
    # for 
    qltb1 = QLTB.objects.annotate(number_of_answers=Count('tenmien'))#đếm số lượng tên miền của 1 trang bị
    tenmien = Tenmien.objects.all().values_list('MAC_TB')#
    list_tenmien = [*tenmien]
    lst = []
    for item in list_tenmien:
        lst.append(item[0])
    
    qltb = QLTB.objects.filter(id__in=lst)

    context = {
        'qltb': qltb,
        'qltb1': qltb1
    }
    return render(request, 'firstapp/dashboard.html', context)
    