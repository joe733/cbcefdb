from django.db import models
from datetime import date

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Survey(models.Model):
    # Question 1 - 10
    q_01 = models.CharField(
        name="ഔദ്യോഗിക പേര് | Full Name", max_length=100, default="")
    q_02 = models.CharField(
        name="വിളിപ്പേരുകൾ പേര് | Aliases / Nicknames", max_length=100, default="")
    q_03 = models.CharField(name="ലിംഗഭേദം | Gender", choices=(
        (1, "തിരഞ്ഞെടുക്കുക | Select"),
        (2, "പുരുഷന്‍ | Male"),
        (3, "സ്ത്രീ | Female"),
        (4, "ഭിന്ന ലിംഗം | Other"),
    ), max_length=60, default="തിരഞ്ഞെടുക്കുക | Select")
    q_04 = models.DateField(name="ജനന തിയതി | Date of Birth",
                            default=date(day=11, month=11, year=1111))
    q_05 = models.CharField(name="ബന്ധം | Relation", choices=(
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
        name="പിതാവിന്‍റെ പേര് | Father's Name", max_length=100, default="")
    q_07 = models.CharField(
        name="മാതാവിന്‍റെ പേര് | Mother's Name", max_length=100, default="")
    q_08 = models.CharField(
        name="ഗാർഡിയന്റെ പേര് | Guardian's Name", max_length=100, default="")
    q_09 = PhoneNumberField(name="മൊബൈല്‍ഫോണ്‍ നമ്പര്‍ | Mobile Number")
    q_10 = models.EmailField(name="ഇ മെയില്‍ അഡ്രസ്‌ | Email Address",
                             max_length=60, default="")

    # Question 11 - 20
    q_11 = models.CharField(name="ഉയർന്ന വിദ്യാഭ്യാസം | Highest Education", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "10-ന് താഴെ | Below 10th"),
        (3, "10-ാം ക്ലാസ്സ് | 10th Class"),
        (4, "12-ാം ക്ലാസ്സ് | 12th Class"),
        (5, "ഡിപ്ലോമ | Diploma"),
        (6, "ബിരുദം | Graduate"),
        (7, "പോസ്റ്റ് ഗ്രാജ്വേറ്റ് | Post Graduate"),
        (8, "ഡോക്ടറേറ്റ് | Doctorate")
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_12 = models.CharField(name="വിവാഹ നില | Marital Status", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "അവിവാഹിതന്‍ / അവിവാഹിത | Single"),
        (3, "വിവാഹിതന്‍ / വിവാഹിത Married "),
        (4, "വിധവ / വിഭാര്യന്‍ Widow / Widower"),
        (5, "Second marriage"),
        (6, "Third marriage"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_13 = models.DateField(name="വിവാഹ തിയതി | Date of Marriage",
                            default=date(day=11, month=11, year=1111))
    q_14 = models.CharField(name="ജോലി / തൊഴില്‍ | Job / Employment", choices=(
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
    q_15 = models.CharField(name="പ്രതിമാസ വരുമാനം | Monthly Income", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "below 10000 താഴെ"),
        (3, "10000 - 30000"),
        (4, "30000 - 60000"),
        (5, "Above 60000 മുകളിൽ"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_16 = models.CharField(name="വീട് | House", choices=(
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
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")
    q_17_02 = models.CharField(
        name="വീടിന്റെ പേര് | House Name", max_length=60, default="")
    q_17_03 = models.CharField(
        name="വീട് / വാർഡ് നമ്പർ | House / Ward No", max_length=60, default="")
    q_17_04 = models.CharField(
        name="റോഡ് / സ്ട്രീറ്റ് പേര് | Road / Street Name", max_length=60, default="")
    q_17_05 = models.CharField(
        name="വില്ലേജ് / പോസ്റ്റ് ഓഫീസ് | Village / Post Office", max_length=60, default="")
    q_17_06 = models.CharField(
        name="താലൂക്ക് / ജില്ല | Taluk / District", max_length=60, default="")
    q_17_07 = models.CharField(
        name="സംസ്ഥാനം | State", max_length=60, default="")
    q_17_08 = models.IntegerField(
        name="പിൻ കോഡ് | Pincode", default=0)
    ## >> സ്ഥിരമായ അഡ്രസ്‌ | Permanent Address << ##
    q_18 = models.CharField(name="പൗരതം | Citizenship",
                            max_length=60, default="")
    q_19 = models.IntegerField(
        name="ആധാര്‍ നമ്പര്‍ | Aadhar Number", default=0)
    q_20 = models.CharField(name="റേഷന്‍ കാര്‍ഡ് | Ration Card", choices=(
        (1, "തെരഞ്ഞെടുക്കുക | Select"),
        (2, "മഞ്ഞ | Yellow"),
        (3, "പിങ്ക് | Pink"),
        (4, "നീല | Blue"),
        (5, "വെള്ള | White"),
        (6, "കാർഡ് ഇല്ല | No Card"),
    ), max_length=60, default="തെരഞ്ഞെടുക്കുക | Select")

    def __str__(self):
        return self.q_01
