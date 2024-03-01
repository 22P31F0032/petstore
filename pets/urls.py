from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
     path('about/',views.about,name='about'),
     path('angelfish/',views.angelfish,name='angelfish'),
    path('angora/',views.angora,name='angora'),
    path('bobtail/',views.bobtail,name='bobtail'),
     path('booknow/',views.booknow,name='booknow'),
     path('cocktail/',views.cocktail,name='cocktail'),
      path('contact/',views.contact,name='contact'),
      path('german/',views.german,name='german'),
       path('golden/',views.golden,name='golden'),
     path('goldfish/',views.goldfish,name='goldfish'),
       path('greyparrot/',views.greyparrot,name='greyparrot'),
     path('himalayan/',views.himalayan,name='himalayan'),
     path('husky/',views.husky,name='husky'),
    path('index/',views.index,name='index'),
     path('login/',views.login,name='login'),
    path('polish/',views.polish,name='polish'),
      path('registration/',views.registration,name='registration'),
      path('orders/',views.orders,name='orders'),
            path('show_orders/',views.show_orders,name='show_orders'),

]