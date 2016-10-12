from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'exercise_name')


class ExerciseInstancesSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    #exercise = serializers.IntegerField(source='exercise.id')

    day = serializers.SlugRelatedField(
        many=False,
        queryset=PlanDays.objects.all(),
        slug_field='day_name',
    )

    class Meta:
        model = ExerciseInstances
        fields = ('id', 'exercise', 'day', 'exercise_duration', 'order')


class PlanDaysSerializer(serializers.ModelSerializer):
    plan = serializers.SlugRelatedField(
        many=False,
        queryset=Plan.objects.all(),
        slug_field='plan_name'
    )
    exercises = ExerciseInstancesSerializer(many=True)

    class Meta:
        model = PlanDays
        fields = ('id', 'plan', 'exercises', 'day_name', 'order')


class PlanSerializer(serializers.ModelSerializer):
    days = PlanDaysSerializer(many=True)

    class Meta:
        model = Plan
        fields = ('id', 'plan_name', 'plan_description', 'plan_difficulty', 'days')
