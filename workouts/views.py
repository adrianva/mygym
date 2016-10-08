from django.shortcuts import render
from rest_framework import viewsets, permissions
from workouts.models import Exercise, ExerciseInstances
from workouts.serializers import ExerciseSerializer, ExerciseInstancesSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseInstancesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and `destroy` actions.
    """
    queryset = ExerciseInstances.objects.all()
    serializer_class = ExerciseInstancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
