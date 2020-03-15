from random import randint
from django.shortcuts import render
from django.shortcuts import redirect

from .models import ToolCategory, DueDates
from datetime import date, datetime
import os

def index(request):
    tools_list = ToolCategory.objects.all()

    context = {
        'tools_list': tools_list,

    }
    return render(request, 'tools/index.html', context)

  
def contact(request):
    return render(request, 'tools/contact.html')
    
def project(request):
    return render(request, 'tools/project.html')
    
    
def checkedOut(request):
    tools_list = ToolCategory.objects.all()
    list = []
    due = DueDates.objects.order_by('-date_due')
    for tool in tools_list:
        for d in due:
            if tool == d.toolCategory:
                list.append(d)
    context = { "checkedOut_tools" : list }
    return render(request, 'tools/checked_out.html', context)

  
def availableTools(request):
    tools_list = ToolCategory.objects.all()
    list = []
    for tool in tools_list:
        if tool.available > 0:
            list.append(tool)
    context = {"available_tools": list}
    return render(request, 'tools/available.html', context)

def create_category(request):
    return render(request, 'tools/create_category.html')
    
def create(request):
    t = ToolCategory()
    t.type = request.POST['name']
    t.available = request.POST['quantity']
    t.unavailable = 0
    t.price = request.POST['price']
    image = request.FILES['img']
    handle_uploaded_file(image)
    t.tool_image = 'https://www.dewalt.com/NA/product/images/3000x3000x96/DCD708B/DCD708B_1.jpg'
    print(t.tool_image.url)
    t.save()
    return redirect('index')
    
def handle_uploaded_file(f):
    with open(f"tools/static/images/{f}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
  
def init(request):
    nuke(request)
    categories = ['hammer','wrench','screwdriver','level','drill']
    images = {
        'hammer': 'https://www.montessoriservices.com/media/catalog/product/cache/1/thumbnail/550x'
                  '/9df78eab33525d08d6e5fb8d27136e95/v/5/v508_hammer.jpg',
        'wrench': 'https://shop.harborfreight.com/media/catalog/product/cache/1/image'
                  '/9df78eab33525d08d6e5fb8d27136e95/6/7/67150_W3.jpg',
        'screwdriver': 'https://images-na.ssl-images-amazon.com/images/I/51kttYf5GFL._AC_SX569_.jpg',
        'level': 'https://shop.harborfreight.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95'
                 '/i/m/image_10922.jpg',
        'drill': 'https://www.dewalt.com/NA/product/images/3000x3000x96/DCD708B/DCD708B_1.jpg',

    }
    for i in range(len(categories)):
        tool = ToolCategory(type=categories[i],
                            available=randint(1, 10),
                            unavailable=randint(0, 10),
                            price=randint(5, 10),
                            tool_image=images.get(categories[i]))
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

def nuke_it(request):
    nuke(request)
    return redirect('index')
