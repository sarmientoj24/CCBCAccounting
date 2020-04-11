from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name="members"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('add_member/', views.add_member, name="add_member")
    # path('profile/<str:pk>/', views.profile)
]
