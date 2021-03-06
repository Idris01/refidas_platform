from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="home"

urlpatterns = [
	path("",views.index, name="index"),
	path("services/",views.services, name="services")
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)