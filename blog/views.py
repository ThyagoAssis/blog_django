from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

#Cptura de sessoes
from django.views import View
from django.shortcuts import render, redirect
#from django.http import HttpResponse


class BlogListView(ListView):
    model = Blog

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('blog_section')  # Redireciona para a página de login se a sessão não estiver ativa
        
        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

class BlogCreateView(CreateView):
    model = Blog
        
    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('blog_section')  # Redireciona para a página de login se a sessão não estiver ativa
        
        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)
    
    fields = ["titulo", "conteudo"]
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = Blog

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('blog_section')  # Redireciona para a página de login se a sessão não estiver ativa
        
        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

    fields = ["titulo", "conteudo"]
    success_url = reverse_lazy('blog_list')
    

class BlogDeleteView(DeleteView):
    model = Blog

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('blog_section')  # Redireciona para a página de login se a sessão não estiver ativa
        
        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)
        
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')


##Capturando sessões
class SolicitarDadosView(View):
    def get(self, request):
        return render(request, 'section/section.html')

    def post(self, request):
        nome_usuario = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        
        # Armazenando os dados na sessão
        request.session['nome_usuario'] = nome_usuario
        request.session['email'] = email
        
        return redirect('blog_list')
    
##Encerrar a sessao
class EncerrarSessaoView(View):
    def get(self, request):
        request.session.flush()  # Remove todos os dados da sessão e exclui a sessão
        return redirect('/')  # Redireciona para a página inicial ou qualquer outra página