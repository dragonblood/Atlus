# Atlus [![Django CI](https://github.com/dragonblood/Atlus/actions/workflows/django.yml/badge.svg)](https://github.com/dragonblood/Atlus/actions/workflows/django.yml)
## 1. About:

when the data is entred in HTML form, It is then submitted using POST and sent through RestAPI to the Classifier, trained using Gradient Boosted Trees.Then the prediction is made using model.sav file (Pickle) and result is displayed as Message on the same page.

XGBoot Classifier Trained Using Folling Databse:
https://www.kaggle.com/osmi/mental-health-in-tech-survey

## 2. Steps To Follow:
```
git clone https://github.com/dragonblood/Atlus.git
cd Atlus
conda env create --file Atlus.yml
conda activate atlus
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Or (PIP method)
```
pipenv shell
pipenv install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## 3. Screenshots
| Initial Screen | Output |
|--------------|-----------------|
|![Initial Screen](https://raw.githubusercontent.com/dragonblood/Atlus/master/Initial.png)|![Result Displayed](https://raw.githubusercontent.com/dragonblood/Atlus/master/Results.png)|

## Please Feel Free to raise an issue.
## Take Permission Before using it in your work.
