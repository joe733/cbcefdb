from datetime import date
from django.db import models
from django.urls import reverse
# from django.forms.models import ModelForm
from phonenumber_field.modelfields import PhoneNumberField


class Family(models.Model):
    fam_name = models.CharField(
        verbose_name="കുടുംബ പേര് | Family Name", null=False, blank=False, max_length=100, default="")
    nofm = models.IntegerField(
        verbose_name="അംഗങ്ങളുടെ എണ്ണം | Number of members", default=1)

    def get_absolute_url(self):
        return reverse(viewname='survey:family_info', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.fam_name

    class Meta:
        verbose_name_plural = "Families"


class Person(models.Model):
    fly = models.ForeignKey(
        verbose_name="കുടുംബ പേര് | Family Name", to=Family, null=False, blank=False, on_delete=models.CASCADE, related_name="family_name")
    # Question 1 - 10
    q_01 = models.CharField(
        verbose_name="01. ഔദ്യോഗിക പേര് | Full Name", null=False, blank=False, max_length=100, default="")
    q_02 = models.TextField(
        verbose_name="02. വിളിപ്പേരുകൾ പേര് | Aliases / Nicknames", blank=True, max_length=200, default="")
    q_03 = models.CharField(verbose_name="03. ലിംഗഭേദം | Gender", choices=(
        ("1", "തിരഞ്ഞെടുക്കുക | Select"),
        ("2", "പുരുഷന്‍ | Male"),
        ("3", "സ്ത്രീ | Female"),
        ("4", "ഭിന്ന ലിംഗം | Other"),
    ), max_length=60, default="തിരഞ്ഞെടുക്കുക | Select")
    q_04 = models.DateField(verbose_name="04. ജനന തിയതി | Date of Birth",
                            default=date(day=11, month=11, year=1111))
    q_05 = models.CharField(verbose_name="05. ബന്ധം | Relation", choices=(
        ("1", "തിരഞ്ഞെടുക്കുക | Select"),
        ("2", "പിതാവ് | Father"),
        ("3", "മാതാവ് | Mother"),
        ("4", "ഭര്‍ത്താവ് | Husband"),
        ("5", "ഭാര്യ | Wife"),
        ("6", "മകന്‍ | Son"),
        ("7", "മകള്‍ | Daughter"),
        ("8", "സഹോദരന്‍ | Brother"),
        ("9", "സഹോദരി | Sister"),
    ), max_length=60, default="തിരഞ്ഞെടുക്കുക | Select")
    q_06 = models.CharField(
        verbose_name="06. പിതാവിന്‍റെ പേര് | Father's Name", blank=True, max_length=100, default="")
    q_07 = models.CharField(
        verbose_name="07. മാതാവിന്‍റെ പേര് | Mother's Name", blank=True, max_length=100, default="")
    q_08 = models.CharField(
        verbose_name="08. ഗാർഡിയന്റെ പേര് | Guardian's Name", blank=True, max_length=100, default="")
    q_09 = PhoneNumberField(
        verbose_name="09. മൊബൈല്‍ഫോണ്‍ നമ്പര്‍ | Mobile Number", blank=True)
    q_10 = models.EmailField(verbose_name="10. ഇ മെയില്‍ അഡ്രസ്‌ | Email Address",
                             blank=True, max_length=60, default="")

    # Question 11 - 20
    q_11 = models.CharField(verbose_name="11. ഉയർന്ന വിദ്യാഭ്യാസം | Highest Education", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "10-ന് താഴെ | Below 10th"),
        ("3", "10-ാം ക്ലാസ്സ് | 10th Class"),
        ("4", "12-ാം ക്ലാസ്സ് | 12th Class"),
        ("5", "ഡിപ്ലോമ | Diploma"),
        ("6", "ബിരുദം | Graduate"),
        ("7", "പോസ്റ്റ് ഗ്രാജ്വേറ്റ് | Post Graduate"),
        ("8", "ഡോക്ടറേറ്റ് | Doctorate")
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_12 = models.CharField(verbose_name="12. വിവാഹ നില | Marital Status", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "അവിവാഹിതന്‍ / അവിവാഹിത | Single"),
        ("3", "വിവാഹിതന്‍ / വിവാഹിത Married "),
        ("4", "വിധവ / വിഭാര്യന്‍ Widow / Widower"),
        ("5", "Second marriage"),
        ("6", "Third marriage"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_13 = models.DateField(verbose_name="13. വിവാഹ തിയതി | Date of Marriage",
                            default=date(day=11, month=11, year=1111))
    q_14 = models.CharField(verbose_name="14. ജോലി / തൊഴില്‍ | Job / Employment", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "ബാധകമല്ല | Not applicable"),
        ("3", "ദിവസ കൂലി | Daily Wages"),
        ("4", "ശുശ്രൂഷ | Ministry"),
        ("5", "ഗവണ്‍മന്റ് ജോലി | Government service"),
        ("6", "പ്രൈവറ്റ് ജോലി | Private firm"),
        ("7", "വിദേശത്തു ജോലി | Overseas Job"),
        ("8", "ബിസിനസ് | Business"),
        ("9", "ക്യഷി | Agriculture / Plantation"),
        ("10", "കന്നുകാലി കൃഷി | Animal farming"),
        ("11", "ഡോക്ടര്‍ | Doctor"),
        ("12", "നേഴ്‌സ് | Nurse"),
        ("13", "മെഡിക്കൽ (മറ്റുള്ളവ) | Medical (Others)"),
        ("14", "അധ്യാപകന്‍ | Teacher"),
        ("15", "വക്കീൽ | Advocate"),
        ("16", "എൻജിനിയർ | Engineer"),
        ("17", "ബാങ്ക് ജോലി | Bank Employee"),
        ("18", "ഡ്രൈവിംഗ് | Driving Job"),
        ("19", "തൊഴിലുറപ്പ് | NREGA"),
        ("20", "സ്വയം തൊഴില്‍ | Self Employed"),
        ("21", "വീട്ടമ്മ | Home maker"),
        ("22", "വിശ്രമ ജീവിതം | Retired"),
        ("23", "ജോലി ഇല്ല | Not working"),
        ("24", "വിദ്യാർത്ഥി | Student"),
        ("25", "മറ്റുള്ളവ | Others"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_15 = models.CharField(verbose_name="15. പ്രതിമാസ വരുമാനം | Monthly Income", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "below 10000 താഴെ"),
        ("3", "10000 - 30000"),
        ("4", "30000 - 60000"),
        ("5", "Above 60000 മുകളിൽ"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_16 = models.CharField(verbose_name="16. വീട് | House", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "സ്വന്തം വീട് | Own House"),
        ("3", "വാടകയ്ക്ക് | Rented"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    ## >> സ്ഥിരമായ അഡ്രസ്‌ | Permanent Address << ##
    q_17_01 = models.CharField(verbose_name="റഫറൻസ് | Reference", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "W/o"),
        ("3", "S/o"),
        ("4", "D/o"),
    ), max_length=60, default="17a. തെരഞ്ഞെടുക്കുക | Select")
    q_17_02 = models.CharField(
        verbose_name="17b. വീടിന്റെ പേര് | House Name", blank=True, max_length=60, default="")
    q_17_03 = models.CharField(
        verbose_name="17c. വീട് / വാർഡ് നമ്പർ | House / Ward No", blank=True, max_length=60, default="")
    q_17_04 = models.CharField(
        verbose_name="17d. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", blank=True, max_length=60, default="")
    q_17_05 = models.CharField(
        verbose_name="17e. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", blank=True, max_length=60, default="")
    q_17_06 = models.CharField(
        verbose_name="17f. താലൂക്ക് / ജില്ല | Taluk / District", blank=True, max_length=60, default="")
    q_17_07 = models.CharField(
        verbose_name="17g. സംസ്ഥാനം | State", blank=True, max_length=60, default="")
    q_17_08 = models.IntegerField(
        verbose_name="17h. പിൻ കോഡ് | Pincode", default=0)
    ## >> സ്ഥിരമായ അഡ്രസ്‌ | Permanent Address << ##
    q_18 = models.CharField(verbose_name="18. പൗരതം | Citizenship",
                            blank=True, max_length=60, default="")
    q_19 = models.IntegerField(
        verbose_name="19. ആധാര്‍ നമ്പര്‍ | Aadhar Number", default=0)
    q_20 = models.CharField(verbose_name="20. റേഷന്‍ കാര്‍ഡ് | Ration Card", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "മഞ്ഞ | Yellow"),
        ("3", "പിങ്ക് | Pink"),
        ("4", "നീല | Blue"),
        ("5", "വെള്ള | White"),
        ("6", "കാർഡ് ഇല്ല | No Card"),
    ), blank=True, max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")

    # Question 21 - 30
    q_21 = models.CharField(verbose_name="21. പാസ്പോര്‍ട്ട്‌ | Passport", choices=(
        ("1", "തെരഞ്ഞെടുക്കുക | Select"),
        ("2", "ഉണ്ട് | Yes"),
        ("3", "ഇല്ല | No"),
    ), blank=True, max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_22 = models.DateField("22. രക്ഷിക്കപ്പെട്ട തിയതി | Date of Salvation", default=date(
        day=11, month=11, year=1111))
    q_23 = models.DateField("23. സ്നാനപ്പെട്ട തിയതി | Date of Baptism", default=date(
        day=11, month=11, year=1111))
    q_24 = models.TextField(
        verbose_name="24. ഈ വിശ്വാസത്തിലേക്ക് വന്നപ്പോഴത്തെ സഭ (മാതൃ സഭ) | Church in which you were saved (Parent Church)", blank=True, max_length=200, default="")
    q_25 = models.TextField(
        verbose_name="25. സ്നാനം നടത്തിയ സ്ഥാനീയ സഭ | Church in which you were baptized", blank=True, max_length=200, default="")
    q_26 = models.TextField(
        verbose_name="26. വിവാഹം നടത്തിയ സ്ഥാനീയ സഭ | Church in which you were married", blank=True, max_length=200, default="")
    q_27 = models.TextField(
        verbose_name="27. ഈ വിശ്വാസത്തിലേക്ക് വരുന്നതിന് മുന്‍പ് ഉണ്ടായിരുന്ന വിശ്വാസ പശ്ചാത്തലം | Previous Faith (if any)", blank=True, max_length=200, default="")
    q_28 = models.TextField(
        verbose_name="28. പിതാവിന്‍റെ വിശ്വാസ പശ്ചാത്തലം | Father's faith background", blank=True, max_length=200, default="")
    q_29 = models.TextField(
        verbose_name="29. മാതാവിന്‍റെ വിശ്വാസ പശ്ചാത്തലം | Mother's faith background", blank=True, max_length=200, default="")
    q_30 = models.TextField(
        verbose_name="30. മറ്റു സഭകളില്‍ അംഗം ആയിരുന്നെങ്കില്‍ ആ സഭയുടെ പേരും അവിടെ തുടര്‍ന്ന വര്‍ഷങ്ങളും | Prevous Assembly (if any) & the no. of years you've attended it", blank=True, max_length=200, default="")

    # Question 31 - 40
    q_31 = models.TextField(
        verbose_name="31. നിലവിലെ അസംബ്ലിയിലെ അംഗമായി നിങ്ങൾ പലപ്പോഴും പങ്കെടുത്തിട്ടുള്ള മറ്റ് സഭയുടെ പേര് നൽകുക | Name other churches you've often attended being a member of the current assembly", blank=True, max_length=300, default="")
    ## >> ജനന സ്ഥലം | Place of Birth << ##
    q_32_01 = models.CharField(
        verbose_name="32a. ആശുപത്രി / വീടിന്റെ പേര് | Hospital / House Name", blank=True, max_length=60, default="")
    q_32_02 = models.CharField(
        verbose_name="32b. വീട് / വാർഡ് നമ്പർ | House / Ward No", blank=True, max_length=60, default="")
    q_32_03 = models.CharField(
        verbose_name="32c. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", blank=True, max_length=60, default="")
    q_32_04 = models.CharField(
        verbose_name="32d. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", blank=True, max_length=60, default="")
    q_32_05 = models.CharField(
        verbose_name="32e. താലൂക്ക് / ജില്ല | Taluk / District", blank=True, max_length=60, default="")
    q_32_06 = models.CharField(
        verbose_name="32f. സംസ്ഥാനം | State", blank=True, max_length=60, default="")
    q_32_07 = models.IntegerField(
        verbose_name="32g. പിൻ കോഡ് | Pincode", default=0)
    ## >> ജനന സ്ഥലം | Place of Birth << ##
    q_33 = models.CharField(
        verbose_name="33. ഏതുതരം പ്രവർത്തനം | Kind of Operation", blank=True, max_length=60, default="")
    q_34 = models.CharField(
        verbose_name="34. നിങ്ങളുടെ ജനനം രജിസ്റ്റർ ചെയ്തിട്ടുണ്ടോ? | Is your birth registered", blank=True, max_length=60, default="")
    q_35 = models.TextField(
        verbose_name="35. ജനനം മുതൽ വൈകല്യങ്ങൾ | Disabilities from birth", blank=True, max_length=60, default="")
    q_36 = models.DateField(verbose_name="36. മരണപ്പെട്ട തിയതി | Date of death",
                            blank=True, max_length=60, default=date(day=11, month=11, year=1111))
    q_37 = models.TextField(
        verbose_name="37. മരണ കാരണം | Cause of death", blank=True, max_length=80, default="")
    ## >> ജനന സ്ഥലം | Place of Burial << ##
    q_38_01 = models.CharField(
        verbose_name="38a. ആശുപത്രി / വീടിന്റെ പേര് | Hospital / House Name", blank=True, max_length=60, default="")
    q_38_02 = models.CharField(
        verbose_name="38b. വീട് / വാർഡ് നമ്പർ | House / Ward No", blank=True, max_length=60, default="")
    q_38_03 = models.CharField(
        verbose_name="38c. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", blank=True, max_length=60, default="")
    q_38_04 = models.CharField(
        verbose_name="38d. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", blank=True, max_length=60, default="")
    q_38_05 = models.CharField(
        verbose_name="38e. താലൂക്ക് / ജില്ല | Taluk / District", blank=True, max_length=60, default="")
    q_38_06 = models.CharField(
        verbose_name="38f. സംസ്ഥാനം | State", blank=True, max_length=60, default="")
    q_38_07 = models.IntegerField(
        verbose_name="38g. പിൻ കോഡ് | Pincode", blank=True, default=0)
    ## >> ജനന സ്ഥലം | Place of Burial << ##
    q_39 = models.TextField(
        "39. ശവസംസ്കാര ചടങ്ങ് സഭ കൈകാര്യം ചെയ്യുന്നു | Church handling the burial cerimony", blank=True, max_length=300, default="")

    # File uploads
    q_40 = models.FileField(verbose_name="40. ഫോട്ടോ ഐഡി | Photo ID",
                            upload_to="survey/assets/", blank=True, default="")
    q_41 = models.FileField(verbose_name="41. ജനനത്തിനുള്ള ഡോക്യുമെന്റ് പ്രൂഫ് | Document proof for birth",
                            upload_to="survey/assets/", blank=True, default="")
    q_42 = models.FileField(verbose_name="42. വിലാസത്തിനുള്ള പ്രമാണ തെളിവ് | Document proof for address",
                            upload_to="survey/assets/", blank=True, default="")
    q_43 = models.FileField(verbose_name="43. വിവാഹത്തിനുള്ള രേഖയുടെ തെളിവ് | Document proof for marriage",
                            upload_to="survey/assets/", blank=True, default="")
    q_44 = models.FileField(verbose_name="44. മരണത്തിനുള്ള രേഖ തെളിവ് | Document proof for death",
                            upload_to="survey/assets/", blank=True, default="")

    def get_absolute_url(self):
        return reverse(viewname='survey:family_info', kwargs={'pk': self.fly.pk})

    def __str__(self) -> str:
        return self.q_01

    class Meta:
        verbose_name_plural = "People"


# class PersonCreateModelForm(ModelForm):
#     class Meta:
#         model = Person
#         template_name = "add_person.html"
#         fields = "__all__"
#         # fields = [f"q_{str(i).zfill(2)}" for i in range(1, 17)] + \
#         #     [f"q_17_{str(i).zfill(2)}" for i in range(1, 9)] + \
#         #     [f"q_{i}" for i in range(18, 32)] + \
#         #     [f"q_32_{str(i).zfill(2)}" for i in range(1, 8)] + \
#         #     [f"q_{i}" for i in range(33, 38)] + \
#         #     [f"q_38_{str(i).zfill(2)}" for i in range(1, 8)] + \
#         #     [f"q_{i}" for i in range(39, 45)]
