from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    contato = forms.EmailField(label='E-email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())