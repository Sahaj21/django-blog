from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

app_name = "blog"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name = 'register'),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]