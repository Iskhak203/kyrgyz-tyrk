from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# 1. Тилге көз каранды болбогон даректер (Админка жана Тил которуу)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# 2. Тилге жараша өзгөрүүчү даректер (мисалы: /ky/login/, /ru/login/)
urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    
    # Логин жана Логаут үчүн даректер
    # Django автоматтык түрдө registration/login.html шаблонун издейт
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Эгер башка auth даректери керек болсо (мисалы, пароль өзгөртүү):
    path('accounts/', include('django.contrib.auth.urls')),

    prefix_default_language=True # Демейки тилди да даректе көрсөтүү үчүн (мисалы /ky/)
)

# 3. Медиа жана Статикалык файлдарды DEBUG режиминде көрсөтүү
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)