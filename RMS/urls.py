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
from restaurant.views import category_list,category_create,category_update,category_delete,menu_list,menu_create,menu_update,menu_delete,table_list,table_create,table_update,table_delete,waiter_list,waiter_create,waiter_update,waiter_delete,order_list,order_create,order_update,order_delete,reception_list,reception_create,reception_update,reception_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    
      
    
    # Category URLs
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/update/<int:pk>/', category_update, name='category_update'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),

    # Menu URLs
    path('menus/', menu_list, name='menu_list'),
    path('menus/create/', menu_create, name='menu_create'),
    path('menus/update/<int:pk>/', menu_update, name='menu_update'),
    path('menus/delete/<int:pk>/', menu_delete, name='menu_delete'),

    # Table URLs
    path('tables/', table_list, name='table_list'),
    path('tables/create/', table_create, name='table_create'),
    path('tables/update/<int:pk>/', table_update, name='table_update'),
    path('tables/delete/<int:pk>/', table_delete, name='table_delete'),

    # Waiter URLs
    path('waiters/', waiter_list, name='waiter_list'),
    path('waiters/create/', waiter_create, name='waiter_create'),
    path('waiters/update/<int:pk>/', waiter_update, name='waiter_update'),
    path('waiters/delete/<int:pk>/', waiter_delete, name='waiter_delete'),

    # Order URLs
    path('orders/', order_list, name='order_list'),
    path('orders/create/', order_create, name='order_create'),
    path('orders/update/<int:pk>/', order_update, name='order_update'),
    path('orders/delete/<int:pk>/', order_delete, name='order_delete'),

    # Reception URLs
    path('receptions/', reception_list, name='reception_list'),
    path('receptions/create/', reception_create, name='reception_create'),
    path('receptions/update/<int:pk>/', reception_update, name='reception_update'),
    path('receptions/delete/<int:pk>/', reception_delete, name='reception_delete'),
]
    

