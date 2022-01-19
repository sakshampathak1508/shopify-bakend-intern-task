from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('list',views.view_prod),
    path('add',views.add_prod),
    path('delete/<int:id>',views.delete_prod),
    path('edit/<int:id>',views.edit_prod),
    path('export',views.export),
]