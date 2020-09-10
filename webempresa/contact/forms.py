from django import forms


class ContactForm(forms.Form):    # parecido al models, pero no igual:
    name = forms.CharField(label="Nombre",required=True, widget= forms.TextInput(
        attrs={'class':'form-control',  'placeholder':'Nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="EMail",required=True, widget= forms.EmailInput(
        attrs={'class':'form-control',  'placeholder':'eMail'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido",required=True, widget=forms.Textarea(  
         attrs={'class':'form-control', 'rows' : 3,  'placeholder':'Escriba aquí su comentario'}
    ), min_length=3, max_length=200)

# tipos de campos en https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes

     