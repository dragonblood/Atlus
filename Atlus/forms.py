from django import forms

class predictForm(forms.Form):
	firstname = forms.CharField(max_length=15)
	lastname=forms.CharField(max_length=15)
	info = forms.CharField(widget=forms.Textarea)#forms.TextField(null=False, blank=False)