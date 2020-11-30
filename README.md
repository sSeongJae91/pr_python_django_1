# pr_python_django_1
<hr/>
장고 설치
<hr/>
> sudo pip install Django
<hr/>
장고가 설치된 디렉토리 검색
<hr/>
> python3 -c "import django; print(django.__path__)"
<hr/>
장고 프로젝트 생성
<hr/>
> django-admin startproject mysite
<hr/>
애플리케이션 생성
<hr/>
> python3 managy.py startapp polls
<hr/>
호스트 설정
<hr/>
- settings.py 수정 =>  ALLOWED_HOST = ['xxx.xx.xx.xxx', 'localhost', '127.0.0.1']
<hr/>
ADMIN PAGE 관리자 생성
<hr/>
> python3 manage.py createsuperuser
<hr/>
model변경될 경우 변경사항 추출
<hr/>
> python3 manage.py makemigrations
<hr/>
변경사항 반영
<hr/>
> python3 manage.py migrate
<hr/>
서버 run
<hr/>
> phthon3 manage.py runserver
<hr/>
