from django.urls import path
from . import views
#1 from .views import qualified_models

urlpatterns =[
    # path ('nomodels/', disqualified_models, name='nomodels'),
    # path ('models/', qualified_models, name='model'),
    path('', views.becomeamodel, name='becomeamodel'),
]
