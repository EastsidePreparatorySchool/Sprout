from django.urls import path
from . import views

app_name = 'leaf'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.slider_submit, name='slider_submit'),
    path('results/<int:value>/', views.slider_result, name='slider_result'),
]