from django.urls import path
from . import views
#1 from .views import qualified_models

urlpatterns =[
    #1 path ('qualified/',qualified_models),
    path('',views.becomeamodel, name='becomeamodel'),
]
