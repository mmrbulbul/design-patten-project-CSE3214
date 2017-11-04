from django.shortcuts import render
from .models import *
from search.forms import SearchForm
from django import forms



# Create your views here.
def index(request):
	return render(request,'rental/indextst.html',None)

########################apartment######################################## 
def apartmentView(request):
	ap_result = Apartment.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	form = SearchForm()
	return  render(request,'rental/apartment.html',dict)

def ap_detail(request, ad_id):
	ap_result = Apartment.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/ap_detail.html',dict)



###################################mess########################

def hostelView(request):
	ap_result = Hostel.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	return  render(request,'rental/hostel.html',dict)

def hostel_detail(request, ad_id):
	ap_result = Hostel.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/hostel_detail.html',dict)

####################################office#######################################
def officeView(request):
	ap_result = Office.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	return  render(request,'rental/office.html',dict)

def office_detail(request, ad_id):
	ap_result = Office.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/office_detail.html',dict)

##########################################sublet#########################################
def subletView(request):
	ap_result = Sublet.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	return  render(request,'rental/sublet.html',dict)

def sublet_detail(request, ad_id):
	ap_result = Sublet.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/sublet_detail.html',dict)

###############################convention-centre#######################################
def conventionView(request):
	ap_result = ConventionCentre.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	return  render(request,'rental/convention.html',dict)

def convention_detail(request, ad_id):
	ap_result = ConventionCentre.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/convention_detail.html',dict)
######################garage ####################################
def garageView(request):
	ap_result = Garage.objects.all().order_by('-posted_on')
	dict = {'ads':ap_result}
	return  render(request,'rental/garage.html',dict)

def garage_detail(request, ad_id):
	ap_result = Garage.objects.filter(id=ad_id)
	dict = {'ids':ap_result}
	return  render(request,'rental/garage_detail.html',dict)






