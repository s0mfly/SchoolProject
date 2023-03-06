from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from datetime import datetime
from . import forms, views


urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('login/',
         LoginView.as_view
             (
             template_name='main/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('regist/', views.regist, name='regist'),
    path('begin/', views.begin, name='begin'),
    path('begin2/', views.begin2, name='begin2'),
    path('begin3/', views.begin3, name='begin3'),
    path('begin4/', views.begin4, name='begin4'),
    path('zada4i_tems/', views.zada4i_tems, name='zada4i_tems'),
    path('zada4i/', views.zada4i, name='zada4i'),
    path('zada4i2/', views.zada4i2, name='zada4i2'),
    path('zada4i3/', views.zada4i3, name='zada4i3'),
    path('zada4i4/', views.zada4i4, name='zada4i4'),
    path('table/', views.table, name='table')
]
