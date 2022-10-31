from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:result_id>/', views.detail, name="detail"),
    path('<int:result_id>/results', views.results, name="results"),
    path('<int:result_id>/vote', views.vote, name="vote"),
]