
from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inner/', views.inner),
    path('portfolio/', views.portfolio),

]

