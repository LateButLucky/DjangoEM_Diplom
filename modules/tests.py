from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module, Lesson
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.net")
        self.user.set_password('admin1')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def authenticate(self):
        response = self.client.post('/users/token/', {
            "email": "admin@example.net", "password": "admin1"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_module(self):
        """ тестирование создания модуля """
        self.authenticate()

        data_module = {
            'user': self.user.pk,
            'name': 'test',
            'description': 'test',
        }

        response = self.client.post(reverse('modules:module-create'), data=data_module)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'test')
        self.assertTrue(Module.objects.filter(name='test').exists())

    def test_list_module(self):
        """ тестирование списка модулей """
        self.authenticate()

        module = Module.objects.create(
            user=self.user,
            name='list test',
            description='list test',
        )

        response = self.client.get(reverse('modules:module-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['name'], 'list test')

    def test_detail_module(self):
        """ тестирование информации о модуле """
        self.authenticate()

        module = Module.objects.create(
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.get(reverse('modules:module-get', kwargs={'pk': module.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'test')

    def test_update_module(self):
        """ тестирование изменения модуля """
        self.authenticate()

        module = Module.objects.create(
            user=self.user,
            name='test',
            description='test',
        )

        data_module_update = {
            'name': 'test1',
        }

        response = self.client.patch(reverse('modules:module-update', kwargs={'pk': module.pk}),
                                     data=data_module_update)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'test1')

    def test_delete_module(self):
        """ тестирование удаления модуля """
        self.authenticate()

        module = Module.objects.create(
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.delete(reverse('modules:module-delete', kwargs={'pk': module.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Module.objects.filter(pk=module.pk).exists())

    def test_module_create_validation_error(self):
        """ тест ошибки валидации """
        self.authenticate()

        data = {
            'name': '#@*-^',
            'description': 'test3'
        }

        response = self.client.post(reverse('modules:module-create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.net")
        self.user.set_password('admin1')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.module = Module.objects.create(
            name='test12',
            description='test12',
            user=self.user
        )

    def authenticate(self):
        response = self.client.post('/users/token/', {
            "email": "admin@example.net", "password": "admin1"
        })
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_lesson(self):
        """ тестирование создания урока """
        self.authenticate()

        data_lesson = {
            'module': self.module.pk,
            'user': self.user.pk,
            'name': 'test1',
            'description': 'test1',
        }

        response = self.client.post(reverse('modules:lesson-create'), data=data_lesson)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'test1')
        self.assertTrue(Lesson.objects.filter(name='test1').exists())

    def test_list_lesson(self):
        """ тестирование списка уроков """
        self.authenticate()

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='list lesson',
            description='list lesson',
        )

        response = self.client.get(reverse('modules:lesson-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['name'], 'list lesson')

    def test_detail_lesson(self):
        """ тестирование информации о уроке """
        self.authenticate()

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.get(reverse('modules:lesson-get', kwargs={'pk': lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'test')

    def test_update_lesson(self):
        """ тестирование изменения урока """
        self.authenticate()

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        data_lesson_update = {
            'name': 'test123',
        }

        response = self.client.patch(reverse('modules:lesson-update', kwargs={'pk': lesson.pk}),
                                     data=data_lesson_update)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'test123')

    def test_delete_lesson(self):
        """ тестирование удаления урока """
        self.authenticate()

        lesson = Lesson.objects.create(
            module=self.module,
            user=self.user,
            name='test',
            description='test',
        )

        response = self.client.delete(reverse('modules:lesson-delete', kwargs={'pk': lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(pk=lesson.pk).exists())
