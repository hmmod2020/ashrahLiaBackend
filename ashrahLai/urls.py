"""ashrahLai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_board import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.create_new_user),
    path('regester',views.create_new_user_backEnd,name='regester'),
    path('login',views.login,name='login'),
    path('login1',views.login_show,name='login1'),
    path('show',views.show_user,name='done1'),
    path('order',views.order_up_go,name='order1'),
    path('order_back',views.order_back,name='order2'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('homeapi',views.homeapi),
    path('order_backapi',views.order_backapi),
    path('showTokenapi',views.showToken),
    path('loginapi',views.loginapi),
    path('create_new_user_backEndapi',views.create_new_user_backEndapi),
    path('myinfo', views.show_my_info_api),
    path('search_api', views.search_api),
    path('updat_my_inf', views.updat_my_inf),

]
