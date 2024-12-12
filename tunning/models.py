from django.db import models


class Discipline(models.Model):
    DisciplineId = models.IntegerField()
    DisciplineName = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Style(models.Model):
    StyleId = models.IntegerField()
    StyleName = models.CharField(max_length=20)
    def __str__(self):
        return self.name  


class Color(models.Model):
    ColorId = models.IntegerField()
    ColorName = models.CharField(max_length=20)
    def __str__(self):
        return self.name  
    

class Tunning(models.Model):
    TunningId = models.IntegerField()
    TunningName = models.CharField(max_length=20)
    TunningDiscipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    TunningStyle = models.ForeignKey(Style, on_delete=models.CASCADE)
    TunningBodyColor = models.ForeignKey(Color, related_name="body_color", on_delete=models.CASCADE)
    TunningDiskColor = models.ForeignKey(Color, related_name="disk_color", on_delete=models.CASCADE)
    TunningIntererColor = models.ForeignKey(Color, related_name="interer_color", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
