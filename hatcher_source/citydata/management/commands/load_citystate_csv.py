# In citydata/management/commands/load_city_data.py
import csv
from django.core.management.base import BaseCommand
from citydata.models import CityState  # Adjust the path to your model

class Command(BaseCommand):
    help = "Load city and state data from CSV"

    def handle(self, *args, **kwargs):
        with open("R:\\data_scrapping\\states_and_cities.csv", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                CityState.objects.create(city=row['City'], state=row['State'])
        self.stdout.write("Data loaded successfully!")
