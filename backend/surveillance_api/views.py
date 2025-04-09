import pandas as pd
from itertools import combinations
<<<<<<< HEAD

from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Professor, Session
from .utils import calculate_max_hours

<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer


def index(request):
    professors = Professor.objects.all()
    sessions = Session.objects.all()
=======

def index(request):
    professors = Professor.objects.all()  # Retrieve all professors
    sessions = Session.objects.all()  # Retrieve all sessions
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
    context = {
        'professors': professors,
        'sessions': sessions,
    }
    return render(request, 'surveillance_api/index.html', context)


<<<<<<< HEAD
=======
>>>>>>> 4a04a29dd8e8ed24a3f757d5564cfb98af3520ea
class UploadExcelView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
=======
# API view to upload an Excel file
class UploadExcelView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            df = pd.read_excel(file)
<<<<<<< HEAD
            required_columns = ["Nom Et Prénom Enseignant", "Département", "Grade", "Cours", "TD", "TP", "coef"]
            missing_columns = [col for col in required_columns if col not in df.columns]

            if missing_columns:
                return Response({"error": f"Missing columns: {', '.join(missing_columns)}"}, status=400)
=======

            # Replace NaN or missing values with 0 for numeric columns
            numeric_columns = ["Cours", "TD", "TP", "coef"]
            df[numeric_columns] = df[numeric_columns].fillna(0)
>>>>>>> 4a04a29dd8e8ed24a3f757d5564cfb98af3520ea

            for _, row in df.iterrows():
                Professor.objects.create(
                    name=row["Nom Et Prénom Enseignant"],
                    department=row["Département"],
                    grade=row["Grade"],
                    courses=row["Cours"],
                    td=row["TD"],
                    tp=row["TP"],
                    coef=row["coef"],
                    max_surveillance_hours=calculate_max_hours(row),
                    available=True,
                )
<<<<<<< HEAD
            return redirect('surveillance_api:success')
=======
            return redirect('surveillance_api:success')  # Redirect to success page after upload
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
        except Exception as e:
            return Response({"error": str(e)}, status=500)


<<<<<<< HEAD
class UpdateAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]

=======
# API view to update the availability of professors
class UpdateAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]


>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
    def post(self, request):
        professor_id = request.data.get("id")
        available = request.data.get("available")

        try:
            professor = Professor.objects.get(id=professor_id)
            professor.available = available
            professor.save()
            return Response({"message": "Availability updated successfully!"}, status=200)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found"}, status=404)


<<<<<<< HEAD
=======
# API view to assign sessions to professors
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
class AssignSessionsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        professors = list(Professor.objects.filter(available=True).exclude(grade="Chef de Département"))
        sessions = Session.objects.all()

        assigned_professors = set()
        for session in sessions:
            for prof1, prof2 in combinations(professors, 2):
                if (prof1.max_surveillance_hours > 0 and
                        prof2.max_surveillance_hours > 0 and
                        prof1.id not in assigned_professors and
                        prof2.id not in assigned_professors):

                    session.professor_1 = prof1
                    session.professor_2 = prof2
                    session.save()

                    prof1.max_surveillance_hours -= 1
                    prof2.max_surveillance_hours -= 1
                    prof1.save()
                    prof2.save()

                    assigned_professors.add(prof1.id)
                    assigned_professors.add(prof2.id)
                    break

        return Response({"message": "Sessions assigned successfully!"}, status=200)


<<<<<<< HEAD
=======
# API view to generate a PDF schedule of sessions
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
class GeneratePDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
<<<<<<< HEAD
        sessions = Session.objects.all()
        if not sessions.exists():
            return Response({"error": "No sessions found"}, status=404)

=======
        # Step 1: Query all sessions
        sessions = Session.objects.all()

        # Step 2: Check if sessions exist
        if not sessions.exists():
            return HttpResponse("No sessions found!", status=404)

        # Step 3: Generate PDF
>>>>>>> 4a04a29dd8e8ed24a3f757d5564cfb98af3520ea
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="surveillance_schedule.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.setFont("Helvetica", 12)

        y = 750
        for session in sessions:
            p.drawString(50, y, f"Session: {session.session_id}, Date: {session.date}, Time: {session.time}")
            p.drawString(50, y - 20, f"Professors: {session.professor_1}, {session.professor_2}")
            y -= 40
            if y < 50:
                p.showPage()
                y = 750

        p.save()
        return response
<<<<<<< HEAD


class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
=======
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
