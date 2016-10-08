from __future__ import unicode_literals

from django.db import models


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'exercise'


class ExerciseInstances(models.Model):
    exercise_id = models.IntegerField()
    day_id = models.IntegerField()
    exercise_duration = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exercise_instances'


class Plan(models.Model):
    plan_name = models.CharField(max_length=150)
    plan_description = models.TextField()
    plan_difficulty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plan'


class PlanDays(models.Model):
    plan_id = models.IntegerField()
    day_name = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plan_days'
