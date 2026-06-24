from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimestampedModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

# Create your models here.

# Get the user model
User = get_user_model()

#Text choices
class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")   



class Profile(TimestampedModel):
    """
    Profile model to store additional information about the user.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
  
    phone_number = PhoneNumberField(max_length=30, default=("+234 7048706557"),
                                    blank=True, null=True,verbose_name=_("Phone Number"))
    about_me = models.TextField(blank=True, null=True, verbose_name=_("About Me"))

    gender = models.CharField(
        max_length=20,choices=Gender.choices, default=Gender.OTHER, verbose_name=_("Gender"))
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True, verbose_name=_("Profile Picture"), default="/profile_default.png"
    )

    
    country = CountryField(blank_label="(select country)", blank=True, null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=255, blank=False, null=False, default="Lagos", verbose_name=_("City"))
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    followers = models.ManyToManyField(
       "self", symmetrical=False, related_name="following", blank=True, verbose_name=_("Followers")
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    # String representation of the profile
    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    
    # Method to get the number of followers
    def follow(self, profile):
        """
        Follow another user's profile.
        """
        self.followers.add(profile)
    
    # Method to unfollow a profile
    def unfollow(self, profile):
        """
        Unfollow another user's profile.
        """
        self.followers.remove(profile)    

    # Method to check if the current user is following another user's profile
    def check_following(self, profile):
        """
        Check if the current user is following another user's profile.
        """
        return self.followers.filter(pkid=profile.pkid).exists()    
