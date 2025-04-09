from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    courses = models.CharField(max_length=255)  # You can use a many-to-many relationship here if needed
    td = models.IntegerField()  # Number of TD sessions
    tp = models.IntegerField()  # Number of TP sessions
    coef = models.FloatField()  # Coefficient
    max_surveillance_hours = models.IntegerField()  # Maximum number of hours a professor can supervise
    available = models.BooleanField(default=True)  # If the professor is available

    def __str__(self):
        return self.name


class Session(models.Model):
    session_id = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    professor_1 = models.ForeignKey(Professor, related_name="sessions_professor_1", on_delete=models.CASCADE)
    professor_2 = models.ForeignKey(Professor, related_name="sessions_professor_2", on_delete=models.CASCADE)

    def __str__(self):
        return f"Session {self.session_id} on {self.date} at {self.time}"


class Formula(models.Model):
    formula = models.TextField()

    def __str__(self):
        return self.formula
