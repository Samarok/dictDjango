from django.urls import path
from dictApp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "dictApp"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home),
    path('words_list/', views.wordsList, name = 'wordslist'),
    path('add_words/', views.addWords, name = 'addwords')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)