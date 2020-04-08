from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('all_tools', views.allTools, name="all_tools"),
    path('contact', views.contact, name='contact'),
    path('email', views.email, name='email'),
    path('checked_out', views.checkedOut, name='checkedOut'),
    path('toolpage/<int:tool_id>', views.toolpage, name='toolpage'),
    path('delete_tool/<int:tool_id>', views.delete_tool, name='delete_tool'),
    path('edit_tool/<int:tool_id>', views.edit_tool, name='edit_tool'),
    path('create_category', views.create_category, name='create_category'),
    path('overdue', views.overdue, name='overdue'),
    path('history', views.history, name='history'),
    path('create', views.create, name='create'),
    path('init', views.init, name='init'),
    path('nuke', views.nuke_it, name='nuke_it'),
    path('available', views.availableTools, name='available'),
    path('project', views.project, name='project'),
    path('checkout', views.checkout, name='checkout'),
    path('checkout_confirmed', views.checkout_confirmed, name='checkout_confirmed'),
    path('checkout_confirmation', views.checkout_confirmation, name='checkout_confirmation'),
    path('addToCart/<int:category_id>/', views.addToCart, name='addToCart'),
    path('checkin/<int:tool_id>', views.checkin, name='checkin'),
]
