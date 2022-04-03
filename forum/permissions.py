from rest_framework.permissions import BasePermission
from rest_framework import status
import requests
import os


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.META.get("REQUEST_METHOD") == "GET":
            return True

        token = (
            request.META.get("HTTP_AUTHORIZATION")
            or request.META.get("Authorization")
            or view.headers.get("Authorization")
        )
        is_authenticated = self.is_authenticated(token)

        return is_authenticated

    def is_authenticated(self, token):
        url = os.environ.get("USER_SERVICE_API_URL") + "profile/"
        user_response = requests.get(
            url,
            headers={"Authorization": token, "Content-Type": "application/json"},
        )

        return user_response.status_code == status.HTTP_200_OK
