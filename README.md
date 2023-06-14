# WNBA-Game-Predictor
Uses current WNBA statistics to make predictions on WNBA matchups.

Using python and tools including xgboost, scikit-learn, pandas, and numpy, a model was trained to predict WNBA matchups based on the average plus-minus of the previous 10 games.

The initial exploration and model training was done through Jupyter Notebook and can be found in the .ipynb file.

In order to deploy a web application, I used FastAPI and Uvicorn to support hosting a local version of the app on my machine.

I made use of Dash for creating an interface. The Dash interface includes a dropdown menu of all available teams to select from. After selecting the teams the probability of the winning team will be displayed below.

This project was primarily for exploration and understanding the technologies that can be used to make analysis and deploy those findings. The plus-minus statistic can be useful, but relying on it solely to train the entire model may not be practical.
