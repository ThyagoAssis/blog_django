from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

#Cptura de sessoes
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse


class BlogListView(ListView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ["titulo", "conteudo"]
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["titulo", "conteudo"]
    success_url = reverse_lazy('blog_list')
    

class BlogDeleteView(DeleteView):
    model = Blog
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