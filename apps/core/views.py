from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Dispositivo, Servico
from .forms import DispositivoForm, ServicoForm


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'core/agendamento.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['dispositivo_form'] = DispositivoForm(self.request.POST)
        else:
            context['dispositivo_form'] = DispositivoForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        dispositivo_form = context['dispositivo_form']

        if form.is_valid() and dispositivo_form.is_valid():
        # 1. Prepara o dispositivo, mas não salva ainda
            dispositivo_obj = dispositivo_form.save(commit=False)
        
        # 2. VINCULA O CLIENTE AO DISPOSITIVO
        if self.request.user.is_authenticated:
            dispositivo_obj.client = self.request.user
        
        # 3. Salva o dispositivo com o dono definido
            dispositivo_obj.save()
        
        # 4. Prepara o serviço e vincula ao dispositivo criado
            servico_obj = form.save(commit=False)
            servico_obj.dispositivo = dispositivo_obj
            servico_obj.save()
        
            return redirect(self.success_url)
    
        return self.render_to_response(self.get_context_data(form=form))


