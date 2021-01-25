from django.contrib import admin
from .models import customer_details, renewal, trainer_details, branch, subscription

# Register your models here.
admin.site.register(customer_details)
admin.site.register(renewal)
admin.site.register(trainer_details)
admin.site.register(branch)
admin.site.register(subscription)
