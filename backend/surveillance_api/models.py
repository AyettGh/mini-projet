from django.db import models

<<<<<<< HEAD
=======
class Formula(models.Model):
    formula = models.CharField(max_length=255, default="(courses + td + tp * 0.75) * coef")

    def __str__(self):
        return self.formula


>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
class Professor(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
<<<<<<< HEAD
    courses = models.CharField(max_length=255)  # You can use a many-to-many relationship here if needed
    td = models.IntegerField()  # Number of TD sessions
    tp = models.IntegerField()  # Number of TP sessions
    coef = models.FloatField()  # Coefficient
    max_surveillance_hours = models.IntegerField()  # Maximum number of hours a professor can supervise
    available = models.BooleanField(default=True)  # If the professor is available
=======
    courses = models.FloatField(default=0)
    td = models.FloatField(default=0)
    tp = models.FloatField(default=0)
    coef = models.FloatField(default=0)
    max_surveillance_hours = models.FloatField(default=0)
    available = models.BooleanField(default=True)
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480

    def __str__(self):
        return self.name


class Session(models.Model):
<<<<<<< HEAD
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
=======
    session_id = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    professor_1 = models.ForeignKey(Professor, related_name="sessions_as_prof_1", null=True, on_delete=models.SET_NULL)
    professor_2 = models.ForeignKey(Professor, related_name="sessions_as_prof_2", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.session_id} - {self.date} {self.time}"
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
