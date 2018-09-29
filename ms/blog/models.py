from django.db import models
from django.utils import timezone

#The blog models are defined here

#Model for travel category
class stories(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "stories"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title		

#Model for fashion category
class fashion(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "fashion"
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title		

#Model for Lifestyle category
class lifestyle(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "lifestyle"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title		

#Model for music category
class music(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "music"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title		


#Model for Art category
class art(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	class Meta:
		verbose_name_plural = "art"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title	


#Model for Glamour category
class glamour(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	class Meta:
		verbose_name_plural = "glamour"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title		


# Model for cards in the main Slider
class sliderCard(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	article_category = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "sliderCard"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title



# Model for trending part
class trending(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	article_category = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)



	class Meta:
		verbose_name_plural = "trending"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

# Model for horizontally placed blocks below trending
class blocks(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	article_category = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	class Meta:
		verbose_name_plural = "blocks"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

# Model for top stories
class topStories(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	article_category = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	class Meta:
		verbose_name_plural = "topStories"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title


# Model for Most Popular menu
class mostPopular(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	article_category = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	class Meta:
		verbose_name_plural = "mostPopular"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

