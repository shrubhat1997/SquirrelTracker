from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

class Squirrels(models.Model) :
    X = models.FloatField(
        help_text=_('Longitude'),
    )

    Y = models.FloatField(
        help_text=_('Latitude'),
    )    
    Unique_Squirrel_ID = models.CharField(
        max_length=50,
        help_text=_('Unique Squirrel ID'),
        primary_key=True,
        default=None,
    )
    PM = 'PM'
    AM = 'AM'
    Shift_choices  = (
        (PM,'PM'),
        (AM,'AM'),
    )
    Shift = models.CharField(
        max_length=2,
        choices=Shift_choices,
    )
    Date = models.DateField(
        help_text=_('Date'),
        blank=True,
    )
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Age_choices = (
        (Adult,'Adult'),
        (Juvenile,'Juvenile'),
    )
    Age = models.CharField(
        max_length=50,
        choices=Age_choices,
        blank=True,
        null=True,
    )
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    Color_Choices = (
        (GRAY,'Gray'),
        (Cinnamon,'Cinnamon'),
        (Black,'Black'),
    )
    Primary_Fur_color = models.CharField(
        help_text=_('Primary Fur Color'),
        max_length=50,
        choices=Color_Choices,
        blank=True,
        null=True,
    )
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'

    Location_Choices = (
        (Ground_Plane,'Ground Plane'),
        (Above_Ground,'Above Ground'),
    )
    Location = models.CharField(
        help_text=_('Location'),
        max_length=50,
        choices=Location_Choices,
        blank=True,
        null=True,
    )
    Specific_Location = models.CharField(
        help_text=_('Specific_Location'),
        max_length=255,
        blank=True,
        null=True,
    )
    running = models.BooleanField(
        help_text=_('Is the squirrel running?'),default=False)
    chasing = models.BooleanField(
        help_text=_('Is the squirrel chasing?'),default=False)
    climbing = models.BooleanField(
        help_text=_('Is the squirrel climbing?'),default=False)
    eating = models.BooleanField(
        help_text=_('Is the squirrel eating?'),default=False)
    foraging = models.BooleanField(
        help_text=_('Is the squirrel foraging?'),default=False)
    other_activites = models.TextField(
        max_length = 100
        help_text=_('Other activites'),
        null=True
        blank=True
    )
    kuks = models.BooleanField(
        help_text=_('Is the squirrel kuking?'), default=False)
    quaas = models.BooleanField(
        help_text=_('Is the squirrel quaaing?'), default=False)
    moans = models.BooleanField(
        help_text=_('Is the squirrel moaning?'), default=False)
    tail_flags = models.BooleanField(
        help_text=_('Does the squirrel have a tail flag?'), default=False)
    tail_twitches = models.BooleanField(
        help_text=_('Is the squirrel\'s tail twitching?'), default=False)
    approaches = models.BooleanField(
        help_text=_('Did the squirrel approach you?'), default=False)
    indifferent = models.BooleanField(
        help_text=_('Was the squirrel indifferent to you?'), default=False)
    runs_from = models.BooleanField(
        help_text=_('Did the squirrel run from you?'), default=False)

    def __str__(self) :
        return self.Unique_Squirrel_ID

    def get_urls(self) :
        return ''
