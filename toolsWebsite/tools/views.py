from random import randint
from django.shortcuts import render
from django.shortcuts import redirect

from .models import ToolCategory, DueDates
from datetime import date, datetime

def index(request):
    tools_list = ToolCategory.objects.all()

    context = {
        'tools_list': tools_list,

    }
    return render(request, 'tools/index.html', context)
    
def checkedOut(request):
    tools_list = ToolCategory.objects.all()
    list = []
    due = DueDates.objects.order_by('-date_due')
    for tool in tools_list:
        for d in due:
            if tool == d.toolCategory:
                list.append(d)
    context = { "checkedOut_tools" : list }
    return render(request, 'tools/checkedOut.html', context)
    
def availableTools(request):
    tools_list = ToolCategory.objects.all()
    list = []
    for tool in tools_list:
        if tool.available > 0:
            list.append(tool)
    context = { "available_tools" : list }
    return render(request, 'tools/available.html', context)


def init(request):
    nuke(request)
    categories = ['hammer', 'wrench', 'screwdriver', 'drill']
    for i in range(4):
        tool = ToolCategory(type=categories[i],
                            available=randint(1, 10),
                            unavailable=randint(0, 10),
                            price=randint(5,10))
        tool.save()
        for j in range(tool.unavailable):
            due = DueDates()
            due.toolCategory = tool
            due.date_bought = datetime(2019,10,8)
            due.date_due = date.today()
            due.buyer = "Tyler"
            due.save()

    return redirect('index')


def nuke(request):
    for categories in ToolCategory.objects.all():
        categories.delete()
