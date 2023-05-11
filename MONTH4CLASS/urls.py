from django.contrib import admin
from django.urls import path
from posts.views import hello, now_date, goodbye
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('date/',now_date ),
    path('goodbye/', goodbye),

]
