# 21.02.02 Workshop (주원상)

### 1번. Semantic Tag

```
제시된 semantic.html과 semantic.css를 수정하여 다음 이미지와 같은 형태가 되도록
코드를 작성하시오.
```

```html
#semantic.html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
 
  <header class="all all2 head ">
    <h1>header</h1>
  </header>
  <nav class="all all2 na">
    <h2>nav</h2>
  </nav>
  <section class="all all2 sec">
    <h2>section</h2>
    <article class="all arti">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class="all all2 asi">
    <h2>aside</h2>
  </aside>
  <footer class="all all2 foot">
    <h2>footer</h2>
  </footer>
 
</body>
</html>

```



```css
#css
body {
  font-family: Arial;
  width: 800px;
}

.all2 {
  background-color: lightgrey;
}

.arti {
  background-color: white;
}

.all{
  margin: 4px;
  padding: 4px;
}

h1 {
  text-align: center;
}

.sec, .asi {
  display: inline-block;
}

.sec {
  width: 482px;
  height: 300px;
}

.asi {
  width: 280px;
  height: 300px;
}

.asi {
  vertical-align: top;
  line-height: 250px;
}

.all {
  border-radius: 4px;
}

```

