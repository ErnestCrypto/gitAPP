# Registering our models
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    class Meta:
        list_display = [
            'username',
            'password',
            'email',
            'date',
            'contact'
        ]
