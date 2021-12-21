from django.urls import path
from . import views

app_name='review'

urlpatterns = [
    path('', views.review_list, name="list"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:pk>/update/', views.review_update, name="update"),
    path('<int:pk>/delete/', views.review_delete, name="delete"),

]