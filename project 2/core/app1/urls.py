from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('111/', views.var1),
    path('222/', views.var2),
    path('333/',views.var3),
    path('444/',views.var4),
    path('555/',views.var5),
    
    
]
