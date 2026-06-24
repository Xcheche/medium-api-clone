from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pkid", "followers_count", "user", "phone_number", "gender", "country", "city")
    list_display_links = ("pkid", "user")
    list_filter = ("gender", "country", "city")

    @admin.display(description="Followers Count")
    def followers_count(self, obj):
        return obj.followers.count()
    
    # Register the Profile model with the custom admin interface
admin.site.register(Profile, ProfileAdmin)