# aws-ip-range-web 

## 작업 배경
어느 정도의 규모로 봇이 인프라에 접근을 하나 확인하는 작업 중, Request를 보낸 IP들에 규칙성이 종종 있었다.`3.x.x.x`, `15.x.x.x` 이런 대역대가 많았는데 
알고보니 AWS 서비스에서 사용하는 IP 대역대였다. 람다나 EC2에 크롤링 코드를 띄워둔 모양이었다. 
AWS에서는 json 형태로 [AWS 서비스에서 사용하고 있는 IP 대역대](https://ip-ranges.amazonaws.com/ip-ranges.json)를 제공하고 있는데, 몇 만 줄이 넘어가는 json 파일이다보니 보기가 쉽지 않았다. 
그래서 한 눈에 보기 쉽도록 간단한 웹사이트를 구현했다. 


<br>

## 작업 상세 

### 프론트엔드 결정 

별도의 서버 없이 Github Page로 호스팅을 하기 위해 `React.js`를 선택했다. 
한 눈에 보기 쉬운 게 중요해서 `필터 기능`이 필수로 들어가야 했는데 코드를 찾던 중  [react-table-filter](https://github.com/cheekujha/react-table-filter) 가 딱 내가 원하던 
테이블 형태라서 가져와서 사용했다. Google Spread Sheet 사용도 고려를 했으나 가벼운 프로젝트로 기획하여 구글에서 별도로 키를 발급받고, cell을 위한 코드 작성 등이 번거로워 포기했다. 


### 운영 환경 결정 

주기적으로 IP 정보를 업데이트 해주기만 하면 되는 정적인 웹사이트라서 별도로 서버를 구성하지 않았다. 
`Github Action`을 이용해서 주기적으로 IP 정보를 업데이트 해주고, `Github Page`를 이용해서 웹사이트를 호스팅했다. IP 정보를 가져와서 업데이트 해주는 코드는 파이썬으로 작업했다. 

<br>

## 산출물 

### 웹사이트
[AWS IP Table by leeleelee3264](https://leeleelee3264.github.io/aws-ip-range-web/)

<br>
 
### 페이지

![image](https://github.com/leeleelee3264/aws-ip-range-web/assets/35620531/585be549-b617-4e4b-88e4-2408e8b9c7bf)



<br>

### 동작 영상

![image](https://github.com/leeleelee3264/aws-ip-range-web/assets/35620531/1d805ad9-59aa-486e-97ca-228d5d6a807b)
