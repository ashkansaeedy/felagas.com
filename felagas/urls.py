from django.contrib import admin
from django.urls import include,path
# from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('', include('index.urls')),
    path('index/', include('index.urls')),
    path('becomeamodel/', include('becomeamodel.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
