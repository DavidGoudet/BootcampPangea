from django.urls import path

from . import views

urlpatterns = [
    # ej: /encuestas/
    path('', views.index, name='index'),
    # ej: /encuestas/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ej: /encuestas/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ej: /encuestas/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]