from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal
    age_range = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state_province = models.CharField(max_length=50, blank=True)

    # Job
    job_role = models.CharField(max_length=50, blank=True)
    job_category = models.CharField(max_length=50, blank=True)
    job_level = models.CharField(max_length=50, blank=True)
    job_years = models.PositiveIntegerField(default=0)

    # Education
    education_degree = models.CharField(max_length=50, blank=True)
    education_school = models.CharField(max_length=50, blank=True)
    education_major = models.CharField(max_length=50, blank=True)
    education_year_graduated = models.PositiveIntegerField(default=0)

    # Misc
    interests = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
