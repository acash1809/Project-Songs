from django.db import models

from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image =  models.ImageField(default='default.png',upload_to='profile_pics')
	bio = models.TextField(max_length=400, null=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		try:
			this = Profile.objects.get(id=self.id)
			if this.image!=self.image:
				this.image.delete()
		except:
			pass

		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			img.thumbnail(output_size)
			img.save(self.image.path)


'''def save(self, *args, **kwargs):
    try:
        this = MyModelName.objects.get(id=self.id)
        if this.MyImageFieldName != self.MyImageFieldName:
            this.MyImageFieldName.delete()
    except: pass
    super(MyModelName, self).save(*args, **kwargs)'''