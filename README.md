# 2019SeoulContest

---

##  This repo is first citizen app for Backend

- 2019 SeoulContest - 김형선, 박지호, 정몽교,  한용희

### 개발 환경 설정

```
git clone https://github.com/contestcrew/2019SeoulContest-Backend.git
brew install pipenv
pipenv --python 3.7.3 shell
pipenv shell
pipenv install
```

### 개발 순서

1. 새로운 작업에 대한 issue를 남긴다. 
2. issue 번호에 해당하는 브랜치를 local에서 생성한다. 
   - 예를 들어 1번 issue에 해당하는 브랜치를 만든다면, 브랜치 명은 `1-개발환경세팅` 이 된다.

3. local에서 생성한 브랜치( `1-개발환경세팅` )에서 작업을 하고 깃헙에 푸쉬한다. 
   - 작업이 완료된 경우 local에서 `add`, `commit`을 한 후 `git push origin 1-개발환경세팅` 으로 푸쉬한다.
4. Github의 repo에 해당하는 push의 pull request를 열어준다.
5. conflict가 나지 않으면 merge한다
   - merge는 급한 작업의 경우가 아니면, 다른 맴버가 확인하고 merge를 한다.
6. merge가 완료되면 local의 `master` 브랜치에서 `git pull origin master`로 업데이트 된 소스 코드를 내려 받는다. 
7. 새로운 작업은 다시 1번 작업부터 반복한다.

