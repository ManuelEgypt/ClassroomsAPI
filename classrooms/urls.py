
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from app.views import ClassroomsList,ClassroomDetails,UpdateClassroom,CancelClassroom,CreateClassroom
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/classrooms/', ClassroomsList.as_view(), name="classrooms-api"),
    path('api/create/',CreateClassroom.as_view(), name="classrooms-api-create"),
    path('api/detail/<int:classroom_id>/', ClassroomDetails.as_view(), name='classroom-details'), 
    path('update/<int:classroom_id>/', UpdateClassroom.as_view(), name='update-classroom'),
    path('delete/<int:classroom_id>/', CancelClassroom.as_view(), name='cancel-classroom'), 
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
