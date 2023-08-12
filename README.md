# california_house_pricing

### Problem Statement:

This is a regression problem to predict california housing prices.

### Software and Tools requirements

1. [GithubAccount](https://githib.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/download)
4. [GitCLI](https://git-scm.com/downloads)

### About the data set:

It can be downloaded/loaded using the function `sklearn.datasets.fetch_california_housing` 

### Data Set Characteristics

- Number of Instances: 20640
- Number of Attributes: 8 numeric, predictive attributes and the target variable

### Data Preparation:

- Created DataFrame using pandas to the dataset.
- using data.info(), analyzed data types and if any missign values
- data.describe() to summarize the stats of the dataset.
- data.isnull() used to check missing values

### Exploratory Data Analysis:

- Analyzed the correlation between independent variables.
- Analyzed  cprrelation between independent and dependent variables
- Drawn various charts and graphs using matplotlib and seaborn to visualize.

### Creating ML Model:

- Divide independent(x) and dependent(y) variables
- Train test split the data
- Test size is 20%

### Standard Scaler:

- Standardized all the data points to the same scale using standard scaler
- Fit the scaled data into training data set

### Model Training:

- Train the model
- Find the good accuracy
- See how it is performing with respect to test data

### Model Prediction:

- Prediction using test data
- Compare the predictions x_test with y_test


Create a new environment for the project

1. conda create -p venv python==3.7 -y
2. To activate:
3. conda activate venv/
4. Create requirements.txt file with all required libraries
5. Install libraries using pip install -r requirements.txt