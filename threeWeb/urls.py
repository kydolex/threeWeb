from django.urls import path
from threeWeb import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
