"""
URL configuration for restaurant_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views impt Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from restaurant.views import RestaurantAPIView, EmployeeAPIView, MenuAPIView, GetResultOfCurrentDay

urlpatterns = [
    path('', include("restaurant.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/restaurantList', RestaurantAPIView.as_view()),
    path('api/v1/employeeList', EmployeeAPIView.as_view()),
    path('api/v1/employeeList/<int:pk>/', EmployeeAPIView.as_view()),
    path('api/v1/menuList', MenuAPIView.as_view()),
    path('api/v1/getResultOfCurrentDay/<int:pk>/', GetResultOfCurrentDay.as_view())
]
