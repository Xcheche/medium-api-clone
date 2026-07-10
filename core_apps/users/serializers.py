from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


#========Import the User model========
User = get_user_model()

#========User Serializer========
class UserSerializer(serializers.ModelSerializer):
    """Serializing the custom user model to include additional fields from the related Profile model."""
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_picture")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")



    class Meta:
        model =  User
        fields = ["id",
                  "email",
                  "first_name",
                  "last_name",
                  "gender",
                  "phone_number",
                  "profile_photo",
                  "country",
                  "city"
                ]
        

    #========Override the to_representation method to include the admin field========    
    def to_representation(self, instance):
        """Making sure that the admin field is included in the serialized representation of the user."""
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


#========Custom Register Serializer for User Registration========
class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Remove the username field
    password1 = serializers.CharField(write_only=True)         
    password2 = serializers.CharField(write_only=True)   
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)



    #=======Override the get_cleaned_data method to remove the password fields========

    def get_cleaned_data(self):
        """
        Override the get_cleaned_data method to remove the password fields
        """
        super().get_cleaned_data()
        return{
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }
    
    #=======Override the save method to create a user without a username========
    def save(self, request):
        """
        Override the save method to create a user without a username
        """
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.set_password(self.cleaned_data.get("password1"))
        user.save()
        setup_user_email(request, user, [])
        return user