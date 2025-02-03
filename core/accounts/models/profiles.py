from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .users import User


class Profile(models.Model):
    '''
    create profile for user and  our app
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    

    
    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create or update the user profile whenever a user is saved.
    """
    if created:
        Profile.objects.create(user=instance)
    # else:
    #     instance.profile.save()