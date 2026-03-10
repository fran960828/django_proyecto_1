from django.urls import path

from core.views import AboutUsView, ContactCreateView, HomeView, login_view, register_view,logout_view

app_name='core'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about_us/',AboutUsView.as_view(),name='about_us'),
    path('contact/',ContactCreateView.as_view(),name='contact'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout')
]

