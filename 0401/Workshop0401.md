# 21.04.01 Workshop (주원상)

데이터베이스 M:N 관계를 활용하여 팔로우 기능을 구현하시오

# 1. Model & Form

팔로우 기능 구현을 위한 모델을 세팅한다

팔로우 기능을 구현하기 위해 User 모델을 대체한다

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

```



## 2. url & view
`/accounts/<username>/`

- 유저 프로필 페이지 기능을 구현한다

  ```python
    # accounts/urls.py
      path('<username>/', views.profile, name='profile'),
      path('<int:user_pk>/follow/',views.follow,name='follow'),
  ```

  ```python
  # accounts/views.py
  def profile(request,username):
      person = get_object_or_404(get_user_model(),username=username)
  
      context={
          'person':person,
      }
      return render(request,'accounts/profile.html',context)
  ```

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
  
  <div>
    <div>
      팔로잉: {{ person.followings.all|length}} / 팔로워 : {{person.followers.all|length}}
    </div>
  
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method ="POST">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <button>언팔로우</button>
          {% else %}
            <button>팔로우</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
  <hr>
  
  <h2>{{person.username}}'s 게시글</h2>
  {% for article in person.post_set.all %}
    <div>{{article.title}}</div>
  {% endfor %}
  
  <hr>
  
  <h2>{{person.username}}'s 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{comment.content}}</div>
  {% endfor %}
  
  <hr>
  
  <h2>{{person.username}}'s likes</h2>
  {% for article in person.like_articles.all %}
    <div>{{article.title}}</div>
  {% endfor %}
  
  <hr>
  
  <form action="{% url 'posts:index' %}">
  
    <button class="btn btn-primary">back</button>
  </form>
  {% endblock content %}
  ```

  

- 로그인한 유저만 팔로우를 할 수 있다



`/accounts/<username>/follow/`

팔로우를 하기 위한 기능을 구현한다

- 로그인한 유저만 팔로우를 할 수 있다

- 본인은 팔로우를 할 수 없다

  ```python
  # accounts/views.py
  def follow(request,user_pk):
      if not request.user.is_authenticated:
          return render('accounts:login')
      
      you = get_object_or_404(get_user_model(),pk=user_pk)
      me = request.user
  
      if you != me:
          if you.followers.filter(pk=me.pk).exists():
              you.followers.remove(me)
          else:
              you.followers.add(me)
      
      return redirect('accounts:profile',you.username)
  
  ```

  






## 3. template

index.html의 username에 profile로 갈 수 있는 링크를 설정한다.

```django
# _card.html
<div class="card">
  
  {% if post.image %}
    <img src="{{ post.image.url }}" class="card-img-top" alt="{{ post.image }}">
  {% else %}
    <img src="/media/lion.jpg" class="card-img-top" alt="">
  {% endif %}
  <div class="card-body">
    <h5 class="card-title text-center">
        <a href="{% url 'accounts:profile' post.user.username %}">
          <p>{{post.user}}</p>
        </a>
      <div>
        <form action="{% url 'posts:likes' post.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in post.like_users.all %}
            <button class ="btn btn-outline-secondary"><i class="fas fa-heart" style="color:red;"></i></button>
          {% else %}
            <button class = "btn btn-outline-secondary"><i class="far fa-heart"></i></button>
          {% endif %}
        </form>
        {{post.like_users.all|length}}
      </div>
      <a href="{% url 'posts:detail' post.pk %}" class="btn">{{ post.title }}</a> 
    </h5>  
  </div>
</div>


```
