from django.shortcuts import redirect, render, get_object_or_404
from .models import Transacao
from .form import TransacaoForm


def home(request):
    return render(request, 'contas/home.html')

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)   

def nova_transacao(request): 
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)
    
def delete_view(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    transacao.delete()
    return redirect('url_listagem')

def update(request, pk):
    data = {}
    transacao = get_object_or_404(Transacao, pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

 
