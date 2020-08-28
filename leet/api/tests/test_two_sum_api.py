from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ConfigurationTests(APITestCase):
    def test_multiple(self):
        data = {'numbers': [19, 2, 13, -400, 5, 410, -3, 8, -9], 'target': 10}
        expected = [[3, 5], [2, 6], [1, 7], [0, 8]]

        url = reverse('two-sum-multiple')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], expected)

    def test_trash_memory(self):
        data = {'numbers': [19, 2, 13, -400, 5, 410, -3, 11, -9], 'target': -1}
        expected = [1, 6]

        url = reverse('two-sum-trash-memory')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], expected)

    def test_brute(self):
        data = {'numbers': [19, 2, 13, -400, 5, 410, -3, 11, -9], 'target': -1}
        expected = [1, 6]

        url = reverse('two-sum-brute')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], expected)

    def test_outside_in(self):
        data = {'numbers': [-400, -9, -3, 2, 5, 11, 13, 19, 410], 'target': -1}
        expected = [2, 3]

        url = reverse('two-sum-outside-in')
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], expected)
