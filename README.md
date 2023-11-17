# final-pjt

$ git checkout ""

$ git branch


# db로 저장하기
python -Xutf8 manage.py dumpdata accounts > accounts/fixtures/initial_data.json
python -Xutf8 manage.py dumpdata community > community/fixtures/initial_data.json
python -Xutf8 manage.py dumpdata movies > movies/fixtures/initial_data.json

# db에서 가져오기
python manage.py loaddata accounts/fixtures/initial_data.json community/fixtures/initial_data.json movies/fixtures/initial_data.json


# accounts 앱 데이터 로드
python manage.py loaddata accounts/fixtures/initial_data.json

# community 앱 데이터 로드
python manage.py loaddata community/fixtures/initial_data.json

# movies 앱 데이터 로드
python manage.py loaddata movies/fixtures/initial_data.json

