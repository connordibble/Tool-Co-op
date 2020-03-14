from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('checked_out', views.checkedOut, name='checkedOut'),
    path('init', views.init, name='init'),
    path('available', views.availableTools, name='available'),
    path('project', views.project, name='project'),
]
