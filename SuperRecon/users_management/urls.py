from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name="home"),
        path("login/",views.login_view,name="login"),
        path("logout/",views.logout_view,name="logout"),
        path("register/",views.register,name="register"),
        path("process_login/",views.process_login,name="process_login"),
        path("process_logout/",views.process_logout,name="process_logout"),
] 
