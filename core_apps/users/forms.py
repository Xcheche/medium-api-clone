from django import forms
# Comes with usercreationform and userchangeform django auth/admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from django.contrib.auth import get_user_model



# Get the custom user model
User = get_user_model()

# Form for updating user information in the admin interface
class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
       


# Form for creating new users in the views 
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email")

        # Custom error messages for the form
        error_messages = {
            "duplicate": ("A user with that email address already exists."),
        }       

        #Validate email uniqueness
        def clean_email(self):
            email = self.cleaned_data["email"]
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(
                self.error_messages["duplicate"],
                code="duplicate",
            )
