from django.db import models
from datetime import date

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Survey(models.Model):
    # Question 1 - 10
    q_01 = models.CharField(
        name="1. ഔദ്യോഗിക പേര് | Full Name", max_length=100, default="")
    q_02 = models.CharField(
        name="2. വിളിപ്പേരുകൾ പേര് | Aliases / Nicknames", max_length=100, default="")
    q_03 = models.CharField(name="3. ലിംഗഭേദം | Gender", choices=(
        (1, "തിരഞ്ഞെടുക്കുക | Select"),
        (2, "പുരുഷന്‍ | Male"),
        (3, "സ്ത്രീ | Female"),
        (4, "ഭിന്ന ലിംഗം | Other"),
    ), max_length=60, default="തിരഞ്ഞെടുക്കുക | Select")
    q_04 = models.DateField(name="4. ജനന തിയതി | Date of Birth",
                            default=date(day=11, month=11, year=1111))
    q_05 = models.CharField(name="5. ബന്ധം | Relation", choices=(
        (1, "തിരഞ്ഞെടുക്കുക | Select"),
        (2, "പിതാവ് | Father"),
        (3, "മാതാവ് | Mother"),
        (4, "ഭര്‍ത്താവ് | Husband"),
        (5, "ഭാര്യ | Wife"),
        (6, "മകന്‍ | Son"),
        (7, "മകള്‍ | Daughter"),
        (8, "സഹോദരന്‍ | Brother"),
        (9, "സഹോദരി | Sister"),
    ), max_length=60, default="തിരഞ്ഞെടുക്കുക | Select")
    q_06 = models.CharField(
        name="6. പിതാവിന്‍റെ പേര് | Father's Name", max_length=100, default="")
    q_07 = models.CharField(
        name="7. മാതാവിന്‍റെ പേര് | Mother's Name", max_length=100, default="")
    q_08 = models.CharField(
        name="8. ഗാർഡിയന്റെ പേര് | Guardian's Name", max_length=100, default="")
    q_09 = PhoneNumberField(name="9. മൊബൈല്‍ഫോണ്‍ നമ്പര്‍ | Mobile Number")
    q_10 = models.EmailField(name="10. ഇ മെയില്‍ അഡ്രസ്‌ | Email Address",
                             max_length=60, default="")

    # Question 11 - 20
    q_11 = models.CharField(name="11. ഉയർന്ന വിദ്യാഭ്യാസം | Highest Education", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "10-ന് താഴെ | Below 10th"),
        (3, "10-ാം ക്ലാസ്സ് | 10th Class"),
        (4, "12-ാം ക്ലാസ്സ് | 12th Class"),
        (5, "ഡിപ്ലോമ | Diploma"),
        (6, "ബിരുദം | Graduate"),
        (7, "പോസ്റ്റ് ഗ്രാജ്വേറ്റ് | Post Graduate"),
        (8, "ഡോക്ടറേറ്റ് | Doctorate")
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_12 = models.CharField(name="12. വിവാഹ നില | Marital Status", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "അവിവാഹിതന്‍ / അവിവാഹിത | Single"),
        (3, "വിവാഹിതന്‍ / വിവാഹിത Married "),
        (4, "വിധവ / വിഭാര്യന്‍ Widow / Widower"),
        (5, "Second marriage"),
        (6, "Third marriage"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_13 = models.DateField(name="13. വിവാഹ തിയതി | Date of Marriage",
                            default=date(day=11, month=11, year=1111))
    q_14 = models.CharField(name="14. ജോലി / തൊഴില്‍ | Job / Employment", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "ബാധകമല്ല | Not applicable"),
        (3, "ദിവസ കൂലി | Daily Wages"),
        (4, "ശുശ്രൂഷ | Ministry"),
        (5, "ഗവണ്‍മന്റ് ജോലി | Government service"),
        (6, "പ്രൈവറ്റ് ജോലി | Private firm"),
        (7, "വിദേശത്തു ജോലി | Overseas Job"),
        (8, "ബിസിനസ് | Business"),
        (9, "ക്യഷി | Agriculture / Plantation"),
        (10, "കന്നുകാലി കൃഷി | Animal farming"),
        (11, "ഡോക്ടര്‍ | Doctor"),
        (12, "നേഴ്‌സ് | Nurse"),
        (13, "മെഡിക്കൽ (മറ്റുള്ളവ) | Medical (Others)"),
        (14, "അധ്യാപകന്‍ | Teacher"),
        (15, "വക്കീൽ | Advocate"),
        (16, "എൻജിനിയർ | Engineer"),
        (17, "ബാങ്ക് ജോലി | Bank Employee"),
        (18, "ഡ്രൈവിംഗ് | Driving Job"),
        (19, "തൊഴിലുറപ്പ് | NREGA"),
        (20, "സ്വയം തൊഴില്‍ | Self Employed"),
        (21, "വീട്ടമ്മ | Home maker"),
        (22, "വിശ്രമ ജീവിതം | Retired"),
        (23, "ജോലി ഇല്ല | Not working"),
        (24, "വിദ്യാർത്ഥി | Student"),
        (25, "മറ്റുള്ളവ | Others"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_15 = models.CharField(name="15. പ്രതിമാസ വരുമാനം | Monthly Income", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "below 10000 താഴെ"),
        (3, "10000 - 30000"),
        (4, "30000 - 60000"),
        (5, "Above 60000 മുകളിൽ"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_16 = models.CharField(name="16. വീട് | House", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "സ്വന്തം വീട് | Own House"),
        (3, "വാടകയ്ക്ക് | Rented"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    ## >> സ്ഥിരമായ അഡ്രസ്‌ | Permanent Address << ##
    q_17_01 = models.CharField(name="റഫറൻസ് | Reference", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "W/o"),
        (3, "S/o"),
        (4, "D/o"),
    ), max_length=60, default="17a. തെരഞ്ഞെടുക്കുക | Select")
    q_17_02 = models.CharField(
        name="17b. വീടിന്റെ പേര് | House Name", max_length=60, default="")
    q_17_03 = models.CharField(
        name="17c. വീട് / വാർഡ് നമ്പർ | House / Ward No", max_length=60, default="")
    q_17_04 = models.CharField(
        name="17d. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", max_length=60, default="")
    q_17_05 = models.CharField(
        name="17e. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", max_length=60, default="")
    q_17_06 = models.CharField(
        name="17f. താലൂക്ക് / ജില്ല | Taluk / District", max_length=60, default="")
    q_17_07 = models.CharField(
        name="17g. സംസ്ഥാനം | State", max_length=60, default="")
    q_17_08 = models.IntegerField(
        name="17h. പിൻ കോഡ് | Pincode", default=0)
    ## >> സ്ഥിരമായ അഡ്രസ്‌ | Permanent Address << ##
    q_18 = models.CharField(name="18. പൗരതം | Citizenship",
                            max_length=60, default="")
    q_19 = models.IntegerField(
        name="19. ആധാര്‍ നമ്പര്‍ | Aadhar Number", default=0)
    q_20 = models.CharField(name="20. റേഷന്‍ കാര്‍ഡ് | Ration Card", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "മഞ്ഞ | Yellow"),
        (3, "പിങ്ക് | Pink"),
        (4, "നീല | Blue"),
        (5, "വെള്ള | White"),
        (6, "കാർഡ് ഇല്ല | No Card"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")

    # Question 21 - 30
    q_21 = models.CharField(name="21. പാസ്പോര്‍ട്ട്‌ | Passport", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "ഉണ്ട് | Yes"),
        (3, "ഇല്ല | No"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_22 = models.DateField("22. രക്ഷിക്കപ്പെട്ട തിയതി | Date of Salvation", default=date(
        day=11, month=11, year=1111))
    q_23 = models.DateField("23. സ്നാനപ്പെട്ട തിയതി | Date of Baptism", default=date(
        day=11, month=11, year=1111))
    q_24 = models.CharField(
        name="24. ഈ വിശ്വാസത്തിലേക്ക് വന്നപ്പോഴത്തെ സഭ (മാതൃ സഭ) | Church in which you were saved (Parent Church)", max_length=200, default="")
    q_25 = models.CharField(
        name="25. സ്നാനം നടത്തിയ സ്ഥാനീയ സഭ | Church in which you were baptized", max_length=200, default="")
    q_26 = models.CharField(
        name="26. വിവാഹം നടത്തിയ സ്ഥാനീയ സഭ | Church in which you were married", max_length=200, default="")
    q_27 = models.CharField(
        name="27. ഈ വിശ്വാസത്തിലേക്ക് വരുന്നതിന് മുന്‍പ് ഉണ്ടായിരുന്ന വിശ്വാസ പശ്ചാത്തലം | Previous Faith (if any)", max_length=200, default="")
    q_28 = models.CharField(
        name="28. പിതാവിന്‍റെ വിശ്വാസ പശ്ചാത്തലം | Father's faith background", max_length=200, default="")
    q_29 = models.CharField(
        name="29. മാതാവിന്‍റെ വിശ്വാസ പശ്ചാത്തലം | Mother's faith background", max_length=200, default="")
    q_30 = models.CharField(
        name="30. മറ്റു സഭകളില്‍ അംഗം ആയിരുന്നെങ്കില്‍ ആ സഭയുടെ പേരും അവിടെ തുടര്‍ന്ന വര്‍ഷങ്ങളും | Prevous Assembly (if any) & the no. of years you've attended it", max_length=200, default="")

    # Question 31 - 40
    q_31 = models.CharField(
        name="31. നിലവിലെ അസംബ്ലിയിലെ അംഗമായി നിങ്ങൾ പലപ്പോഴും പങ്കെടുത്തിട്ടുള്ള മറ്റ് സഭയുടെ പേര് നൽകുക | Name other churches you've often attended being a member of the current assembly", max_length=300, default="")
    ## >> ജനന സ്ഥലം | Place of Birth << ##
    q_32_01 = models.CharField(
        name="32a. ആശുപത്രി / വീടിന്റെ പേര് | Hospital / House Name", max_length=60, default="")
    q_32_02 = models.CharField(
        name="32b. വീട് / വാർഡ് നമ്പർ | House / Ward No", max_length=60, default="")
    q_32_03 = models.CharField(
        name="32c. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", max_length=60, default="")
    q_32_04 = models.CharField(
        name="32d. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", max_length=60, default="")
    q_32_05 = models.CharField(
        name="32e. താലൂക്ക് / ജില്ല | Taluk / District", max_length=60, default="")
    q_32_06 = models.CharField(
        name="32f. സംസ്ഥാനം | State", max_length=60, default="")
    q_32_07 = models.IntegerField(
        name="32g. പിൻ കോഡ് | Pincode", default=0)
    ## >> ജനന സ്ഥലം | Place of Birth << ##
    q_33 = models.CharField(
        name="33. ഏതുതരം പ്രവർത്തനം | Kind of Operation", max_length=60, default="")
    q_34 = models.CharField(
        name="34. നിങ്ങളുടെ ജനനം രജിസ്റ്റർ ചെയ്തിട്ടുണ്ടോ? | Is your birth registered", max_length=60, default="")
    q_35 = models.CharField(
        name="35. ജനനം മുതൽ വൈകല്യങ്ങൾ | Disabilities from birth", max_length=60, default="")
    q_36 = models.DateField(name="36. മരണപ്പെട്ട തിയതി | Date of death",
                            max_length=60, default=date(day=11, month=11, year=1111))
    q_37 = models.CharField(
        name="37. മരണ കാരണം | Cause of death", max_length=80, default="")
    ## >> ജനന സ്ഥലം | Place of Burial << ##
    q_38_01 = models.CharField(
        name="38a. ആശുപത്രി / വീടിന്റെ പേര് | Hospital / House Name", max_length=60, default="")
    q_38_02 = models.CharField(
        name="38b. വീട് / വാർഡ് നമ്പർ | House / Ward No", max_length=60, default="")
    q_38_03 = models.CharField(
        name="38c. റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", max_length=60, default="")
    q_38_04 = models.CharField(
        name="38d. വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", max_length=60, default="")
    q_38_05 = models.CharField(
        name="38e. താലൂക്ക് / ജില്ല | Taluk / District", max_length=60, default="")
    q_38_06 = models.CharField(
        name="38f. സംസ്ഥാനം | State", max_length=60, default="")
    q_38_07 = models.IntegerField(
        name="38g. പിൻ കോഡ് | Pincode", default=0)
    ## >> ജനന സ്ഥലം | Place of Burial << ##
    q_39 = models.CharField(
        "39. ശവസംസ്കാര ചടങ്ങ് സഭ കൈകാര്യം ചെയ്യുന്നു | Church handling the burial cerimony", max_length=80, default="")

    # File uploads
    q_40 = models.FileField(name="40. ഫോട്ടോ ഐഡി | Photo ID",
                            upload_to="survey/assets/", default="")
    q_41 = models.FileField(name="41. ജനനത്തിനുള്ള ഡോക്യുമെന്റ് പ്രൂഫ് | Document proof for birth",
                            upload_to="survey/assets/", default="")
    q_42 = models.FileField(name="42. വിലാസത്തിനുള്ള പ്രമാണ തെളിവ് | Document proof for address",
                            upload_to="survey/assets/", default="")
    q_43 = models.FileField(name="43. വിവാഹത്തിനുള്ള രേഖയുടെ തെളിവ് | Document proof for marriage",
                            upload_to="survey/assets/", default="")
    q_44 = models.FileField(name="44. മരണത്തിനുള്ള രേഖ തെളിവ് | Document proof for death",
                            upload_to="survey/assets/", default="")

    def __str__(self):
        return self.q_01
