from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from leet.api.problems.two_sum import TwoSum
from leet.api.serializers.two_sum_serializer import TwoSumSerializer


class TwoSumViewset(viewsets.ViewSet):
    """
        Leet: https://leetcode.com/problems/two-sum/

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

    def _generate_output(self, inputs, method):
        numbers = inputs['numbers']
        target = inputs['target']
        return {
            'input': {'numbers': numbers, 'target': target},
            'result': method(numbers, target),
        }

    def list(self, request):
        return Response(
            {
                "urls": {
                    "Leet": {"url": "https://leetcode.com/problems/two-sum/"},
                    "Brute": {
                        "description": TwoSum.brute.__doc__.strip(),
                        "url": request.build_absolute_uri(reverse('two-sum-brute')),
                        "code": "https://github.com/theovoss/leet/blob/master/leet/api/problems/two_sum.py#L6-L14",
                    },
                    "Outside In": {
                        "description": TwoSum.outside_in.__doc__.strip(),
                        "url": request.build_absolute_uri(
                            reverse('two-sum-outside-in')
                        ),
                        "code": "https://github.com/theovoss/leet/blob/master/leet/api/problems/two_sum.py#L16-L35",
                    },
                    "trash_memory": {
                        "description": TwoSum.trash_memory.__doc__.strip(),
                        "url": request.build_absolute_uri(
                            reverse('two-sum-trash-memory')
                        ),
                        "code": "https://github.com/theovoss/leet/blob/master/leet/api/problems/two_sum.py#L37-L46",
                    },
                    "multiple": {
                        "description": TwoSum.trash_memory.__doc__.strip(),
                        "url": request.build_absolute_uri(reverse('two-sum-multiple')),
                        "code": "https://github.com/theovoss/leet/blob/master/leet/api/problems/two_sum.py#L49-L60",
                    },
                }
            }
        )

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
            return Response(
                self._generate_output(serializer.validated_data, TwoSum().brute)
            )

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
            return Response(
                self._generate_output(serializer.validated_data, TwoSum().outside_in)
            )

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
            return Response(
                self._generate_output(serializer.validated_data, TwoSum().trash_memory)
            )

    @csrf_exempt
    @action(methods=['GET', 'POST'], detail=False, url_name="multiple")
    def multiple(self, request, pk=None):
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
            return Response(
                self._generate_output(
                    serializer.validated_data, TwoSum().multiple_trash_memory
                )
            )
