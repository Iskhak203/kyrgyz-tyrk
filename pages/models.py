from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Колдонуучунун Профили (Ролдор үчүн) ---
class Profile(models.Model):
    ROLE_CHOICES = (
        ('teacher', 'Мугалим'),
        ('student', 'Окуучу'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student', verbose_name="Ролу")
    assigned_class = models.CharField(max_length=20, verbose_name="Классы (Окуучу болсо)", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

# Сигналдар: Колдонуучу катталганда Профиль автоматтык түрдө түзүлөт
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# --- Сиздин мурунку моделдериңиз ---
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Аталышы")
    description = models.TextField(verbose_name="Толук маалымат")
    image = models.ImageField(upload_to='news/', verbose_name="Сүрөт")
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Teacher(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Аты-жөнү")
    subject = models.CharField(max_length=100, verbose_name="Предмети")
    photo = models.ImageField(upload_to='teachers/', verbose_name="Сүрөтү")
    bio = models.TextField(verbose_name="Өмүр баяны", blank=True)
    def __str__(self): return self.full_name

class Achievement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Жетишкендик")
    description = models.TextField(verbose_name="Кыскача маалымат")
    image = models.ImageField(upload_to='achievements/', verbose_name="Сүрөт/Диплом")

class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name="Сүрөттүн аталышы")
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

class Schedule(models.Model):
    class_name = models.CharField(max_length=20, verbose_name="Класс")
    start_time = models.TimeField(verbose_name="Башталышы", null=True)
    end_time = models.TimeField(verbose_name="Аякташы", null=True)
    subject = models.CharField(max_length=100, verbose_name="Предмет", null=True)
    teacher_name = models.CharField(max_length=100, verbose_name="Мугалим", null=True)
    
    # Мугалим менен байланыштыруу (Система автоматтык түрдө таануу үчүн)
    teacher_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'profile__role': 'teacher'})