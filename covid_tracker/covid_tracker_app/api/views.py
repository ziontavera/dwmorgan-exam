import csv
from datetime import datetime

from django.db import transaction
from django.db.models import Sum

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from covid_tracker_app.models import CovidObservation


class CovidTrackerView(APIView):
    def post(self, request):
        with open("covid_19_data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                observation_date = datetime.strptime(row["ObservationDate"], "%m/%d/%Y")
                province = row["Province/State"]
                country = row["Country/Region"]
                confirmed = round(float(row["Confirmed"]))
                deaths = round(float(row["Deaths"]))
                recovered = round(float(row["Recovered"]))
                with transaction.atomic():
                    instance = CovidObservation.objects.create(
                        observation_date=observation_date,
                        province=province,
                        country=country,
                        confirmed=confirmed,
                        deaths=deaths,
                        recovered=recovered,
                    )
                    instance.save()

        return Response(
            {"message": "CSV Parsed and Saved"}, status=status.HTTP_201_CREATED
        )

    def get(self, request):
        observation_date = datetime.strptime(
            request.data["observation_date"], "%Y/%m/%d"
        )
        max_results = int(request.data["max_results"])
        data = (
            CovidObservation.objects.filter(observation_date=observation_date)
            .values("country")
            .annotate(
                confirmed=Sum("confirmed"),
                deaths=Sum("deaths"),
                recovered=Sum("recovered"),
            )
            .order_by("-confirmed")[:max_results]
        )

        response = {
            "observation_date": request.data["observation_date"],
            "countries": [],
        }

        for entry in data:
            response["countries"].append(
                {
                    "country": entry["country"],
                    "confirmed": entry["confirmed"],
                    "deaths": entry["deaths"],
                    "recovered": entry["recovered"],
                }
            )

        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        with transaction.atomic():
            CovidObservation.objects.all().delete()

        return Response({"message": "OK"}, status=status.HTTP_200_OK)
