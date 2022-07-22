from django.contrib import admin

from .models import Pro_soccer_info
from polls.models import Question,Choice
from . import models
# Register your models here.

admin.site.register(Pro_soccer_info)

@admin.register(models.Team_honors)
class Team_HonorsAdmin(admin.ModelAdmin):
    list_display = ['number_of_goals','earned_awards','active_teams','active_player']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price']

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['message','name','message_type']

@admin.register(models.Next_matches)
class Next_matchsAdmin(admin.ModelAdmin):
    list_display = ['first_team_name','second_team_name','clock','league_type']

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','season','type','author']
    search_fields = ['title__istartswith']
    ordering = ['-id']
@admin.register(models.Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ['title','date']

@admin.register(models.Latest_result)
class Latest_resultAdmin(admin.ModelAdmin):
    list_display = ['first_team_name','second_team_name','league_type','month']

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title','type','date']

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','location','date']

@admin.register(models.League_Table)
class LeagueTableAdmin(admin.ModelAdmin):
    list_display = ['team','pos','Pts']
    ordering = ['pos']
@admin.register(models.Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['name','age']

@admin.register(models.Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title','date']

@admin.register(models.Sport_fields)
class Sport_fieldsAdmin(admin.ModelAdmin):
    list_display = ['title','field']

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name','post','team']
    search_fields = ['full_name']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','count','owner']

@admin.register(models.Users_count)
class User_countAdmin(admin.ModelAdmin):
    list_display = ['user']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields' : ['question_text']}),
        ('Date information', {'fields' :  ['pub_date'],
        'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)