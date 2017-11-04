from django.shortcuts import render
from django.utils import timezone
from .forms import *

from Rental.models import *

# Create your views here.

def index(request):
	return render(request,'postAd/post-ads.html',None)

def ap_postView(request):
	if request.method == "POST" :
		form = ApartmentForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = Apartment.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/ap_detail.html',dict)
	else:
		form = ApartmentForm
	return render(request, 'postAd/add_ap.html', {'form': form})
#sublet

def sublet_postView(request):
	if request.method == "POST" :
		form = SubletForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = sublet.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/sublet_detail.html',dict)
	else:
		form = SubletForm()
	return render(request, 'postAd/add_sublet.html', {'form': form})
#office
def office_postView(request):
	if request.method == "POST" :
		form = OfficeForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = Office.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/office_detail.html',dict)
	else:
		form = OfficeForm()
	return render(request, 'postAd/add_office.html', {'form': form})

#convention

def convention_postView(request):
	if request.method == "POST" :
		form = ConventionCentreForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = ConventionCentre.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/convention_detail.html',dict)
	else:
		form = ConventionCentreForm()
	return render(request, 'postAd/add_convention.html', {'form': form})
#garage
def garage_postView(request):
	if request.method == "POST" :
		form = GarageForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = Garage.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/garage_detail.html',dict)
	else:
		form = GarageForm()
	return render(request, 'postAd/add_garage.html', {'form': form})
#hostel
def hostel_postView(request):
	if request.method == "POST" :
		form = HostelForm(request.POST)
		if form.is_valid():
			ad = form.save(commit=False)
			ad.posted_on = timezone.now()
			ad.save()
			print(ad.id)
			res = Hostel.objects.filter(id=ad.id)
			dict ={ 'ids':res}
			print(dict['ids'])
			return render(request, 'rental/hostel_detail.html',dict)
	else:
		form = HostelForm()
	return render(request, 'postAd/add_hostel.html', {'form': form})
