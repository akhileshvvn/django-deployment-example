from django.urls import path,re_path
from django.conf.urls import url
from . import views

#TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    re_path(r'^index/', views.index, name=''),
    re_path(r'formindex/',views.form_name_view,name='form_name'),
    re_path(r'^relative/$',views.relative,name = 'relative'),
    re_path(r'^other/$',views.other,name='other'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login')
]