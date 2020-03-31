# Atlus
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
## 3. Screenshots
| Initial Screen | Entered Form Data | Result Displayed |
| -------|--------------|-----------------|
|![Initial Screen](https://github.com/dragonblood/Atlus/blob/master/Github_readme_img/Screenshot%20from%202020-03-31%2018-52-52.png)|![Entered Form Data](https://github.com/dragonblood/Atlus/blob/master/Github_readme_img/Screenshot%20from%202020-03-31%2018-54-48.png)|![Result Displayed](https://github.com/dragonblood/Atlus/blob/master/Github_readme_img/Screenshot%20from%202020-03-31%2018-54-18.png)|

### Please Feel Free to raise an issue.
### Take Permission Before using it in your work.
