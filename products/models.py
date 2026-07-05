from django.db import models
from PIL import Image

class Flavour(models.Model):
    name = models.CharField(max_length=50)
    price_per_kg = models.DecimalField(max_digits=6, decimal_places=2, default=200)
    image = models.ImageField(upload_to='flavours/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Resize down if too large (max width 800px, keeps quality high enough)
            max_size = (800, 800)
            if img.height > max_size[1] or img.width > max_size[0]:
                img.thumbnail(max_size, Image.LANCZOS)
                img.save(img_path, quality=80, optimize=True)