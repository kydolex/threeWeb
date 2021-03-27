from django.urls import path
from threeWeb import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.List_View.as_view(), name='list'),
    path('plan/', views.Plan_View.as_view(), name='plan'),
    path('request/', views.request_View.as_view(), name='request'),
    path('contact/', views.contact_View.as_view(), name='contact'),
    path('request_next/', views.request_next, name='request_next'),
]
