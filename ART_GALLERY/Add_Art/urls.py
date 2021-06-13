from django.urls import path
from Add_Art.views import addart,add,logout,viewall,delete_art
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^addart/$',addart),
    url(r'^add/$',add),
    url(r'^viewall/$',viewall),
    url(r'logout/$',logout),
    url(r'delete_art/$',delete_art),
]
