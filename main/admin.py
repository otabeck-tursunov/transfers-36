from django.contrib import admin
from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'coach', 'found_date', 'country',)
    search_fields = ('name',)
    list_filter = ('country',)
    ordering = ('found_date', 'name')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'number', 'age', 'price', 'nation', 'club',)
    search_fields = ('name',)
    list_filter = ('club', 'position', 'nation')
    ordering = ('number', 'age', 'price')
