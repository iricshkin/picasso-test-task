from drf_yasg import openapi
from rest_framework import status


authentication_error_schema = openapi.Schema(
    type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)
)


error_responses = {
    status.HTTP_204_NO_CONTENT: openapi.Response(
        description="Successful request. Object successfully deleted."
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Response(
        description="Error: Bad Request.",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"errors": openapi.Schema(type=openapi.TYPE_STRING)},
        ),
        examples={
            "application/json": {"errors": "Invalid data provided. Check the fields."}
        },
    ),
    status.HTTP_404_NOT_FOUND: openapi.Response(
        description="Error: NOT_FOUND",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"detail": openapi.Schema(type=openapi.TYPE_STRING)},
        ),
        examples={
            "application/json": {
                "detail": "Record not found. Invalid activation data.",
            }
        },
    ),
    status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
        description="Error: INTERNAL_SERVER_ERROR",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"error": openapi.Schema(type=openapi.TYPE_STRING)},
        ),
        examples={
            "application/json": {
                "detail": "Internal server error occurred.",
            }
        },
    ),
}
