from django.shortcuts import render
from .forms import *
from Rental.models import *

# Create your views here.

def search(request):
	if request.method == "POST" :
		form = SearchForm(request.POST)
		if form.is_valid():
			ap_result = get_result(form)
			# ap_result = Apartment.objects.all().order_by('-posted_on')
			dict = {'ads':ap_result}
			return  render(request,'rental/result.html',dict)
	else:
		form = SearchForm()
	return render(request, 'search.html', {'form': form})


def get_result(form):
	data = form.cleaned_data
	form_cat = str(data['category'])
	loc = data['location']
	st_rent = data['starting_rent']
	end_rent = data['ending_rent']

	if form_cat == "Apartment":
		ap_result = Apartment.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')
	elif form_cat == 'Hostel':
		ap_result = Hostel.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')
	elif form_cat == 'ConventionCentre':
		ap_result = ConventionCentre.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')
	elif form_cat == 'Sublet':
		ap_result = Sublet.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')
	elif form_cat == 'Garage':
		ap_result = Garage.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')
	elif form_cat == 'Office':
		ap_result = Office.objects.filter(location = loc, rent__gte = st_rent, rent__lte = end_rent).order_by('-posted_on')

	return ap_result