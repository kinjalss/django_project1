# from django.urls import path
# from . import views 
from django.conf import settings
from django.conf.urls.static import static
# from .views import about
# urlpatterns = [
#     # path('home/', views.home,name="home"),
#     # path('getuser/<name>/<id>',views.pathview,name="pathview"),
#     #  path('getuser/', views.pathview, name="pathview"),
#      path('showform/', views.showform, name="showform"),
#      path('getform/', views.getform, name='getform'),
#      path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
     
  
#     path('', views.home, name="home"),  # Home page
#     # path('about/', views.about, name='about'),
#     # path('menu/', views.menu, name="menu"),
#     path('book/', views.book, name="book"),
#     # path('about/',views.about,name='about'),
#     path('menu/', views.menu, name='menu'),
#     path('menu_card/', views.menu_card, name='menu_card'),
#     path("about/", about, name="about"),

    
# ]
from django.urls import path
from myapp.views import home, about, menu, book

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('index/', home, name='index'),
    path('book/', book, name='book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
