# Text Classification of Course Designs 
This repository aims to depositary the projects for text classification tasks in diverse contexts of the course designs. In this repository, there are models developed for the two tasks temporarily. 

## Text Classification for Song Lyrics and News Data
The project files lie in the folder `Lyrics_News`. Aiming to recognize the artist of one specific song through the lyric, the text classification models are developed.  
However, a lot of feature enigneering methods and deep learning models show a poor performance on the lyric data, which can only be used for music recommendation from the lyrics. After that, the above models and methods are used for recognize the news genre from one specific news report, and show a remarkable performance. 
### lyric data  
About the data, the crawler inside the folder `Lyrics-Cralwer` is used for getting the lyric data from Netease Music. In this project, 41 most famous artists in recent three decades are selected with the song lyrics in all their formal albums. 
### news data
All news data is from the public [dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) which collected HuffPost news reports with categories  from 2012 to 2018.

## Real or Fake Job Postings Recognition
The project files lie in the folder `Job_Postings`. Basically, the feature engineering methods and the models used in this project are similar to the former, while an `oversampling` method is used in this project for settling the extremely unbalanced  dataset. 
### job postings data
The [dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) is available on Kaggle. However, the dataset is extremely unbalanced. There are 17014 real job postings, and just 866 fake postings. 
