from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updateItem/<str:pk>/', views.updateItem, name="updateItem"),
    path('deleteItem/<str:pk>/', views.deleteItem, name="deleteItem"),
    path('viewUsers/', views.viewUsers, name="viewUsers"),
    path('createList/', views.createList, name="createList"),
    path('viewLists/', views.viewLists, name="viewLists"),
    path('viewItems/<int:id>', views.viewItems, name="viewItems"),
    path('admin', views.admin, name="admin"),
]