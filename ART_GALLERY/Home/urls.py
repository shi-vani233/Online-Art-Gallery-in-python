from django.urls import path
from Home.views import home,purchases_view,cart_view,search,cart,remove,new_purchase,profile
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$',home),
    url(r'^search/$',search),
    url(r'^purchases_view/$',purchases_view),
    url(r'^cart_view/$',cart_view),
    url(r'^cart/$',cart),
    url(r'^remove/$',remove),
    url(r'^new_purchase/$',new_purchase),
    url(r'^profile/$',profile),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)