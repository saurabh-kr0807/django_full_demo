from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customers_details'),
    path('customers/new/', views.CreateCustomerView.as_view(), name='new_customer'),
]
