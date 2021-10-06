from typing import BinaryIO
from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.urls import reverse

# Create your models here.

#############################################################################################################

class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self,sender):

        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))

        # Above we need to check two cases where sender is our profile or the receiver is our profile

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)

        available = [profile for profile in profiles if profile not in accepted]

        # above we need to exclude all profiles where rel = accepted and also select all profiles where only we are excluded
        # Here we used list comprehension method = newList = "[ expression(element) for element in oldList if condition ]"
        # to avoid long loops.

        print(available)
        return available

    def get_all_profiles(self,me):

        profiles= Profile.objects.all().exclude(user=me)
        return profiles

#############################################################################################################

class Profile(models.Model):

    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Bio = models.TextField(default='no bio ...',max_length=300)
    email = models.EmailField(max_length=200,blank=True)
    dob = models.DateField(blank=True,null=True)
    country = models.CharField(max_length=100,blank=True)
    avatar = models.ImageField(default = 'profile/images/avatar.png',upload_to="profile/images")
    friends = models.ManyToManyField(User,blank=True,related_name='friends')
    slug = models.SlugField(unique=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now =True)

    objects = ProfileManager()

    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view",kwargs={'slug':self.slug})

    def get_friends(self):
        return self.friends.all()
    
    def get_friends_no(self):
        return self.friends.all().count()

    def get_posts_no(self):
        return self.posts.all().count()    # author we named to posts

    def get_all_authors_post(self):
        return self.posts.all()
    
    def get_likes_given_no(self):
        likes = self.like_set.all()      # since related name to Like is not given
        total_liked = 0
        for item in likes:
            if item.value =='Like':
                total_liked += 1
        return total_liked

    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()    # object name 'liked' used instead of related name 'likes' because has no reverse relationship
        return total_liked

    
    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self. __initial_first_name = self.first_name
        self. __initial_last_name = self.last_name

    def save(self,*args, **kwargs):
        ex=False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name and self.last_name != self.__initial_last_name or self.slug =="":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name)+ " " +str(self.last_name))
                ex=Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " +str(get_random_code()))
                    ex=Profile.objects.filter(slug=to_slug).exists()
            else:
                 to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)



#############################################################################################################


STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)

class RelationshipManager(models.Manager):

    def invitations_received(self,receiver):
        qs = Relationship.objects.filter(receiver=receiver,status="send")
        return qs
        
        # instead of writing in views "Relationship.objects.filter()"" we now will write "Relationship.objects.invitations_received"

#############################################################################################################


class Relationship(models.Model):

    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status = models.CharField(max_length=8,choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects =RelationshipManager()

    def __str__(self):
        return str(self.sender)+"  "+str(self.receiver)+ "  " +str(self.status)


#############################################################################################################