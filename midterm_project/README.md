Hi there! This is my midterm project for Machine Learning Zoomcamp.

# Description


File in repository :


# How to run project

## Starter
Download project
Install dependencies with pipenv install

## To run notebook.ipynb
Activate virtual environment in directory by pipenv shell and open jupyter notebook
Open notebook.ipynb
Run first section 1(Table of contents ) to section 5(EDA) .
For section 6.1 and 6.2 , you can run 6.2 first than 6.1 , but in each subsection of 6.1 and 6.2 , must run sequentially
For section 6.2 to 9.4 , run first section between 6.2 and 6.3.No need to run sequentially in section 6.2 to 9.4 , but need to run sequentially in each section.

## To run train.py
Activate virtual environment in directory by pipenv shell
run python train.py , it will save model_chosen.bin in directory

## Deploy locally using docker
run docker image using docker run -it --rm -p 9696:9696 zoomcamp-project
run python predict-test.py on another command prompt
Player data that specified in predict-test.py can modified if you want to try another player

# Contacts
