from rest_framework import serializers
from modules.models import Module, Lesson


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели образовательных модулей"""

    class Meta:
        model = Module
        fields = '__all__'

    def validate_name(self, value):
        """
        Валидатор для названия модуля.
        Разрешает использование букв, цифр и пробелов.
        """
        if not all(char.isalnum() or char.isspace() for char in value):
            raise serializers.ValidationError("Название может содержать только буквы, цифры и пробелы.")
        return value

    def validate(self, data):
        """
        Проверка на уникальность комбинации name и description.
        """
        if Module.objects.filter(name=data.get('name'), description=data.get('description')).exists():
            raise serializers.ValidationError("Модуль с таким названием и описанием уже существует.")
        return data


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели уроков"""

    class Meta:
        model = Lesson
        fields = '__all__'

    def validate_name(self, value):
        """
        Валидатор для названия урока.
        Разрешает использование букв, цифр и пробелов.
        """
        if not all(char.isalnum() or char.isspace() for char in value):
            raise serializers.ValidationError("Название может содержать только буквы, цифры и пробелы.")
        return value

    def validate(self, data):
        """
        Проверка на уникальность комбинации name и module.
        """
        if Lesson.objects.filter(name=data.get('name'), module=data.get('module')).exists():
            raise serializers.ValidationError("Урок с таким названием уже существует в данном модуле.")
        return data
