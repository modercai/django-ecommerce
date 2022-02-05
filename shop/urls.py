from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/',
         views.category_list, name='category_list')
]