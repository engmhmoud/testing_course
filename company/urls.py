from django.urls import path
from rest_framework import routers

from .views import CompanyViewSet, EmailView, email, list

app_name = "company"
# cbv : CBV.as_view()
# fbv : property_details
# dynamic url  '/id:int'
router = routers.DefaultRouter()
router.register("companies", viewset=CompanyViewSet, basename="companies")
urlpatterns = [
    path("list", list.as_view(), name="list"),
    path("email", email, name="email"),
    path("EmailView", EmailView.as_view(), name="EmailView"),
]
urlpatterns += router.urls
