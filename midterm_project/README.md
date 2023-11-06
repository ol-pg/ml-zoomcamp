# TikTok User Engagement Data

Hi there! This is my midterm project for Machine Learning Zoomcamp 2023.

![Imgur](https://www.internetmatters.org/wp-content/uploads/2019/04/Tik_Tok_logo.png)
# Description

TikTok is the leading destination for short-form mobile video. The platform is built to help imaginations thrive. TikTok's mission is to create a place for inclusive, joyful, and authentic content–where people can safely discover, create, and connect.

To build a machine learning model that can determine whether a video contains a **claim or an opinion**, there are several stages and techniques that can be used. It is important to split the data into training, validation, and test sets to avoid overfitting and underfitting. Additionally, it is important to validate and verify your machine learning model outcomes to ensure that you're getting the right data and that the data is accurate. Finally, it is important to deploy your machine learning model in production and monitor it regularly to ensure that it continues to put out accurate, relevant information.

The data can downloaded from [kaggle](https://www.kaggle.com/datasets/yakhyojon/tiktok/data).

## About the dataset

TikTok is the leading destination for short-form mobile video. The platform is built to help imaginations thrive. TikTok's mission is to create a place for inclusive, joyful, and authentic content–where people can safely discover, create, and connect.


|  Column name  |             Type             |  Description  |
|:--------:|:-----------------------------------:|:-----------------------------------:|
|    **#**   |  int  |   TikTok assigned number for video with claim/opinion.    |
|    **claim_status**   |  obj |    Whether the published video has been identified as an “opinion” or a “claim.” In this dataset, an “opinion”  to an individual’s or group’s personal belief or thought. A “claim” refers to information that is either unsourced or from an unverified source.  | 
|    **video_id**   |  int |    Random identifying number assigned to video upon publication on TikTok.  |
|   **video_duration_sec**   | int | How long the published video is measured in seconds. |
| **video_transcription_text** |    obj  | Transcribed text of the words spoken in the published video. |
| **verified_status** |  obj | Indicates the status of the TikTok user who published the video in terms of their verification, either “verified” or “not verified.”| 
|  **author_ban_status**  | obj  |Indicates the status of the TikTok user who published the video in terms of their permissions: “active,” “under scrutiny,” or “banned.” | 
| **video_view_count**  |  float | The total number of times the published video has been viewed. |
| **video_like_count**  |  float | The total number of times the published video has been liked by other users. |
| **video_share_count**  |  float | The total number of times the published video has been shared by other users. |
| **video_download_count**  |  float | The total number of times the published video has been downloaded by other users. |
| **video_comment_count**  |  float |  The total number of comments on the published video. |

## Files in repo
|  File name |      Description       |
|:--------:|:-----------------------------------:|
|    **tiktok_dataset.csv**   |  Dataset for the study |
|    **notebook.ipynb**   |  Data preparation and data cleaning; EDA, feature importance analysis; Model selection process and parameter tuning |
|    **train.py**   |  Training the final model; Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML) |
|    **predict.py**   |  Loading the model; Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)|
|    **Pipfile**   |  python virtual environment management (pipenv) file with all the used packages and their versions listed (used for deployment)|
|    **Pipfile.lock**   |  python virtual environment management(pipenv) file specifying which specific version of the packages present in `Pipfile` should be used (used for deployment)|
|    **Dockerfile**   |  Dockerfile for running the service|
|    **README.md**   |  The file is an essential guide that gives other developers a detailed description of your GitHub project. | 



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
If you encounter any problem running any part of the project contact me at:

    - olgapogodina11@gmail.com

    - tg https://t.me/ol_pg

