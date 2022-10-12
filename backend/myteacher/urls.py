from django.contrib import admin
from django.urls import path

from teacher.views import ProfessorAPIView, CadastrarAulaAPiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professores/', ProfessorAPIView.as_view()),
    path('professores/<int:id>/aulas', CadastrarAulaAPiView.as_view()), 
]
