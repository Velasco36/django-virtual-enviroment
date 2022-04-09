from importlib.resources import path
from django.urls import path
from toys import views 
 
urlpatterns = [ 
    path(r'toys/', views.toy_list), 
    path(r'toys/(?P<pk>[0-9]+)$', views.toy_detail), 
] 

