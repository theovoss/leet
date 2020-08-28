import json

from django import forms
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.reverse import reverse

from leet.api.problems.two_sum import TwoSum
from leet.api.serializers.two_sum_serializer import TwoSumSerializer


class TwoSumViewset(viewsets.ViewSet):
    """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:

        Given {
            "numbers": [2, 7, 11, 15],
            "target": 9
        }

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """

    # TODO: serializer class isn't quite working how I expect
    serializer_class = TwoSumSerializer

    def list(self, request):
        return Response({
            "urls": {
                "Brute": {
                    "description": TwoSum.brute.__doc__.strip(),
                    "url": request.build_absolute_uri(reverse('two-sum-brute'))
                },
                "Outside In": {
                    "description": TwoSum.outside_in.__doc__.strip(),
                    "url": request.build_absolute_uri(reverse('two-sum-outside-in'))
                },
                "trash_memory": {
                    "description": TwoSum.trash_memory.__doc__.strip(),
                    "url": request.build_absolute_uri(reverse('two-sum-trash-memory'))
                }
            }
        })

    @csrf_exempt
    @action(methods=['GET', 'POST'], detail=False, url_name="brute")
    def brute(self, request, pk=None):
        """
        Sample input:
        ```
        {
            "numbers": [2, 7, 11, 15],
            "target": 9
        }
        ```
        """
        if request.method == "GET":
            return Response()
        else:
            serializer = TwoSumSerializer(data=request.data)
            serializer.is_valid()
            return Response(TwoSum().brute(serializer.validated_data['numbers'], serializer.validated_data['target']))

    @csrf_exempt
    @action(methods=['GET', 'POST'], detail=False, url_name="outside-in")
    def outside_in(self, request, pk=None):
        """
        Sample input:
        ```
        {
            "numbers": [2, 7, 11, 15],
            "target": 9
        }
        ```
        """
        if request.method == "GET":
            return Response()
        else:
            serializer = TwoSumSerializer(data=request.data)
            serializer.is_valid()
            return Response(TwoSum().outside_in(serializer.validated_data['numbers'], serializer.validated_data['target']))

    @csrf_exempt
    @action(methods=['GET', 'POST'], detail=False, url_name="trash-memory")
    def trash_memory(self, request, pk=None):
        """
        Sample input:
        ```
        {
            "numbers": [2, 7, 11, 15],
            "target": 9
        }
        ```
        """
        if request.method == "GET":
            return Response()
        else:
            serializer = TwoSumSerializer(data=request.data)
            serializer.is_valid()
            return Response(TwoSum().trash_memory(serializer.validated_data['numbers'], serializer.validated_data['target']))
