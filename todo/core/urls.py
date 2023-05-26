
from .views import *
from django.urls import re_path, include,path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
# from core.view import api_root
#api/product/
urlpatterns =  format_suffix_patterns(  [
   # path('', api_root),

   # User
    path('v1/user-list/', UserList.as_view(), name='user-list'),
    path('v1/user-details/', UserDetails.as_view(), name='user-details'),

     # Task
    path('v1/task-list/<int:id>/', TaskList.as_view(), name='task-list'),
    path('v1/task-detail/<int:id>/<int:task>/', TaskDetails.as_view(), name='task-details'),
   


    
])