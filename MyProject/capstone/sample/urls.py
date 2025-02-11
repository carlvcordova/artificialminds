from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
	path('index', views.IndexView.as_view(), name="index"),
	path('register', views.RegistrationView.as_view(), name="register"),
	path('login', views.LoginView.as_view(), name="login"),
	path('home', views.HomeView.as_view(), name="home"),
	path('about', views.AboutView.as_view(), name="about"),
	path('contact', views.ContactView.as_view(), name="contact"),
	path('setting', views.SettingView.as_view(), name="setting"),
	path('lgout', views.LogoutView.as_view(), name="logout"),
]