from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from blog_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/<int:post_id>', views.post_page, name='post_page'),
    path('create_post', views.create_post, name='make_post'),
    path('accounts/registration', views.signup, name='registration'),
    path('like/', views.like, name='like'),
]
