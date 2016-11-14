from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponseRedirect
#from django.template import loader

from django.utils import timezone
#from django.urls import reverse
from django.core.urlresolvers import reverse
from .models import Menu, CustRecord
def index(request):
    '''index view'''
    list_of_pie = Menu.objects.all()
    context = {
        'list_of_pie': list_of_pie,
    }
    return render(request, 'choose/index.html', context)

def submit(request):
    '''submit view, the view after submission'''
    cust = CustRecord(name=request.POST["name"],table_id = request.POST["table_num"])
    cust.save()
    menu = Menu.objects.all()
    for dish in menu:
        quant = int(request.POST['dish' + str(dish.id)])
        if quant != 0:
            cust.cust_order.create(dish_id=dish, quantity = quant)
    cust.save()
    return HttpResponseRedirect(reverse('result', args=(cust.id,)))

def result(request, cust_id):
    '''result view, redirect from submit view, show result'''
    cust = get_object_or_404(CustRecord, pk=cust_id)
    return render(request, 'choose/result.html', {'cust': cust})

def detail(request):
    print ("aa")
    if request.method == "POST":
        dish_id = request.POST['dish_id']
        dish = get_object_or_404(Menu, id = dish_id)
        context = {
            'dish':dish,
        }
        return render(request,'choose/detail.html',context)
    else:
        raise Http404("")

