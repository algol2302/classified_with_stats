from infi.clickhouse_orm import F

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from core.models import CustomUser
from clicks.models.click import Clicks, db


class ClickStatsAPI(APIView):
    """Clicks stats"""

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        # TODO move business logic to services:

        queryset = Clicks.objects_in(db)
        total = queryset.count()

        user_clicks = []
        for row in queryset.aggregate(Clicks.visitor_id, count=F.count()):
            user = CustomUser.objects.get(id=row.visitor_id)
            user_clicks.append({
                "user": user.email,
                "click count": row.count
            })

        clicks_per_date = []
        for row in queryset.aggregate(
            date=F.toDate(Clicks.created_at),
            count=F.count()
        ).group_by('date'):

            clicks_per_date.append({
                "date": row.date,
                "click count": row.count
            })

        values = {
            "total": total,
            "user clicks": user_clicks,
            "clicks per date": clicks_per_date,
        }

        return Response(values)
