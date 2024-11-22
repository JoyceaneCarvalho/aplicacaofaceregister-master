from django.urls import path
from . import views
from .api.viewsets import AlunoViewsSets
from .api.viewsets import ProfessorViewsSets

from .views import index, perfilaluno, perfilprof, loginprof, loginaluno, cadastroaluno, cadastroprof, consfrequencia, realizarfreq, consfrequencia_prof, cadaluno


urlpatterns = [
    path('', index, name='index'),
    path('perfilaluno/', views.perfilaluno, name='perfilaluno'),
    path('perfilprof/', perfilprof, name='perfilprof'),
    path('loginprof/', loginprof, name='loginprof'),
    path('loginaluno/', loginaluno, name='loginaluno'),
    path('cadastroaluno/', views.cadastroaluno, name='cadastroaluno'),
    path('cadastroprof/', cadastroprof, name='cadastroprof'),
    path('consfrequencia/', consfrequencia, name='consfrequencia'),
    path('realizarfreq/', realizarfreq, name='realizarfreq'),
    path('consfrequencia_prof/', consfrequencia_prof, name='consfrequencia_prof'),
    path('cadaluno/', cadaluno, name='cadaluno'),
    path('api/aluno/', AlunoViewsSets.as_view(), name='aluno-list'),
    path('api/aluno/<str:id>', AlunoViewsSets.as_view(), name='aluno-detalhe'),
    path('api/professor/', ProfessorViewsSets.as_view(), name='professor-list'),
    path('api/professor/<str:id>', ProfessorViewsSets.as_view(), name='professor-detalhe')
]