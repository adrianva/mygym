from rest_framework import viewsets, permissions

from .models import Exercise, ExerciseInstances, Plan, PlanDays
from .serializers import ExerciseSerializer, ExerciseInstancesSerializer, PlanSerializer, PlanDaysSerializer


class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    his viewset automatically provides list, create, retrieve, update and `destroy` actions for Exercises.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ExerciseInstancesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and destroy actions for Exercise Instances.
    """
    queryset = ExerciseInstances.objects.all().order_by('order')
    serializer_class = ExerciseInstancesSerializer
    ordering_fields = 'order'
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        exercise_id = serializer.validated_data["exercise"]["id"]
        exercise = Exercise.objects.get(id=exercise_id)
        serializer.save(exercise=exercise)


class PlanViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and destroy actions for Plans.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(serializer)
        days = serializer.validated_data["days"]
        for day in days:
            plan_day = PlanDays.objects.create(
                plan=serializer,
                day_name=day["day_name"],
                order=day["order"]
            )
            exercises = day["exercises"]
            for exercise in exercises:
                ExerciseInstances.objects.create(
                    exercise=exercise["exercise"],
                    day=plan_day,
                    exercise_duration=exercise["exercise_duration"],
                    order=exercise["order"]
                )


class PlanDayViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and destroy actions for Plan Days.
    """
    queryset = PlanDays.objects.all().order_by('order')
    serializer_class = PlanDaysSerializer
    ordering_fields = 'order'
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
