from django.urls import path
from Login_App.views import login,signup,authentication,validate,logout,admincheck,adminlogin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from django.contrib.auth import password_reset
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    url(r'^login',login),
    url(r'^signup',signup),
    url(r'^authentication/$',authentication),
    url(r'^validate/$',validate),
    url(r'^logout/$',logout),
    url(r'^adminlogin/$',adminlogin),
    url(r'^admincheck/$',admincheck),
    path('password_reset/',PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
	path('password_reset/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
	path('password_reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
	path('password_reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
]