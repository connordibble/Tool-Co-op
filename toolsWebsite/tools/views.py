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


def availableTools(request):
    tools_list = ToolCategory.objects.all()
    list = []
    for tool in tools_list:
        if tool.available > 0:
            list.append(tool)
    context = {"available_tools": list}
    return render(request, 'tools/available.html', context)


def init(request):
    nuke(request)
    categories = {
        'hammer': 'https://www.montessoriservices.com/media/catalog/product/cache/1/thumbnail/550x/9df78eab33525d08d6e5fb8d27136e95/v/5/v508_hammer.jpg'}
    # for i in range(4):
    tool = ToolCategory(type='hammer',
                        available=randint(1, 10),
                        unavailable=randint(0, 10),
                        price=randint(5, 10),
                        tool_image=categories.get('hammer'))
    tool.save()

    return redirect('index')


def nuke(request):
    for categories in ToolCategory.objects.all():
        categories.delete()
