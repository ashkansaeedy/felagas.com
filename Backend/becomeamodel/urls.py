from django.urls import path
from . import views
# from .views import qualified_models

urlpatterns =[
    # path ('nomodels/', views.becomeamodel.disqualified_models, name='nomodels'),
    # path ('models/', views.becomeamodel.qualified_models, name='model'),
    path('', views.becomeamodel, name='becomeamodel'),
]
