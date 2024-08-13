from django.urls import path

from modules.apps import ModulesConfig
from modules.views import ModuleCreateAPIView, ModuleListAPIView, \
    ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView, LessonCreateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = ModulesConfig.name

urlpatterns = [
    path('module/create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('module/', ModuleListAPIView.as_view(), name='module-list'),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),

    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]
