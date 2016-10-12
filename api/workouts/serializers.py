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
        required=False,
    )

    class Meta:
        model = ExerciseInstances
        fields = ('id', 'exercise', 'day', 'exercise_duration', 'order')


class PlanDaysSerializer(serializers.ModelSerializer):
    plan = serializers.SlugRelatedField(
        many=False,
        queryset=Plan.objects.all(),
        slug_field='plan_name',
        required=False,
    )
    exercises = ExerciseInstancesSerializer(many=True, required=False)

    class Meta:
        model = PlanDays
        fields = ('id', 'plan', 'exercises', 'day_name', 'order')


class PlanSerializer(serializers.ModelSerializer):
    days = PlanDaysSerializer(many=True)

    class Meta:
        model = Plan
        fields = ('id', 'plan_name', 'plan_description', 'plan_difficulty', 'days')

    def create(self, validated_data):
        days = validated_data.pop('days')
        plan = Plan.objects.create(**validated_data)
        for day in days:
            plan_day = PlanDays.objects.create(
                plan=plan,
                day_name=day["day_name"],
                order=day["order"]
            )
            exercises = day["exercises"]
            for exercise in exercises:
                ExerciseInstances.objects.create(
                    exercise=Exercise.objects.get(exercise_name=exercise["exercise"]["exercise_name"]),
                    day=plan_day,
                    exercise_duration=exercise["exercise_duration"],
                    order=exercise["order"]
                )

        return plan
