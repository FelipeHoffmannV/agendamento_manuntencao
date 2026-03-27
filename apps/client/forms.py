from django import forms
from .models import Client, EnderecoClient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.hashers import make_password


# form cadastro
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = EnderecoClient
        fields = ['cep', 'rua', 'numero', 'cidade', 'bairro']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        self.helper.layout = Layout(
            Row(
                Column('cep', css_class='col-md-4'),
                Column('cidade', css_class='col-md-8'),
            ),
            Row(
                Column('rua', css_class='col-md-8'),
                Column('numero', css_class='col-md-4'),
            ),
            'bairro'
        )

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name_client', 'tel_client', 'email_client', 'password']
        exclude = ['id_client', 'endereco']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Sua senha'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('name_client', css_class='col-md-4'),
                Column('tel_client', css_class='col-md-4'),
                Column('email_client', css_class='col-md-4'),
                Column('password', css_class='col-md-4'),
            )
        )
    
    def save(self, commit=True):
        client = super().save(commit=False)
        client.password = make_password(self.cleaned_data['password'])
        if commit:
            client.save()
        return client


#form login
