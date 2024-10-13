"""
URL configuration for RMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
     
    
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Menu URLs
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/create/', views.menu_create, name='menu_create'),
    path('menus/update/<int:pk>/', views.menu_update, name='menu_update'),
    path('menus/delete/<int:pk>/', views.menu_delete, name='menu_delete'),

    # Table URLs
    path('tables/', views.table_list, name='table_list'),
    path('tables/create/', views.table_create, name='table_create'),
    path('tables/update/<int:pk>/', views.table_update, name='table_update'),
    path('tables/delete/<int:pk>/', views.table_delete, name='table_delete'),

    # Waiter URLs
    path('waiters/', views.waiter_list, name='waiter_list'),
    path('waiters/create/', views.waiter_create, name='waiter_create'),
    path('waiters/update/<int:pk>/', views.waiter_update, name='waiter_update'),
    path('waiters/delete/<int:pk>/', views.waiter_delete, name='waiter_delete'),

    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),

    # Reception URLs
    path('receptions/', views.reception_list, name='reception_list'),
    path('receptions/create/', views.reception_create, name='reception_create'),
    path('receptions/update/<int:pk>/', views.reception_update, name='reception_update'),
    path('receptions/delete/<int:pk>/', views.reception_delete, name='reception_delete'),
]
    

