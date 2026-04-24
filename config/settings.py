import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# 1. Негизги дарек
BASE_DIR = Path(__file__).resolve().parent.parent

# Коопсуздук
SECRET_KEY = 'django-insecure-ej-c33@2d798!p*q9rt)zx8v*-=aawj-e1f(917*(t!)%pxike'
DEBUG = True
ALLOWED_HOSTS = []

# 2. Тиркемелерди кошуу
INSTALLED_APPS = [
    # Custom Admin (Башкалардан өйдө турушу керек)
    'jazzmin',
    
    # Көп тилдүүлүк үчүн (Админден өйдө турушу керек)
    'modeltranslation',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Биздин тиркеме
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Тилдерди которуу үчүн иштетүүчү (Middleware)
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 3. Маалыматтар базасы
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 4. Тил жана локализация (Кыргызча, Орусча, Түркчө)
LANGUAGE_CODE = 'ky'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Тилдердин тизмеси
LANGUAGES = (
    ('ky', _('Kyrgyz')),
    ('ru', _('Russian')),
    ('tr', _('Turkish')),
)

# Котормо файлдары сактала турган папка
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/'),
]

# 5. Статикалык жана Медиа файлдар
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 6. JAZZMIN СТАТУСУ (Custom Admin Panel орнотуулары)
JAZZMIN_SETTINGS = {
    "site_title": "№52 Мектеп Админ",
    "site_header": "Кыргыз-Түрк достугу №52",
    "site_brand": "№52 Мектеп",
    "welcome_sign": "Кош келиңиз! Башкаруу панелине кириңиз.",
    "copyright": "№52 Мектеп - Кыргыз-Түрк достугу",
    "search_model": ["pages.News", "pages.Teacher"],
    "topmenu_links": [
        {"name": "Башкы бет", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Сайтка өтүү", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "theme": "flatly", # Дизайндын түрү (dark, flatly, cosmo ж.б.)
}