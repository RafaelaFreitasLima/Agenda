from django.contrib import admin
from AgendaApp.models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_display_links = ['nome']
    list_filter = ['data_nascimento', 'bairro', 'estado', 'cidade']
    search_fields = ['nome', 'apelido']


admin.site.register(Contato, ContatoAdmin)