from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.http import QueryDict

from main.views import IndexPageView, ChangeLanguageView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),
    path('atlus/', include('Atlus.urls')),
    #path('boomerang/', include('Boomerang.urls')),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

   
    path('Contact/', views.contact, name = 'Contact'),
    path('Portfolio/', views.portfolio, name = 'Portfolio'),
    path('About/', views.about, name = 'About'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
