from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/<int:p_id>', views.add_to_cart, name='add_to_cart'),
    path('detail/', views.cart_details, name='cart'),
    path('remove:<int:p_id>',views.remove_item,name='remove_item'),
    path('delete:<int:p_id>',views.delete_item,name='delete_item'),

]
