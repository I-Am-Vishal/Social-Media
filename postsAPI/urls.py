from django.urls import path
from postsAPI import views

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    path('Allposts/', views.Allposts, name='Allposts'),
    path('Viewposts/<int:pk>/', views.Viewposts, name='Viewposts'),
    path('Createposts/', views.Createposts, name='Createposts'),
    path('updateposts/<int:pk>/', views.updateposts, name='updateposts'),
    path('deleteposts/<int:pk>/', views.deleteposts, name='deleteposts'),

    path('Alllikes/', views.Alllikes, name='Alllikes'),
    path('Viewlikes/<int:pk>/', views.Viewlikes, name='Viewlikes'),
    path('Createlikes/', views.Createlikes, name='Createlikes'),
    path('updatelikes/<int:pk>/', views.updatelikes, name='updatelikes'),
    path('deletelikes/<int:pk>/', views.deletelikes, name='deletelikes'),

    path('Allcomments/', views.Allcomments, name='Allcomments'),
    path('Viewcomments/<int:pk>/', views.Viewcomments, name='Viewcomments'),
    path('Createcomments/', views.Createcomments, name='Createcomments'),
    path('updatecomments/<int:pk>/', views.updatecomments, name='updatecomments'),
    path('deletecomments/<int:pk>/', views.deletecomments, name='deletecomments'),



]