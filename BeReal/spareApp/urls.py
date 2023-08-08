from django.urls import path
#let us reuse the django login views
from django.contrib.auth import views as auth_views

#let us import views file from 'spareApp' Application
from spareApp import views
urlpatterns=[
    path ('',views.index,name='index'),
    path('home/',views.home,name='home'),
    


    path('home/<int:product_id>',views.product_detail,name='product_detail'),

    path('receipt/',views.receipt,name='receipt'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),

    #for sale
    path('all_sales/',views.all_sales,name='all_sales'),
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),
    #to add stock
    path('add_to_stock/<str:pk>',views.add_to_stock, name= 'add_to_stock'),
    
    #path to login
    path('login/',auth_views.LoginView.as_view (template_name='spare/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view (template_name='spare/index.html'),name='logout'),

]