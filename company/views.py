from django.core.mail import send_mail
from django.http.request import QueryDict
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Email
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class list(ListAPIView):
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@api_view(["POST", "GET"])
@parser_classes([JSONParser])
def email(request: Request):
    query_params = request.query_params
    data = request.data
    req_body = request.GET.dict()
    request.DATA.get("email")

    if request.method == "GET":
        pass

    Email.objects.create()
    return Response(
        {"status": "success", "info": "email sent successfully"},
        status=status.HTTP_200_OK,
    )


class EmailView(APIView):
    def get(self, request: Request):
        data = request.data
        id = data.get("id")
        return Response({"id": id, "data": f"{data}"})

    def post(self, request: Request):
        data = request.data
        subject: str = data.get("subject")
        content: str = data.get("v")
        to_email: str = data.get("to_email")
        from_email: str = data.get("from_email")

        res = send_mail(subject=subject, message=content, from_email=from_email, recipient_list=[to_email])
        print(res)
        return Response(
            {"status": "success", "info": "email sent successfully"},
        )
