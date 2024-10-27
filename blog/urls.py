from django.urls import path
from .views import home, showcase

urlpatterns = [
    path('', home, name='home'),
    path('showcase/', showcase, name='showcase'),
]
