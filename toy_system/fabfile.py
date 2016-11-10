from fabric.api import local

def testRun():
    local('python manage.py migrate choose')
    local('python manage.py test choose')
    local('python manage.py runserver')