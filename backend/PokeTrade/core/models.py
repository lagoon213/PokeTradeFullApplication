from django.db import models
from django.core.validators import RegexValidator

class Card(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('double rare', 'Double Rare'),
        ('ace spec rare', 'Ace Spec Rare'),
        ('illustration rare', 'Illustration Rare'),
        ('ultra rare', 'Ultra Rare'),
        ('special illustration rare', 'Special Illustration Rare'),
        ('hyper rare', 'Hyper Rare'),
        ('shiny rare', 'Shiny Rare'),
        ('shiny ultra rare', 'Shiny Ultra Rare'),
        ('black star promo', 'Black Star Promo'),
        ('black white rare', 'Black White Rare'),
    ]
    number_validator = RegexValidator(
        regex=r'^\d+/\d+$',  # pattern: één of meer cijfers, /, één of meer cijfers
        message='Number must be in format X/Y (e.g., 171/86)'
    )
    number = models.CharField(
        max_length=10,
        validators=[number_validator],
        help_text='Format: X/Y, e.g., 171/86'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    set_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rarity = models.CharField(
        max_length=50,
        choices=RARITY_CHOICES,
        default='common',  # geldige default
    )
    image_url = models.URLField()
    grading = models.CharField(max_length=10, blank=True, null=True)
    gradingCompany = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name