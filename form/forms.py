from json import load
from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

with open(file="cbcefdb/form/questions.json", mode='r', encoding="utf-8") as jfp:
    questions = load(jfp)

answers = dict()


def form_definition():
    for idx in range(1, len(questions)+1):
        q_atrb = questions[str(idx)]

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


class MainForm(forms.Form):

    fd = form_definition

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-mainForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
