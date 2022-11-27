from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('osrs/', include('osrsMonsterDatabase.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('summernote/', include('django_summernote.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# client, secret
#1006858553666-q8c0oolskmimickm8buhnqohdgt5b8tk.apps.googleusercontent.com
#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
