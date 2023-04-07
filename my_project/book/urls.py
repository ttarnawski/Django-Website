from django.urls import path
from .views import BookCreateView, BookDetailView, BookInstanceCreateView, BookInstanceDetailView, BookInstanceListView, BookInstanceUpdateView
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('create_instance/', BookInstanceCreateView.as_view(), name='create_instance'),
    path('detail_instance/<uuid:id>', BookInstanceDetailView.as_view(), name='detail_instance'),
    path('list_instance/', BookInstanceListView.as_view(), name='list_instance'),
    path('update_instance/<uuid:id>', BookInstanceUpdateView.as_view(), name='update_instance')
]