# Setup

1.  Install Git & Python
```
# Arch
$ sudo pacman -Sy git python

# Windows
> Set-ExecutionPolicy RemoteSigned -scope CurrentUser
> iwr -useb get.scoop.sh | iex
> scoop install git python
```

2. Install pipenv

```
pip install pipenv
``` 

3. Clone the repository
```
git clone https://github.com/joe733/cbcefdb.git
cd cbcefdb
```

4. Enter into pipenv shell & install dependencies
```
pipenv shell
pipenv install
``` 

5. Run the project
```
python manage.py migrate
python manage.py runserver
```