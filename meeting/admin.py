from django.contrib import admin

from .models import Profile
from .models import Project
from .models import Member
from .models import TimeAvailability
from .models import Meeting

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Member)
admin.site.register(TimeAvailability)
admin.site.register(Meeting)