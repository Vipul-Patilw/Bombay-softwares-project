from django.contrib import admin
from django.urls import path,include
from BombaySoftwares import  views
from BombaySoftwares.registration_view import usercreate
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from BombaySoftwares.usersdetail_view import usersdetail
urlpatterns = [

path('bio-data',TemplateView.as_view(template_name="Devloper Resume - M.html"),name="bio-data"),
	path('accounts/', include('django.contrib.auth.urls')),
#	path('userdetail',usersdetail.userdetail,name="data"),
	path("search",views.search,name="search"),
	path('social-create/<email>/<first_name>',views.storesocialacccount,name="social-create"),
	path('after-change-password',views.logout_after_change_password,name='logout-after-change-pass'),
	path('logout-page',TemplateView.as_view(template_name="registration/logout.html"),name="logout-page"),
	  path('password_change',views.ChangePassword.as_view(),name="password"),
	  path("searchdetails",TemplateView.as_view(template_name="searchdetail.html"),name="searchdetail"),
	path('personal_details',views.updateProfile,name='personal_detail'),
	path('',views.updateProfile,name='home'),
#	path('superuser/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('user/create',usercreate.UserCreate.as_view(),name='registration'), 
  
     path('about',TemplateView.as_view( template_name="about.html"),name='about'),
 path('privacy-policy',TemplateView.as_view( template_name="privacy-policy.html"),name='privacy-policy'),

    path('user/account-update/<pk>',views.UserAccountUpdate.as_view(),name='useraccountupdate'),
     path('user/account-delete/<pk>',views.UserAccountDelete.as_view(),name='useraccountdelete'),

    path('userdetail',views.UsersDetail.as_view(),name='userdetail'),

   ]


   