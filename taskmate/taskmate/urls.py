from django.contrib import admin
from django.urls import path, include
from todolist import views as todoViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoViews.home, name="home"),
    path('contact/', todoViews.contact, name="contact"),
    path('about/', todoViews.about, name="about"),
    path('task/', include('todolist.urls')),
    path('account/', include('user_app.urls')),
]
