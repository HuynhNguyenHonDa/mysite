from django.db.models.expressions import OrderBy
from django.shortcuts import render
from .models import Donvi, QLTB, Tenmien
from matplotlib import pyplot

# Create your views here.
def index(request):
    # data = Donvi.objects.filter(active=True).order_by().values()
    # for 
    tenmien = Tenmien.objects.all().va
    lst_tm = []
    for tm in tenmien:
        lst_tm.append(tm[str(tm.keys())])
    print(lst_tm)
    data = QLTB.objects.all()
    context = {
        'data':data
    }
    return render(request, 'firstapp/dashboard.html', context)
    