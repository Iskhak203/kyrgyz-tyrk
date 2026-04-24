from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from modeltranslation.admin import TranslationAdmin
from .models import News, Teacher, Gallery, Schedule, Achievement, Profile

# 1. User Adminди кеңейтүү (Профилди User ичинде көрсөтүү үчүн)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role')
    
    def get_role(self, obj):
        return obj.profile.get_role_display()
    get_role.short_description = 'Ролу'

# Стандарттык UserAdminди биздики менен алмаштырабыз
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# 2. Башка моделдерди каттоо
@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'description')

@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    list_display = ('full_name', 'subject')
    list_filter = ('subject',)

@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    # Графикти көрүүдө маанилүү талааларды чыгарабыз
    list_display = ('class_name', 'subject', 'start_time', 'end_time', 'teacher_name', 'teacher_user')
    list_filter = ('class_name', 'subject')
    search_fields = ('class_name', 'teacher_name')