from django.db.models.expressions import OrderBy
from django.shortcuts import render
from .models import Donvi, QLTB, Tenmien
from matplotlib import pyplot

# Create your views here.
def index(request):
    data = D
    context = {
        'data':data
    }
    return render(request, 'firstapp/dashboard.html', context)
    