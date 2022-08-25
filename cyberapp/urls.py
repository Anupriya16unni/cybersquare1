from django.urls import path
from .import views
urlpatterns=[
    path('',views.fnIndex,name='index/'),
    path('adhun/',views.adhun)
]