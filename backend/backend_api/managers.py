from django.db.models import Manager


class SoftDeleteManager(Manager):
    def get_queryset(self):
        query = super().get_queryset()

        query = query.filter(deleted_at=None)

        return query
