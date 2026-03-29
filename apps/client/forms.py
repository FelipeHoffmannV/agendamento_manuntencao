from django import forms
from .models import Client, EnderecoClient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.forms import AuthenticationForm

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
        fields = ['username', 'tel_client', 'email_client', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Sua senha'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-md-6'), 
                Column('email_client', css_class='col-md-4'),
            ),
            Row(
                Column('tel_client', css_class='col-md-4'),
                Column('password', css_class='col-md-4'),
            )
        )
    
    def save(self, commit=True):
        client = super().save(commit=False)
        client.set_password(self.cleaned_data['password'])
        if commit:
            client.save()
        return client


class LoginForm(AuthenticationForm): # Usar AuthenticationForm facilita muito
    username = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={'placeholder': 'Seu usuário'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Entrar', css_class='btn btn-primary w-20'),
        )
