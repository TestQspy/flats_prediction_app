# Flats price prediction app
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a flat listing and returns an estimated price. 

# Flats In Wroclaw Price Estimator: Project Overview 
* Created a tool that estimates flats price (MAE ~ PLN 5K) to help potential buyers negotiate the price for flat.
* Scraped over 15000 flat offers from otodom.pl using python and selenium
* Engineered features from the text of each flat description to quantify the value sellers put on district, flat surface etc. 
* Optimized Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

# Code and Resources Used
**Python Version:** 3.8  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## AND THE BIGGEST HELP IN THIS PROJECT - KEN JEE
His YouTube Data Science Project from Scratch
**https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t**

And also github repo:
**https://github.com/PlayingNumbers/ds_salary_proj**
