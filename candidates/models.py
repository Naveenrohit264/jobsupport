from django.db import models

class Candidate(models.Model):

    STATUS_CHOICES = [
        ('Interview', 'Interview'),
        ('Assessment', 'Assessment'),
        ('Technical Round', 'Technical Round'),
        ('HR Round', 'HR Round'),
        ('Selected', 'Selected'),
        ('Waiting For Offer', 'Waiting For Offer'),
        ('Offer Released', 'Offer Released'),
        ('Onboarding', 'Onboarding'),
        ('Welcome Mail', 'Welcome Mail'),
        ('Training', 'Training'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)

    total_fee = models.IntegerField()
    paid_amount = models.IntegerField()
    pending_amount = models.IntegerField()

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.name