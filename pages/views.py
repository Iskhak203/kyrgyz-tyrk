from django.shortcuts import render, redirect
from .models import News, Teacher, Gallery, Achievement, Schedule, Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required # Бул бетке кирүү үчүн сөзсүз катталуу керек
def home_page(request):
    query = request.GET.get('q')
    user = request.user
    
    # 1. Жалпы маалыматтар
    gallery = Gallery.objects.all().order_by('-created_at')[:8]
    achievements = Achievement.objects.all()
    
    # 2. Ролдорго жараша Графикти фильтрлөө
    try:
        user_role = user.profile.role
    except Profile.DoesNotExist:
        user_role = 'student'

    if user_role == 'teacher':
        # Мугалим өзүнүн гана сабактарын корот
        schedules = Schedule.objects.filter(teacher_user=user).order_by('start_time')
    elif user_role == 'student' and user.profile.assigned_class:
        # Окуучу өзүнүн классынын сабактарын корот
        schedules = Schedule.objects.filter(class_name=user.profile.assigned_class).order_by('start_time')
    else:
        # Эгер белгисиз болсо, бардык графикти көрсөтөбүз
        schedules = Schedule.objects.all().order_by('class_name')

    # 3. Издөө логикасы
    if query:
        news = News.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        teachers = Teacher.objects.filter(Q(full_name__icontains=query) | Q(subject__icontains=query))
        is_search = True
    else:
        news = News.objects.all().order_by('-date_posted')[:3]
        teachers = Teacher.objects.all()
        is_search = False

    context = {
        'query': query,
        'news': news,
        'teachers': teachers,
        'gallery': gallery,
        'achievements': achievements,
        'schedules': schedules,
        'is_search': is_search,
        'user_role': user_role,
    }
    
    return render(request, 'index.html', context)