from django import forms
from Rental.models import *
from django.contrib.admin import widgets  
from django.forms.fields import DateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RentalForm(forms.ModelForm):
	location = forms.ModelChoiceField(LocationModel.objects.all())
	rent = forms.IntegerField()
	advance = forms.IntegerField()
	contact = forms.CharField()
	details = forms.CharField()
	available_from = forms.DateField(widget=forms.widgets.SelectDateWidget)
	available_upto = forms.DateField(widget=forms.widgets.SelectDateWidget)
	

	class Meta :
		model = Rental
		exclude = ('posted_on',)

		
	


class ApartmentForm(RentalForm):	
	size = forms.IntegerField()
	parking_space = forms.BooleanField(required=False)
	no_of_bed = forms.IntegerField()
	no_of_bath = forms.IntegerField()
	floor_no = forms.IntegerField()
	lift = forms.BooleanField(required=False)
	cctv = forms.BooleanField(required=False)
	generator = forms.BooleanField(required=False)
	balcony = forms.BooleanField(required=False)
	service_charge = forms.IntegerField()
	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = Apartment
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(ApartmentForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = ApartmentForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.ApartmentForm(Submit('save', 'save'))




class HostelForm(RentalForm):
	no_of_roommate = forms.IntegerField(help_text="No of Roomamates")
	available_roommate = forms.IntegerField(help_text="Available No of Roomamates")
	rent_with_meal = forms.IntegerField(help_text="Rent With Meal")
	bed = forms.BooleanField(required=False, help_text="Bed")
	table = forms.BooleanField(required=False, help_text="Table")
	chair = forms.BooleanField(required=False, help_text="Chair")
	water_purifier = forms.BooleanField(required=False, help_text="Ehether Water Purifier is available or not")
	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = Hostel
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(HostelForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = HostelForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.HostelForm(Submit('save', 'save'))

	

class ConventionCentreForm(RentalForm):
	name = forms.CharField(help_text="Your conventtion-centre name")
	size_of_floor = forms.IntegerField(help_text="Size of Floor")
	no_of_floor = forms.IntegerField(help_text="Floor No.")
	human_capacity = forms.IntegerField(help_text="Human Capacity")
	catering_system = forms.BooleanField(required=False, help_text="Catering System")
	parking_space = forms.IntegerField(help_text="Parking Space(No of Cars)")
	open_space = forms.BooleanField(required=False, help_text="Open Space")
	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = ConventionCentre
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(ConventionCentreForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = ConventionCentreForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.ConventionCentreForm(Submit('save', 'save'))

class SubletForm(RentalForm):
	total_roommate = forms.IntegerField(help_text= "Total No. of Roomamates")
	available_roommate = forms.IntegerField(help_text="Available No. of Roomamates")
	family = forms.BooleanField(required=False,help_text="Family")
	bed = forms.BooleanField(required=False, help_text="Bed")
	table = forms.BooleanField(required=False,help_text="Table")
	chair = forms.BooleanField(required=False,help_text="Chair")
	water_purifier = forms.BooleanField(required=False,help_text="Water Purifier")
	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = Sublet
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(SubletForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = SubletForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.SubletForm(Submit('save', 'save'))

class GarageForm(RentalForm):

	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = Garage
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(GarageForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = GarageForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.GarageForm(Submit('save', 'save'))

class OfficeForm(RentalForm):
	size = forms.IntegerField(help_text="Size")

	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Save','Save',css_class='btn-primary'))

	class Meta:
		model = Office
		exclude = ()
		def __init__(self, *args, **kwargs):
				super(OfficeForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = OfficeForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.OfficeForm(Submit('save', 'save'))


	