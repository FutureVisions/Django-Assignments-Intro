from django.urls import path
from . import views
urlpatterns = [
    path('', views.count),
    path('reset', views.reset),
]