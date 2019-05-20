from django import forms

class PetSearchForm(forms.Form):
    pet_name = forms.CharField(label="Pet name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter pet name'}))