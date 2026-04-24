from modeltranslation.translator import register, TranslationOptions
from .models import News, Teacher, Achievement

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio')

@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')