from django.urls import path
from index import views
from . import views

urlpatterns = [
    path('<int:pk>/', views.index_detail, name='index_detail'),
    path('', views.list_of_index, name='list_of_index'),
]