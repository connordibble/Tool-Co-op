from random import randint
from django.shortcuts import render, redirect, get_object_or_404

from .models import ToolCategory, DueDates, ShoppingCart, History
from django.utils import timezone
import datetime
import os


def index(request):
    tools_list = ToolCategory.objects.all()
    cart = ShoppingCart.objects.all()

    context = {
        'tools_list': tools_list,
        'cart': cart,

    }
    return render(request, 'tools/index.html', context)


def contact(request):
    cart = ShoppingCart.objects.all()

    context = {
        'cart': cart,
    }
    return render(request, 'tools/contact.html', context)


def project(request):

    cart = ShoppingCart.objects.all()

    context = {
        'cart': cart,
    }

    return render(request, 'tools/project.html', context)
    
def history(request):
    cart = ShoppingCart.objects.all()
    history = History.objects.order_by('-date_bought')
    context = { "history" : history,
                "cart" : cart
                }
    return render(request, 'tools/history.html', context)
    
def toolpage(request, tool_id):
    cart = ShoppingCart.objects.all()
    tool_category = get_object_or_404(ToolCategory, pk=tool_id)
    context = {'tool' : tool_category, 'cart': cart}
    return render(request, 'tools/toolpage.html', context)

def delete_tool(request, tool_id):
    tool_category = get_object_or_404(ToolCategory, pk=tool_id)
    tool_category.delete()
    return redirect('index')

def edit_tool(request, tool_id):
    t = get_object_or_404(ToolCategory, pk=tool_id)
    t.type = request.POST['name']
    t.available = request.POST['quantity']
    t.price = request.POST['price']
    t.tool_image = request.POST['img']
    t.save()
    return redirect('index')
    
def checkedOut(request):
    cart = ShoppingCart.objects.all()
    tools_list = ToolCategory.objects.all()
    list = []
    due = DueDates.objects.order_by('-date_bought')
    for d in due:
        for tool in tools_list:
            if tool == d.toolCategory:
                list.append(d)
    context = {
            "checkedOut_tools": list,
            "cart": cart,
    }
    return render(request, 'tools/checked_out.html', context)


def availableTools(request):
    cart = ShoppingCart.objects.all()
    tools_list = ToolCategory.objects.all()
    list = []
    for tool in tools_list:
        if tool.available > 0:
            list.append(tool)
    context = {"available_tools": list, "cart": cart,}
    return render(request, 'tools/available.html', context)


def create_category(request):
    cart = ShoppingCart.objects.all()

    context = {
        'cart': cart,
    }
    return render(request, 'tools/create_category.html', context)


def overdue(request):
    cart = ShoppingCart.objects.all()
    due_dates = DueDates.objects.order_by('-date_due')
    list = []
    for tool in reversed(due_dates):
        if tool.date_due < timezone.now():
            list.append(tool)
    context = {"overdue_tools": list, "cart": cart}
    return render(request, 'tools/overdue.html', context)


def create(request):
    t = ToolCategory()
    t.type = request.POST['name']
    t.available = request.POST['quantity']
    t.unavailable = 0
    t.price = request.POST['price']
    t.tool_image = request.POST['img']
    t.save()
    return redirect('index')


def handle_uploaded_file(f):
    with open(f"tools/static/images/{f}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def checkout(request):
    cart = ShoppingCart.objects.all()

    context = {
        'cart': cart,
    }

    history = History()
    for cart in ShoppingCart.objects.all():
        due = DueDates()
        due.toolCategory = cart.toolCategory
        due.quantity = cart.quantity
        due.date_bought = datetime.datetime(2019, randint(1, 12), randint(1, 28))
        due.date_due = datetime.datetime(2020, randint(1, 12), randint(1, 28))
        # due.date_bought = datetime.datetime.now()
        # due.date_due = datetime.datetime.now()
        due.buyer = "Connor"
        due.save()
        
        history.customer = due.buyer
        history.date_bought = due.date_bought
        history.price += due.toolCategory.price
        history.tools += due.toolCategory.type + ", "
        
        cart.delete()
    
    history.tools = history.tools[:-2]
    history.save()
    return render(request, 'tools/checkout.html', context)


def addToCart(request, category_id):
    tool = get_object_or_404(ToolCategory, pk=category_id)
    tool.available -= 1
    tool.unavailable += 1
    tool.save()

    inCart = False
    for cart in ShoppingCart.objects.all():
        if cart.tool == tool.type:
            cart.quantity += 1
            cart.save()
            inCart = True

    if not inCart:
        cart = ShoppingCart()
        cart.toolCategory = tool
        cart.tool = tool.type
        cart.quantity = 1
        cart.save()

    return redirect('index')


def init(request):
    nuke(request)
    categories = ['hammer', 'wrench', 'screwdriver', 'level', 'drill']
    images = {
        'hammer': 'data:image/jpeg;base64,'
                  '/9j/4AAQSkZJRgABAQAAAQABAAD'
                  '/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys'
                  '/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N'
                  '//AABEIALoAugMBIgACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAABgcBBAMFCAL'
                  '/xAA4EAACAgECBAQDBwMDBQEAAAAAAQIDBAURBhIhMUFRYXETIoEjMkJicqHRBxSRQ7HBJDNjgvEV'
                  '/8QAGAEBAAMBAAAAAAAAAAAAAAAAAAEDBAL/xAAdEQEBAAMBAQADAAAAAAAAAAAAAQIDETEhEjJB'
                  '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',
        'wrench': 'https://shop.harborfreight.com/media/catalog/product/cache/1/image'
                  '/9df78eab33525d08d6e5fb8d27136e95/6/7/67150_W3.jpg',
        'screwdriver': 'https://images-na.ssl-images-amazon.com/images/I/51kttYf5GFL._AC_SX569_.jpg',
        'level': 'https://shop.harborfreight.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95'
                 '/i/m/image_10922.jpg',
        'drill': 'https://www.dewalt.com/NA/product/images/3000x3000x96/DCD708B/DCD708B_1.jpg',

    }

    prices = {'hammer': 2, 'wrench': 2, 'screwdriver': 2, 'level': 2, 'drill': 5}
    for i in range(len(categories)):
        tool = ToolCategory(type=categories[i],
                            available=10,
                            unavailable=randint(1, 5),
                            price=prices.get(categories[i]),
                            tool_image=images.get(categories[i]))
        tool.save()
        for j in range(tool.unavailable):
            due = DueDates()
            due.toolCategory = tool
            due.date_bought = datetime.datetime(2019, randint(1, 12), randint(1, 28))
            due.date_due = datetime.datetime(2020, randint(1, 12), randint(1, 28))
            due.buyer = "Tyler"
            due.save()

    return redirect('index')


def nuke(request):
    for categories in ToolCategory.objects.all():
        categories.delete()


def nuke_it(request):
    nuke(request)
    return redirect('index')
