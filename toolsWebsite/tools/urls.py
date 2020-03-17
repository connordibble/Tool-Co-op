from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('checked_out', views.checkedOut, name='checkedOut'),
    path('create_category', views.create_category, name='create_category'),
    path('create', views.create, name='create'),
    path('init', views.init, name='init'),
    path('nuke', views.nuke_it, name='nuke_it'),
    path('available', views.availableTools, name='available'),
    path('project', views.project, name='project'),
]
