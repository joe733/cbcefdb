from os import name
from django.db import models
from json import load

form_fields = []
answers = q_atrb = dict()

with open(file="survey/assets/questions.json", mode='r', encoding="utf-8") as jfp:
    questions = load(jfp)


# Create your models here.
class Survey(models.Model):
    for idx in range(1, 11):
        q_atrb = questions[str(idx)]
        form_fields.append(q_atrb["label"])

        if q_atrb["element_type"] == "textbox":
            if q_atrb["input_type"] in ["text_input", "text_area"]:
                answers[q_atrb["label"]] = models.CharField(
                    name=q_atrb["label"])
            if q_atrb["input_type"] == "number_input":
                answers[q_atrb["label"]] = models.IntegerField(
                    name=q_atrb["label"])

        if q_atrb["element_type"] == "radio":
            answers[q_atrb["label"]] = models.CharField(
                choices=[(idx, val) for idx, val in enumerate(q_atrb["optionValues"])])

    def __str__(self):
        return q_atrb["0"]["label"]
