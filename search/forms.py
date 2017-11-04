from django import forms
from Rental.models import *
from django.contrib.admin import widgets  
from django.forms.fields import DateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

CATEGORIES = (
    (1, "Apartment"),
    (2, "Hostel"),
    (3, "ConventionCentre"),
    (4, "Sublet"),
    (5, "Garage"),
    (6, "Office")
)

class SearchForm(forms.Form):
	category = forms.ModelChoiceField(CategoryModel.objects.all())
	location = forms.ModelChoiceField(LocationModel.objects.all())
	starting_rent = forms.IntegerField()
	ending_rent = forms.IntegerField()

	helper = FormHelper()
	helper.form_method ='POST'
	helper.add_input(Submit('Search','Search',css_class='btn-primary'))

	class Meta:
		def __init__(self, *args, **kwargs):
				super(SearchForm, self).__init__(*args, **kwargs)

				# If you pass FormHelper constructor a form instance
				# It builds a default layout with all its fields
				self.helper = SearchForm(self)

				# You can dynamically adjust your layout
				self.helper.layout.SearchForm(Submit('search', 'search'))