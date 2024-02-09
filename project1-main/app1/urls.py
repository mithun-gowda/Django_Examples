from django.urls import path

from . import views as s2

app_name='app1'

urlpatterns=[
    path('register/',s2.register,name='register'),
    path('user/<pk>/',s2.user,name='user'),
    path('person/',s2.person,name='person'),
    path('student/',s2.student,name='student'),
]
