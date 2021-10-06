from django.urls import path
from profilesAPI import views

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    path('Allprofiles/', views.Allprofiles, name='Allprofiles'),
    path('Viewprofiles/<int:pk>/', views.Viewprofiles, name='Viewprofiles'),
    path('Createprofile/', views.Createprofile, name='Createprofile'),
    path('updateprofile/<int:pk>/', views.updateprofile, name='updateprofile'),
    path('deleteprofile/<int:pk>/', views.deleteprofile, name='deleteprofile'),

    path('Allrelationship/', views.Allrelationship, name='Allrelationship'),
    path('Viewrelationship/<int:pk>/', views.Viewrelationship, name='Viewrelationship'),
    path('Createrelationship/', views.Createrelationship, name='Createrelationship'),
    path('updaterelationship/<int:pk>/', views.updaterelationship, name='updaterelationship'),
    path('deleterelationship/<int:pk>/', views.deleterelationship, name='deleterelationship'),


]