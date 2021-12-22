from django.db import models
from django.utils.timezone import now

# Create your models here.


# STATUS_CHOICES = [
#     ("Hiring", "Hiring"),
#     ("Stable", "Stable"),
#     ("Contract", "Contract")
# ]


class Company(models.Model):
    class STATUS_CHOICES(models.TextChoices):
        Hiring = "Hiring"
        Hiring_Freeze = "Hiring_Freeze"
        Stable = "Stable"
        Contract = "Contract"

    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    status = models.CharField(
        max_length=20,
        # choices=STATUS_CHOICES
        choices=STATUS_CHOICES.choices,
        default=STATUS_CHOICES.Stable,
    )
    updated = models.DateTimeField(default=now, auto_now=False, auto_now_add=False, blank=True, null=True)

    notest = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Email(models.Model):
    e_from = models.EmailField(max_length=254)
    e_to = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"email subject :{self.subject}" + "from :{self.e_from} to :{self.e_to} and content is :{self.content}"
