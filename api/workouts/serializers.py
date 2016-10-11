from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'exercise_name')


class ExerciseInstancesSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    day = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='day_name'
    )

    class Meta:
        model = ExerciseInstances
        fields = ('id', 'exercise', 'day', 'exercise_duration', 'order')


class PlanDaysSerializer(serializers.ModelSerializer):
    plan = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='plan_name'
    )
    #exercises = ExerciseInstancesSerializer(many=True, read_only=True)
    exercises = serializers.SerializerMethodField('get_exercises_with_order')

    class Meta:
        model = PlanDays
        fields = ('id', 'plan', 'exercises', 'day_name', 'order')

    def get_exercises_with_order(self, obj):
        data = []
        exercises = ExerciseInstances.objects.filter(day=obj).order_by('order')
        for exercises in exercises:
            serializer = ExerciseInstancesSerializer(exercises)
            data.append(serializer.data)
        return data


class PlanSerializer(serializers.ModelSerializer):
    #days = PlanDaysSerializer(many=True, read_only=True)
    days = serializers.SerializerMethodField('get_days_with_order')

    class Meta:
        model = Plan
        fields = ('id', 'plan_name', 'plan_description', 'plan_difficulty', 'days')

    def get_days_with_order(self, obj):
        data = []
        days = PlanDays.objects.filter(plan=obj).order_by('order')
        for day in days:
            serializer = PlanDaysSerializer(day)
            data.append(serializer.data)
        return data
