# 관통프로젝트 세번째 시간(반응형 웹 페이지 구성)

##  목표 

##  ⚫ HTML을 통한 웹 페이지 마크업 분석 

##  ⚫ CSS 라이브러리의 이해와 활용 

##  ⚫ 컴포넌트 및 그리스 시스템 활용 

##  ⚫ 커뮤니티 서비스 반응형 레이아웃 구성





### a . nav_footer

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <title>Navbar Footer Test</title>
</head>
<body>
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="02_home.html">
        <img src="images/logo.png" alt="" style="width: 120px;">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="02_home.html" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" @getbootstrap>Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<!-- modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
  <footer class="fixed-bottom">
    <div class="text-center p-2">Web-bootstrap PJT, by 주원상</div>
  </footer>
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>
```



### b. home

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="02_home.css">
  <title>Home</title>
</head>
<body>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="02_home.html">
        <img src="images/logo.png" alt="" style="width: 120px;">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="02_home.html" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" @getbootstrap>Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<!-- modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
  <footer class="fixed-bottom">
    <div class="text-center p-2">Web-bootstrap PJT, by 주원상</div>
  </footer>

  
  <!-- 02_home.html -->
  <header style="margin-top: 61px;">
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/header1.jpg" class="d-block w-100" alt="main image 1">
        </div>
        <div class="carousel-item">
          <img src="images/header2.jpg" class="d-block w-100" alt="main image 2">
        </div>
        <div class="carousel-item">
          <img src="images/header3.jpg" class="d-block w-100" alt="main image 3">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
    </div>
  </header>

  <br><br>
  <h1 class="m-4 text-center fw-bold">Boxoffice</h1>
  <hr>

  <section class="m-5">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4 m-4">
      <div class="col">
        <div class="card">
          <img src="images/movie1.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie2.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie3.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie5.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="images/movie6.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <br><br><br>
  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html> 
```

### c. community

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="01_nav_footer.css">
  <link rel="stylesheet" href="03_community.css">
  <title>Community</title>
</head>
<body>

  <!-- 01_nav_footer.html -->
  <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand" href="02_home.html">
        <img src="images/logo.png" alt="" style="width: 120px;">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" aria-current="02_home.html" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal" @getbootstrap>Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<!-- modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
  <footer class="fixed-bottom">
    <div class="text-center p-2">Web-bootstrap PJT, by 주원상</div>
  </footer>



  <!-- 03_community.html -->
  <div class="main" style="margin-top: 100px;">
    <h1 class="m-5 text-center fw-bold">Community</h1>
    <!-- Sidebar -->
    <div class="container">
      <div class="row">
        <aside class="col-12 col-lg-2">
          <ul class="list-group text-primary">
            <a href="#" class="text-decoration-none">
              <li class="list-group-item">Boxoffice</li>
            </a>
            <a href="#" class="text-decoration-none">
              <li class="list-group-item">Movies</li>
            </a>
            <a href="#" class="text-decoration-none">
              <li class="list-group-item">Genres</li>
            </a>
            <a href="#" class="text-decoration-none">
              <li class="list-group-item">Actors</li>
            </a>
          </ul>
        </aside>

        <!-- Board -->
        <section class="d-none d-lg-block col-12 col-lg-10"> 
          <div>
            <table class="table table-hover">
              <thead class="table-dark">
                <tr>
                  <th scope="col">Great Movie title</th>
                  <th scope="col">글 제목</th>
                  <th scope="col">작성자</th>
                  <th scope="col">작성 시간</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Best Movie Ever</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie Test</td>
                  <td>user</td>
                  <td>1 minutes ago</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      <div class="d-block d-lg-none">
        <article>
          <hr>
          <p><h5>Best Movie Ever</h5></p>
          <p><h6>Great Movie Title</h6></p>
          <p><h6>1 minutes ago</h6></p>
          <hr>
          <p><h5>Best Movie Ever</h5></p>
          <p><h6>Great Movie Title</h6></p>
          <p><h6>1 minutes ago</h6></p>
          <hr>
          <p><h5>Best Movie Ever</h5></p>
          <p><h6>Great Movie Title</h6></p>
          <p><h6>1 minutes ago</h6></p>
        </article>
      </div> 
      <div class="d-flex justify-content-center mt-5">
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
      </div>
      </div>
    </div>
  </div>


```

## 느낀점 및 수정사항

```python
아직 너무 부족하고 일단은 리드미를 주말에 수정해야겠습니당 ㅠ

```

