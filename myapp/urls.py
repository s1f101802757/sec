from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
 
#from .views import file_download_view

urlpatterns = [
    path('', views.index_template, name='index'),
    path('syou/', views.syou, name='syou'),
     #path('download/', views.download, name='download_pdf_file'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

