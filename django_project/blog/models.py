from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# User can have multiple posts, but a post will have one author => 

# Create your models here.
class Post(models.Model):
    title = models.CharField('Title', max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted , delete these posts of user

    def __str__(self) -> str:
        return self.title




# >>> from blog.models import Post
# >>> from django.contrib.auth.models import User
# >>> User.objects.all()
# <QuerySet [<User: arun.khanchandani>, <User: Test>]>
# >>> User.objects.first()
# <User: arun.khanchandani>
# >>> User.objects.last()
# <User: Test>
# >>> User.objects.filter(username='Test')
# <QuerySet [<User: Test>]>
# >>> test = User.objects.filter(username='Test')
# >>> type(test)
# <class 'django.db.models.query.QuerySet'>
# >>> test = User.objects.filter(username='Test').first()
# >>> type(test)
# <class 'django.contrib.auth.models.User'>

# >>> Post.objects.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>]>
# >>> post1 = Post.objects.first()
# >>> post1.content
# 'First post content!'
# >>> post1.date_posted
# datetime.datetime(2023, 7, 7, 8, 1, 47, 369267, tzinfo=datetime.timezone.utc)
# >>> post1.author
# <User: Test>

# >>> user = User.objects.all()
# >>> user
# <QuerySet [<User: arun.khanchandani>, <User: Test>]>
# >>> user = User.objects.get(username = 'Test')
# >>> user
# <User: Test>
# >>> user.post_set
# <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000013A436567A0>
# >>> user.post_set.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>]>