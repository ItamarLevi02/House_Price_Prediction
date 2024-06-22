# Predictive Modeling of U.S. Real Estate Prices

## Project Overview

This project aims to predict home prices in the Bay Area, California, using various machine learning models. By analyzing features like the number of bedrooms, bathrooms, lot size, square footage, and location, we developed a model that provides accurate home price predictions.

## Author
 Itamar Levi

## Abstract
My machine learning model predicts home prices based on features such as bedrooms, bathrooms, lot size, square footage, and location. Focusing on the Bay Area, we combined exploratory data analysis (EDA) with regression modeling, using techniques like data clustering and one-hot encoding to enhance accuracy.

## Introduction
Accurate home price prediction is essential for buyers, sellers, investors, and policymakers. Traditional methods often fall short due to their inability to capture complex interactions between factors. We employed various machine learning techniques, including linear regression, decision trees, Lasso, and Ridge regression, with ensemble methods like Random Forests to improve predictions.

## Methodology

### Data Collection and Preprocessing
- **Source**: Kaggle
- **Features**: Price, bedrooms, bathrooms, lot size, address, city, zip code, house size, and price per square foot.
- **Scope**: Focused on the Bay Area for better model accuracy.
- **Steps**:
  - Handled missing values.
  - Encoded categorical variables using one-hot encoding.
  - Normalized features.
  - Removed outliers for cleaner data.

### Exploratory Data Analysis (EDA)
- Visualized data distribution and identified correlations.
- Removed outliers to improve data quality.
- Plotted scatter plots and created correlation maps.

### Model Development
- **Feature Engineering**: 
  - One-hot encoding for city names.
  - K-means clustering for zip codes based on average home prices.
- **Models Evaluated**:
  - Linear Regression
  - Decision Tree
  - Lasso Regression
  - Ridge Regression
- **Hyperparameter Tuning**: Grid search and cross-validation for optimization.

### Model Evaluation
- **Baseline**: Linear regression achieved 61% accuracy.
- **Final Model**: Decision Tree with 92% accuracy.
- **Enhancements**: Included clustered zip codes and one-hot encoded city names for improved performance.

## Results
The final model, using decision trees, achieved an accuracy of 92%. Incorporating clustered zip codes and one-hot encoding significantly boosted the model's performance from the baseline.

## Conclusion
Our study highlights the effectiveness of machine learning in real estate price prediction. Key insights include the importance of handling categorical data and thorough EDA. Future work could integrate more features and explore advanced algorithms for further improvements.

## Road Map
1. **Data Collection**
   - Source: Kaggle
   - Features: Price, bedrooms, bathrooms, lot size, address, city, zip code, house size, price per square foot.
2. **Exploratory Data Analysis (EDA)**
   - Handle missing values, encode categorical variables, normalize features, visualize data, remove outliers.
3. **Feature Engineering**
   - One-hot encoding for city names, K-means clustering for zip codes.
4. **Model Selection**
   - Evaluate Linear Regression, Decision Tree, Lasso Regression, Ridge Regression.
5. **Hyperparameter Tuning**
   - Optimize models using grid search and cross-validation.
6. **Model Training and Testing**
   - Train and validate the final Decision Tree model.
7. **Implementation and Deployment**
   - Export model, deploy using Flask, integrate with front-end application.
8. **Future Work**
   - Integrate additional features, apply sophisticated algorithms, maintain model relevance with real-time data and periodic retraining.

## References
- Wu (2020), Limsombunchai (2004)

## GitHub Repository Link
- [Project Repository](https://github.com/ItamarLevi02/Term_Project.git)
- [Demo Video](https://www.loom.com/share/64073230839b43898127434a71006900?sid=16b154e2-842e-4267-baf7-b7118d07c8d4)
