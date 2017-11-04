
from django.conf.urls import url,include 
from django.contrib import admin
from django.conf.urls.static import static
from Rental import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^rental/',include('Rental.urls')),
    url(r'^post-ad/',include('postAd.urls')),
    url(r'^search/',include('search.urls')),
    

    # url(r'^apartment/', include('Rental.urls') ),
    # url(r'^apartment/', include('Rental.urls') ),
    
    
   
]
    
