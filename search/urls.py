from django.urls import path

from . import views


urlpatterns = [
        path('', views.search, name='product'),
        path('detail/<int:product_id>/', views.detail, name='detail'),
        path('favorite/<int:product_id>/', views.fav, name='favorite'),
        path('favorite-delete/<int:product_id>/', views.fav_delete, name='delete'),
        path('my-foods/', views.my_food, name='my-food'),
        path('account/', views.account, name='account'),
        path('legal/', views.legal_notice, name='legal'),
        path('login/', views.login_page, name='logint'),
        path('connect/', views.post, name='connect'),
        path('singup/', views.singup, name='singup'),

]
