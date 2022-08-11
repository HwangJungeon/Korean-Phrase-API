# 한국어 명언 API
500개의 한국어 명언 중 하나를 랜덤으로 리턴해주는 API입니다.
<br>사용방법은 다음을 참고해주세요.</br>

# API 사용방법
|요청|타입|응답코드|응답
|------|----|---|---------------|
|[GET] https://api.jungeon.cc/korean/phrase |JSON|200|{ "phrase": "명언 내용", "writer": "저자 이름" }|
|[GET] https://api.jungeon.cc/korean/phrase |JSON|429|{ "Too Many Requests": "50 per minute" }|

# API 사용량
<b>1분</b> 동안 <b>50번</b> 호출 가능
<br><b>1일</b> 동안 <b>5000번</b> 호출 가능</br>
