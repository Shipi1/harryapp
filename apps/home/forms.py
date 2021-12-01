from django import forms

class EmocionesForm(forms.Form):

    CHOICES = [('Triste','Triste'),('Templado','Templado'),('Feliz','Feliz'),('Enojado','Enojado')]

    emocion = forms.ChoiceField(label='¿Cómo te sientes hoy? :',choices=CHOICES, widget=forms.RadioSelect)
    descripcion = forms.CharField(label='Si quieres, puedes describir tus emociones aquí...', max_length=220, widget= forms.TextInput(attrs={'class':'form-control','id':'descripcion','autocomplete':"off",'placeholder':'...'}))