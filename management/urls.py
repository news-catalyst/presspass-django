from django.conf.urls import url
from django.urls import path
from management import views
from .auth import LoginView

app_name = 'management'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    path("presspass_login/", LoginView.as_view(), name="presspass_login"),

]
