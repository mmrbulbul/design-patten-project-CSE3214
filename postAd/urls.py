from django.conf.urls import url

from . import views

urlpatterns = [
   
    
    url(r'^$',views.index,name='index'),
    url(r'^apartment/',views.ap_postView,name='ap_postView'),
    url(r'^hostel/',views.hostel_postView,name='hostel_postView'),
    url(r'^sublet/',views.sublet_postView,name='sublet_postView'),
    url(r'^office/',views.office_postView,name='office_postView'),
    url(r'^convention-centre/',views.convention_postView,name='convention_postView'),
    url(r'^garage/',views.garage_postView,name='garage_postView'),
   
 

   ]

