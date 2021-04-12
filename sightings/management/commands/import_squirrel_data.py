from django.core.management.base import BaseCommand

from sightings.models import Squirrels

import csv

import datetime

from distutils.util import strtobool

class Command(BaseCommand):

    help = 'Import squirrel sightings data from csv file'


    def add_arguments(self, parser):

        parser.add_argument('path', type=str)


    def handle(self, *args, **kwargs):

        path = kwargs['path']


        try:

            with open(path, encoding='utf-8') as f:

                reader = csv.DictReader(f)

                for i in reader:

                    s = Squirrels(

                        X=i['X'],

                        Y=i['Y'],

                        Unique_Squirrel_ID=i['Unique Squirrel ID'],

                        Shift=i['Shift'],

                        Date=datetime.date(

                            int(i['Date'][-4:]), int(i['Date'][:2]), int(i['Date'][2:4])),

                        Age=i['Age'],

                        Primary_Fur_Color=i['Primary Fur Color'],

                        Location=i['Location'],

                        Specific_Location=i['Specific Location'],

                        Running=strtobool(i['Running']),

                        Chasing=strtobool(i['Chasing']),

                        Climbing=strtobool(i['Climbing']),

                        Eating=strtobool(i['Eating']),

                        Foraging=strtobool(i['Foraging']),

                        Other_Activities=i['Other Activities'],

                        Kuks=strtobool(i['Kuks']),

                        Quaas=strtobool(i['Quaas']),

                        Moans=strtobool(i['Moans']),

                        Tail_Flags=strtobool(i['Tail flags']),

                        Tail_Twitches=strtobool(i['Tail twitches']),

                        Approaches=strtobool(i['Approaches']),

                        Indifferent=strtobool(i['Indifferent']),

                        Runs_From=strtobool(i['Runs from']),

                    )

                    s.save()

        except csv.Error as e:

            print(f'there is something wrong with {reader.line_num}')

