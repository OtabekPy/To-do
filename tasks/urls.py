from django.urls import path
from .views import index, update, delete
urlpatterns = [
   path('', index),
   path('update/<int:task_id>/', update),
   path('delete/<int:task_id>/', delete),
]