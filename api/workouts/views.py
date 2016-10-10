from rest_framework import viewsets, permissions

from .models import Exercise, ExerciseInstances, Plan, PlanDays
from .serializers import ExerciseSerializer, ExerciseInstancesSerializer, PlanSerializer, PlanDaysSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    his viewset automatically provides list, create, retrieve, update and `destroy` actions for Exercises.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ExerciseInstancesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and `destroy` actions for Exercise Instances.
    """
    queryset = ExerciseInstances.objects.all()
    serializer_class = ExerciseInstancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and `destroy` actions for Plans.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PlanDayViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and `destroy` actions for Plan Days.
    """
    queryset = PlanDays.objects.all()
    serializer_class = PlanDaysSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
