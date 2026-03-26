from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Client, EnderecoClient
from .forms import ClientForm, EnderecoForm  # Importe o form de endereço também

# views.py
def index_(request):
    return render(request, 'client/home.html')

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/cadastro_cliente.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['endereco_form'] = EnderecoForm(self.request.POST)
        else:
            context['endereco_form'] = EnderecoForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        endereco_form = context['endereco_form']
        
        if form.is_valid() and endereco_form.is_valid():
            # 1. Salva o endereço primeiro
            endereco = endereco_form.save()
            
            # 2. Vincula ao cliente e salva
            cliente = form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            
            # 3. Importante: redireciona manualmente para garantir o sucesso
            from django.shortcuts import redirect
            return redirect(self.success_url)
        else:
            # Se cair aqui, imprima os erros no terminal para descobrir o motivo
            print("Erros no Cliente:", form.errors)
            print("Erros no Endereço:", endereco_form.errors)
            return self.render_to_response(self.get_context_data(form=form))
