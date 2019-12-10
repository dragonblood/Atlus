from django import forms

class PredictForm(forms.Form):
	firstname = forms.CharField(max_length=15)
	info = forms.CharField(widget=forms.Textarea)

	def __str__(self):
		return self.info
		