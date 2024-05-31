from django.db import models
from django.utils import timezone

class Student(models.Model):

    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    heslo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.mail} {self.heslo}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]



class Odbor(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory"
        ordering = ["nazov"]



class Dostupnost(models.Model):
    stav = models.CharField(max_length=20)
   
    def __str__(self):
        return f"{self.stav}"
    
    class Meta:
        verbose_name = "Dostupnost"
        verbose_name_plural = "Dostupnosti"
        ordering = ["stav"]


class Konzultant(models.Model):
    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    heslo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} {self.mail} {self.heslo}"
    
    class Meta:
        verbose_name = "Konzultant"
        verbose_name_plural = "Konzultanti"
        ordering = ["priezvisko"]


class Tema(models.Model):
    nazov = models.CharField(max_length=50)
    popis = models.CharField(max_length=255)
    konzultant = models.ForeignKey(Konzultant, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.SET_NULL, null=True, blank=True)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nazov} {self.popis} {self.konzultant} {self.student} {self.odbor} {self.dostupnost}"


    class Meta:
        verbose_name = "Téma"
        verbose_name_plural = "Témy"
        ordering = ["dostupnost"]



