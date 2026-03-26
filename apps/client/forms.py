from django import forms
from .models import Client, EnderecoClient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

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
        fields = ['name_client', 'tel_client', 'email_client']
        exclude = ['id_client', 'endereco']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('name_client', css_class='col-md-4'),
                Column('tel_client', css_class='col-md-4'),
                Column('email_client', css_class='col-md-4'),
            )
        )