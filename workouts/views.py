from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, permissions

import requests

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


def show_plans(request):
    json = {}
    response = requests.get(settings.API_URL + '/plans/')
    json['plans'] = response.json()
    return render(request, 'plans.html', json)


def plan_detail(request):
    json = {}
    plan_id = request.GET.get('plan', None)
    response = requests.get(settings.API_URL + '/plans/' + plan_id)
    json['plan'] = response.json()
    return render(request, 'plan_detail.html', json)