import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDSCBlog.settings")
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment

print("----------------------------------posts-------------------------------------------")
Post.objects.all().delete()
post1 = Post.objects.create(
    title='Post 1',
    category='web development',
    content='Django is a powerful and popular web framework used by developers to build robust and scalable web applications'
)

post2 = Post.objects.create(
    title='Post 2',
    category='web  development',
    content="Improve database queries by using Django's query optimization tools, indexing, and optimizing related queries. Implement caching techniques like template fragment caching, database query caching, and external caching servers"
)

post3 = Post.objects.create(
    title="Post 3",
    category="Business",
    content="Unlock the potential of Django in the world of e-commerce. Dive into the process of building robust and scalable online stores using Django"
)


'''filtering post with catagory'''

posts = Post.objects.filter(category='web development')
for post in posts:
    print(post.title)
    print(post.category)
    print(post.content)
print()
posts = Post.objects.filter(category='web  development')
for post in posts:
    print(post.title)
    print(post.category)
    print(post.content)
print()
posts = Post.objects.filter(category='Business')
for post in posts:
    print(post.title)
    print(post.category)
    print(post.content)
print()

'''updating a post'''
print("updating")
post = Post.objects.get(category="web  development")
post.title = "Building RESTful APIs with Django"
post.catagory = "web development"
post.content = "Learn how to build robust and scalable RESTful APIs using Django. Explore Django's powerful built-in tools for creating APIs"
print(post.title)
print(post.category)
print(post.content)
print()

print("----------------------------------comments-------------------------------------------------")
comment1 = Comment.objects.create(
    post = Post.objects.get(title="Getting Started with Django"),
    author="john smith",
    content="This blog post on getting started with Django is a fantastic resource for beginners like me. The explanation of Django's power and popularity in building web applications is clear and concise"
)

comment2 = Comment.objects.create(
    post = Post.objects.get(title="Optimizing Django"),
    author="Lisa Johnson",
    content="I found this blog post on optimizing Django extremely helpful. As a developer, improving database queries and optimizing performance is crucial"
)

comment3 = Comment.objects.create(
    post = Post.objects.get(title="Django in E-commerce"),
    author="Michael Brown",
    content="This blog post on using Django in e-commerce is a game-changer. The potential of Django in building robust and scalable online stores is impressive. The content provides a great overview of the key aspects to consider when developing an e-commerce platform with Django"
)


comments = Comment.objects.filter(author="Lisa Johnson")
for comment in comments:
    print(comment.author)
    print(comment.content)
    print(comment.post.title)
print()
comments = Comment.objects.filter(author="john smith")
for comment in comments:
    print(comment.author)
    print(comment.content)
    print(comment.post.title)
print()
comments = Comment.objects.filter(author="Michael Brown")
for comment in comments:
    print(comment.author)
    print(comment.content)
    print(comment.post.title)
print()

'''updating a comment'''
print("updating")
comment = Comment.objects.get(author="Michael Brown")
comment.post = Post.objects.get(title="Optimizing Django")
print(comment.author)
print(comment.content)
print(comment.post.title)
print()

'''deleting a post'''
print("deleting post")
post = Post.objects.filter(category="web  development")
post.delete()

'''deleting a comment'''
print("deleting comment")
comment = Comment.objects.filter(author="Michael Brown")
comment.delete()