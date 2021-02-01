# 21.02.01 workshop (주원상)

### 1번.  img tag

```
아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image
폴더 안의 my_photo.png를 보여주는 <img> tag를 작성하시오.
단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.
```

```python
절대경로
<img src="C:Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt="ssafy >

```



### 2번. 파일 경로

```
위와 같이 경로를 __(a)__로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가
변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 __(b)__
로 바꾸어 작성하면 된다
__(a)__와 __(b)__에 들어갈 말과 __(b)__ 로 변경한 코드를 작성하시오.
```

```python
(a)절대경로, (b) 상대경로
상대경로
<img scr="..\image\my_photo.png" alt="ssafy >
```



### 3번. Hyper Link

```
출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.
```

```python
<a href="https://www.ssafy.com">
  <img src="image/my_photo.png" alt="ssafy " width="250">
```



### 4번. 선택자

```
1) 아래의 코드를 작성하고 결과를 확인 하시오.
2) nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.
```

```python
1) 첫번째 단락이 빨간색으로 출력됨
2) 두번째 단락이 빨간색으로 출력됨

3)두 가지의 차이점
nth-child(n): 부모 엘리먼트의 모든 자식(<h2></h2>포함) 엘리먼트중 n번째에 할당
nth-of-type(n): 부모 엘리먼트의 특정 자식(<p></p>중에서만) 엘리먼트중 n번째에 할당
```



