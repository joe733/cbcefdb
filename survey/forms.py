# from json import load
from django import forms
from django.forms import fields
from .models import Survey, questions

form_fields = []
answers = q_atrb = dict()

# with open(file="survey/assets/questions.json", mode='r', encoding="utf-8") as jfp:
#     questions = load(jfp)


def load_questions():
    for idx in range(1, 11):
        q_atrb = questions[str(idx)]
        form_fields.append(q_atrb["label"])

        if q_atrb["element_type"] == "textbox":
            if q_atrb["input_type"] in ["text_input", "text_area"]:
                answers[q_atrb["label"]] = forms.CharField(
                    label=q_atrb["label"],
                    max_length=80,
                    required=True
                )
            if q_atrb["input_type"] == "number_input":
                answers[q_atrb["label"]] = forms.IntegerField(
                    label=q_atrb["label"],
                    min_value=q_atrb["valminNumeric"],
                    max_value=q_atrb["valmaxNumeric"]
                )

        if q_atrb["element_type"] == "radio":
            answers[q_atrb["label"]] = forms.ChoiceField(
                label=q_atrb["label"],
                choices=tuple(
                    [(idx, val) for idx, val in enumerate(q_atrb["optionValues"])]),
                widget=forms.RadioSelect
            )


class IndividualModel(forms.ModelForm):
    class Meta:
        model = Survey
        fields = form_fields


class IndividualForm(forms.Form):
    load_questions()

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
