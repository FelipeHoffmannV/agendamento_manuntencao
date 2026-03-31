from django import forms
from .models import Dispositivo, Servico
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Button

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nome_meu_dispositivo', 'tipo_dispositivo']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
                Row(
                    Column('nome_meu_dispositivo', css_class='col-md-4'),
                ),
                Row(
                    Column('tipo_dispositivo', css_class='col-md-4'),

                )
                

            )
    
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['tipo_servico', 'data_servico']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
                Row(Column('tipo_servico', css_class='col-md-4'),
                    Column('data_servico', css_class='col-md-8')),
                    Submit('submit', 'enviar', css_class='btn btn-primary')
            )
    