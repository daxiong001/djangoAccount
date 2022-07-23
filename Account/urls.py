"""Account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from accountmanage.views import views, admin, account


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('account/list/', views.accountList),
    path('account/add/', views.accountAdd),
    path('account/<int:nid>/edit/', views.accountEdit),
    path('account/delete/', views.accountDelete),

    # 管理员
    path('admin/list/', admin.adminList),
    path('admin/add/', admin.adminAdd),
    path('admin/<int:nid>/edit/', admin.adminEdit),
    path('admin/delete/', admin.adminDelete),
    path('admin/reset/', admin.adminReset),
    
    # 登陆
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image)


]
