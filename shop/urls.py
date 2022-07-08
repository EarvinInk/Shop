from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.allProductCategories, name='allproducts'),
    path('<slug:c_slug>/', views.allProductCategories, name='productsbycat'),
    path('<slug:c_slug>/<slug:p_slug>', views.productDetails,name='productdetails' )

]
