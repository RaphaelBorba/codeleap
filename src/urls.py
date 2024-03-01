from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_or_create),
    path('<int:post_id>', views.delete_or_update),
    
]