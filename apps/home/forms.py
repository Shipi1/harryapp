from django import forms

class emocionesForm(forms.Form):
    #emocion = forms.
    descripcion = forms.CharField(label='descripcion', max_length=220, widget= forms.TextInput(attrs={'class':'form-control','id':'descripcion'}))