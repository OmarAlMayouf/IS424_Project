from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_product, name='create_product'),
    path('read/', views.read_product, name='read_product'),
    path('search/', views.search_medicines, name='search_medicines'),
    path('<int:id>/update/', views.update_product, name='update_product'),
    path('<int:id>/view/', views.view_product, name='view_product'),
    path('<int:id>/delete/', views.delete_product, name='delete_product'),
]