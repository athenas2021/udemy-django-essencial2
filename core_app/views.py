from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Nome: ',nome,'E-mail: ', email,'Assunto: ', assunto,'Mensagem: ', mensagem)

            messages.success(request, 'E-mail enviado.') 
            form = ContatoForm()   
        else:
            messages.error(request,'Algo deu errado.')
    context = {
        'form' : form
    }
    return render(request,'contato.html', context)

def produto(request):
    return render(request, 'produto.html')