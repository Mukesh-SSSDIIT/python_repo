from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_book),
    path('add_book/', views.add_book),
    path('edit_book/<int:id>', views.edit_book),
    path('update_book/<int:id>', views.update_book),
    path('delete_book/<int:id>', views.delete_book),
]
