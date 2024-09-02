from django.contrib import admin
from django.urls import path
from blog.views import BlogCreateView, BlogDeleteView, BlogListView, BlogUpdateView, SolicitarDadosView, EncerrarSessaoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', BlogListView.as_view(), name="blog_list"),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="blog_update"),
    path('create/<int:pk>', BlogDeleteView.as_view(), name="blog_delete"),

    #Section
    path("", SolicitarDadosView.as_view(), name='blog_section'),
    path("encerra_sessao", EncerrarSessaoView.as_view(), name='blog_section_fim')
]