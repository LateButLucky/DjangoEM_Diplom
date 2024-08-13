from rest_framework import serializers

from modules.models import Module, Lesson
from modules.validators import TitleValidator


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели образовательных модулей"""

    class Meta:
        model = Module
        fields = '__all__'
        validators = [TitleValidator(field='name')]
        serializers.UniqueTogetherValidator(fields=['name', 'description'],
                                            queryset=Module.objects.all())


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели уроков"""

    class Meta:
        model = Lesson
        fields = '__all__'
