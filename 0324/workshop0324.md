# 21.03.24 Workshop (주원상)

### 1. Model

댓글 작성을 위한 테이블을 정의한다.

```
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```



### 2. Comment Create

/articles/comments/ 댓글 작성 기능을 구현한다.

```
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
```





### 3. Comment Read

댓글 읽기 기능을 구현한다. 상세 페이지 하단에 댓글 목록을 출력한다.

```
<h4>댓글 목록</h4>
  <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% empty %}
      <p>댓글이 없습니당.</p>
    {% endfor %}
  </ul>
```





### 4. Comment Delete

articles/comments/delete/ 댓글 삭제 기능을 구현한다.

```
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)

```
