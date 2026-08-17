from django.db import models

class Driver(models.Model):
    TRANSMISSION_CHOICES = [
        ('MANUAL', 'Manual Only'),
        ('AUTOMATIC', 'Automatic Only'),
        ('BOTH', 'Both Manual & Automatic'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField()
    transmission_type = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='BOTH')
    profile_photo = models.ImageField(upload_to='drivers/')
    is_verified = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)

    def __str__(self):
        return f"{self.full_name} - {self.city}"

class PricingTier(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='pricing')
    trip_type = models.CharField(max_length=50)  # e.g. "Local (4 Hrs)", "Outstation (Per Day)"
    base_rate = models.DecimalField(max_digits=8, decimal_places=2)
    overtime_rate_per_hour = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.driver.full_name} ({self.trip_type})"

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    pickup_address = models.TextField()
    start_datetime = models.DateTimeField()
    duration_hours = models.PositiveIntegerField(default=4)
    car_transmission = models.CharField(max_length=10, choices=Driver.TRANSMISSION_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.driver.full_name} by {self.customer_name}"