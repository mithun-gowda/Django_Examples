from django.urls import path

from . import views as s1

app_name='app2'

urlpatterns=[
    
    path('sample1/',s1.sample1,name='sample1'),
    path('sample/',s1.sample,name='sample'),
] 