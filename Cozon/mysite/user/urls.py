from django.urls import path
from .import views
urlpatterns=[

    path('index/',views.index,name='index'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('logoout/', views.logoout, name='logoout'),
    path('search/', views.search, name='search'),
    path('detail/', views.detail, name='detail'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('pay/', views.pay, name='pay'),
    path('deleo/', views.deleo, name='deleo'),
    path('succe/', views.succe, name='succe'),
    path('comment/', views.comment, name='comment'),
    path('con/', views.con, name='con'),
    path('selled/', views.selled, name='selled'),


]