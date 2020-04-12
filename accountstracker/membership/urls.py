from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name="members"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('add_member/', views.add_member, name="add_member"),
    path(
        'add_transaction/<str:pk>/',
        views.add_transaction, name="add_transaction"),
    path('profile/delete/<str:pk>/', views.delete_member, name="delete_member")
]
