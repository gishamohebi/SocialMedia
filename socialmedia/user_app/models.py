from django.db import models
from . import managers


class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Enter your first name"
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        help_text="Enter your last name"
    )

    phone_number = models.CharField(
        unique=True,  # must be unique because it is a social app
        null=False,
        max_length=12,
        help_text="Your phone number",
        error_messages={
            "unique": "This phone number exist",
            'required': 'Please enter your phone'}
    )

    email = models.EmailField(
        blank=False,
        unique=True,  # must be unique because it is a social app
        null=False,
        error_messages={
            "unique": "This email exist",
            'required': 'Please enter your email'}
    )

    id_code = models.CharField(
        max_length=4,
    )

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        default="post"
    )
    text = models.TextField(
        blank=True,
        null=True,
        help_text="caption"
    )
    image = models.ImageField(
        verbose_name="Image",
        blank=False,
        null=False,
        default=None,
        upload_to="image",
    )
    date = models.DateField(
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    objects = managers.PostsOfWeek()

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Commented ON POST  {self.post.user}  ."
