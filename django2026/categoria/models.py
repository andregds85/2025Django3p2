from django.db import models


class categoria(models.Model):
    hospital = models.CharField("hospital", max_length=255, blank = True, null = True)
    cnes = models.CharField("cnes", max_length=255, blank = True, null = True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.hospital