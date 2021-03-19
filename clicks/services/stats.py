from infi.clickhouse_orm import F

from clicks.models.click import Clicks, db
from core.models import CustomUser


def get_stats():
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

    return {
        "total": total,
        "user clicks": user_clicks,
        "clicks per date": clicks_per_date,
    }
