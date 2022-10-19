from django.contrib import admin
from django.urls import path

from teacher.views import ProfessorAPIView, CadastrarAulaAPiView, RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professores/', ProfessorAPIView.as_view()),
    path('professores/<int:id>/aulas', CadastrarAulaAPiView.as_view()), 
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]
