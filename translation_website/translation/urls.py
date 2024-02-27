from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('translate/', views.translation_form, name='translation'),  # Translation form URL
    path('translate/submit', views.translate_text, name='translate'),  # Translation submit URL
]

