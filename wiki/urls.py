from django.urls import path
from wiki import views


app_name = 'wiki'
urlpatterns = [
    path('', views.page_index, name='index'),
    path('<str:slug>/', views.page_view, name='page_view'),
    path('<str:slug>/edit/', views.page_edit, name='page_edit'),
    path('<str:slug>/save/', views.page_save, name='page_save'),
]