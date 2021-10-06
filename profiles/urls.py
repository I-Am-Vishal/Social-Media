from . import views
from django.urls import path

from . views import (
    my_profile,
    invites_received_view,
    invite_profiles_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invitation,
    remove_from_friends,
    accept_invitation,
    reject_invitation,
    search,
      
)


app_name='profiles'

urlpatterns = [

    path('',ProfileListView.as_view(),name='all-profiles-view'),
    path('myprofile/',my_profile,name='my-profile'),
    path('my-invites/',invites_received_view,name='my-invites-view'),
    path('<slug>',ProfileDetailView.as_view(),name='profile-detail-view'),
    path('to-invite/',invite_profiles_list_view,name='invite-profiles-view'),
    path('send-invite/',send_invitation,name='send-invite'),
    path('remove-friend/',remove_from_friends,name='remove-friend'),
    path('my-invite/accept/',accept_invitation,name='accept-invite'),
    path('my-invite/reject/',reject_invitation,name='reject-invite'),
    path('search/' , search , name='search'),
   

]