from django.conf.urls import url

from . import views

urlpatterns = [
   
    
    url(r'^apartment/$',views.apartmentView,name='apartmentView'),
    url(r'^apartment/(?P<ad_id>[0-9]+)/$', views.ap_detail, name='ap_detail'),

    url(r'^hostel/$',views.hostelView,name='hostelView'),
    url(r'^hostel/(?P<ad_id>[0-9]+)/$', views.hostel_detail, name='hostel_detail'),

    url(r'^sublet/$',views.subletView,name='subletView'),
    url(r'^sublet/(?P<ad_id>[0-9]+)/$', views.sublet_detail, name='sublet_detail'),

    url(r'^convention-centre/$',views.conventionView,name='conventionView'),
    url(r'^convention-centre/(?P<ad_id>[0-9]+)/$', views.convention_detail, name='convention_detail'),

    url(r'^garage/$',views.garageView,name='garageView'),
    url(r'^garage/(?P<ad_id>[0-9]+)/$', views.garage_detail, name='garage_detail'),

    url(r'^office-space/$',views.officeView,name='officeView'),
    url(r'^office-space/(?P<ad_id>[0-9]+)/$', views.office_detail, name='office_detail'),

   ]

