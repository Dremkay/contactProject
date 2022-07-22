from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<str:pk>', views.edit_contact, name='edit_contact'),
    path('profile/<str:pk>', views.profile,name='profile'),
    path('delete/<str:pk>',views.delete,name='delete')
]
