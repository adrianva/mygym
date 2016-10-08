from rest_framework import serializers
from workouts.models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'exercise_name')


class ExerciseInstancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInstances
        fields = ('id', 'exercise_id', 'day_id', 'exercise_duration', 'order')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'plan_name', 'plan_description', 'plan_dificulty')


class PlanDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDays
        fields = ('id', 'plan_id', 'day_name', 'order')

