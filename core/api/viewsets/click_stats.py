from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from clicks.services import get_stats


class ClickStatsAPI(ViewSet):
    """Clicks stats"""

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def list(self, request, format=None):
        """
        Return the stats.
        """

        stats = get_stats()

        return Response(stats)
