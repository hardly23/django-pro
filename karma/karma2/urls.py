from django.conf.urls import url
from . import views


app_name = 'karma2'



urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'other/$',views.other,name='other'),
    url(r'register/$',views.register,name='register'),
    url(r'user_login/$',views.user_login,name='login'),
]