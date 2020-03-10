from random import randint
from django.shortcuts import render
from django.shortcuts import redirect

from .models import ToolCategory


def index(request):
    tools_list = ToolCategory.objects.all()

    context = {
        'tools_list': tools_list,

    }
    return render(request, 'tools/index.html', context)
    
def contact(request):
    return render(request, 'tools/contact.html')
    
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

    return redirect('index')


def nuke(request):
    for categories in ToolCategory.objects.all():
        categories.delete()
