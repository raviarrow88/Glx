from django.urls import path
from .views import index,post_list
urlpatterns=[
path('',index,name='post_home'),
path('<int:id>/',post_list,name='post_list')
]
