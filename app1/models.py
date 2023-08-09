# models.py

from django.db import models

class Login(models.Model):
    association_user_id = models.AutoField(primary_key=True)
    association_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Device(models.Model):
    device_id = models.CharField(max_length=100, primary_key=True)
    association_id = models.CharField(max_length=100)
    apartment_id = models.CharField(max_length=100)
    eb_over_voltage = models.BooleanField(default=False)
    eb_over_frequency = models.BooleanField(default=False)
    eb_over_current = models.BooleanField(default=False)
    eb_under_voltage = models.BooleanField(default=False)
    eb_under_frequency = models.BooleanField(default=False)
    eb_load_delay_time = models.IntegerField(default=0)
    eb_tripping_delay_timer = models.IntegerField(default=0)
    eb_trip_count = models.IntegerField(default=0)
    dg_over_voltage = models.BooleanField(default=False)
    dg_over_frequency = models.BooleanField(default=False)
    dg_over_current = models.BooleanField(default=False)
    dg_under_voltage = models.BooleanField(default=False)
    dg_under_frequency = models.BooleanField(default=False)
    dg_load_delay_time = models.IntegerField(default=0)
    dg_tripping_delay_timer = models.IntegerField(default=0)
    dg_trip_count = models.IntegerField(default=0)
    dg_auto_reset_delay_timer = models.IntegerField(default=0)
    dg_auto_retry_limit = models.IntegerField(default=0)
    kwh_limit = models.FloatField(default=0.0)
    dg_remote_delay = models.IntegerField(default=0)
    phase = models.CharField(max_length=50)
    added_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_id