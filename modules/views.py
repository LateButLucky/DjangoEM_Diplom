from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from modules.paginators import ModulesPaginator
from modules.permissions import IsModuleOwner, IsLessonOwner

from modules.models import Module, Lesson
from modules.serializers import ModuleSerializer, LessonSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """ Класс создания модуля"""

    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsModuleOwner]

    def perform_create(self, serializer):
        new_module = serializer.save()
        new_module.user = self.request.user
        new_module.save()


class ModuleListAPIView(generics.ListAPIView):
    """ Класс просмотра списка модулей"""

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModuleOwner]
    pagination_class = ModulesPaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра модуля"""

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModuleOwner]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения модуля"""

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModuleOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления модуля"""

    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModuleOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    """ Класс создания урока"""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsLessonOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """ Класс просмотра списка уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]
    pagination_class = ModulesPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('module',)
    ordering_fields = ('name',)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления урока"""

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]
