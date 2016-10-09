from rest_framework import serializers
from workouts.models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'exercise_name')


class PlanDaysSerializer(serializers.ModelSerializer):
    plan = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='plan_name'
    )

    class Meta:
        model = PlanDays
        fields = ('id', 'plan', 'day_name', 'order')


class PlanSerializer(serializers.ModelSerializer):
    days = PlanDaysSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = ('id', 'plan_name', 'plan_description', 'plan_difficulty', 'days')


class ExerciseInstancesSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    day = PlanDaysSerializer()

    class Meta:
        model = ExerciseInstances
        fields = ('id', 'exercise', 'day', 'exercise_duration', 'order')
