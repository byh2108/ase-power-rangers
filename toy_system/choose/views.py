from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect
import json
from django.http import JsonResponse
#from django.template import loader

from django.utils import timezone
#from django.urls import reverse
from django.core.urlresolvers import reverse
from .models import Menu, CustRecord, Review

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
    if request.method == "POST":
        dish_id = request.POST['dish_id']
        dish = get_object_or_404(Menu, id = dish_id)
        context = {
            'dish':dish,
        }
        return render(request,'choose/detail.html',context)
    else:
        raise Http404("")

def review(request):
    if request.method == "POST":
        dish_id = request.POST['dish_id']
        cust_id = request.POST['cust_id']
        context = request.POST['context']
        dish = get_object_or_404(Menu, id = dish_id)
        cust = get_object_or_404(CustRecord, id = cust_id)
        new_review = Review(cust_id = cust, dish_id = dish, context= context)
        new_review.save()
        context = {
            'success':1,
        }
        return JsonResponse(context)
    else:
        raise Http404("")
