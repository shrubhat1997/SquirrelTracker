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
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    Color_Choices = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
    )
    Primary_Fur_Color = models.CharField(
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
    Running = models.BooleanField(
        help_text=_('Is the squirrel running?'),default=False)
    Chasing = models.BooleanField(
        help_text=_('Is the squirrel chasing?'),default=False)
    Climbing = models.BooleanField(
        help_text=_('Is the squirrel climbing?'),default=False)
    Eating = models.BooleanField(
        help_text=_('Is the squirrel eating?'),default=False)
    Foraging = models.BooleanField(
        help_text=_('Is the squirrel foraging?'),default=False)
    Other_Activities = models.TextField(
        max_length = 100,
        help_text=_('Other activites'),
        null=True,
        blank=True,
    )
    Kuks = models.BooleanField(
        help_text=_('Is the squirrel kuking?'), default=False)
    Quaas = models.BooleanField(
        help_text=_('Is the squirrel quaaing?'), default=False)
    Moans = models.BooleanField(
        help_text=_('Is the squirrel moaning?'), default=False)
    Tail_Flags = models.BooleanField(
        help_text=_('Does the squirrel have a tail flag?'), default=False)
    Tail_Twitches = models.BooleanField(
        help_text=_('Is the squirrel\'s tail twitching?'), default=False)
    Approaches = models.BooleanField(
        help_text=_('Did the squirrel approach you?'), default=False)
    Indifferent = models.BooleanField(
        help_text=_('Was the squirrel indifferent to you?'), default=False)
    Runs_From = models.BooleanField(
        help_text=_('Did the squirrel run from you?'), default=False)

    def __str__(self) :
        return self.Unique_Squirrel_ID
