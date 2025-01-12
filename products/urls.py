"""
URL configuration for itapps project.

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
from django.urls import path, include
from django.conf import settings
import products.views as product_views





urlpatterns = [

    path('productMain/', product_views.productMain, name="product" ),
    path('productdetail/<int:pk>', product_views.product_detail, name="product_detail" ),
    path('productdetail/<int:product_id>/add_review/', product_views.add_review, name="add_review" ),
] 

