from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    #user is the foreign key that connects to the default user model
    #user = pass
    #it is a foriegn key which is connected to User which is the imported model
    #on_delete   This is the behaviour to adopt when the referenced object is deleted. It is not specific to Django; this is an SQL standard.
    #CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well).
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    #allows it to be blank
    bio = models.TextField(blank=True)
    #in the brackets we specify in which folder the pic will be uploaded to,if it doesnt exist it will be created by django.if user doesnt upload a default image will be added
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100,blank=True)
    #it is optional so that the admin wont see object 1 or object 2, rather the useranme of the user 
    def __str__(self):
                return self.user.username
    
class Post(models.Model):
        id=models.UUIDField(primary_key=True,default=uuid.uuid4)
        user=models.CharField(max_length=100)
        image=models.ImageField(upload_to='post_images')
        caption=models.TextField()
        created_at=models.DateTimeField(default=datetime.now)
        no_of_likes=models.IntegerField(default=0)
        def __str__(self):
                return self.user
        #not username because this is not an object that has been passed here and not a foreign key

class LikePost(models.Model):
        post_id=models.CharField(max_length=500)
        username=models.CharField(max_length=100)
        def __str__(self):
                return self.username
        
class FollowersCount(models.Model):
        follower=models.CharField(max_length=500)
        user=models.CharField(max_length=100)
        def __str__(self):
                return self.user        