README
# Students Social Media Addiction Prediction

A machine learning project that predicts student social media addiction scores based on various behavioral and demographic factors using Random Forest Regression.

## 📋 Overview

This project analyzes student social media usage patterns and predicts addiction scores using features like daily usage hours, academic performance impact, sleep patterns, and mental health scores.

## 🎯 Objective

To build a predictive model that can estimate a student's social media addiction score based on their personal and behavioral characteristics.

## 📊 Dataset

The dataset (`Students Social Media Addiction.csv`) contains information about students including:

- **Age**: Student's age
- **Academic Level**: Education level (encoded)
- **Average Daily Usage Hours**: Time spent on social media daily
- **Affects Academic Performance**: Whether social media impacts studies (encoded)
- **Sleep Hours Per Night**: Daily sleep duration
- **Mental Health Score**: Mental well-being rating
- **Relationship Status**: Current relationship status (encoded)
- **Conflicts Over Social Media**: Number of conflicts related to social media use
- **Addicted Score**: Target variable (what we're predicting)

### Dropped Features
- Country
- Most Used Platform
- Gender
- Student ID

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms and tools
- **seaborn**: Data visualization
- **matplotlib**: Plotting and graphs

## 🔧 Model Details

- **Algorithm**: Random Forest Regressor
- **Number of Estimators**: 100
- **Test Size**: 20%
- **Random State**: 42 (for reproducibility)
- **Feature Scaling**: StandardScaler

## 📈 Model Performance

The model performance is evaluated using:
- **R² Score**: Measures how well the model explains variance in addiction scores

## 📁 Project Structure

```
social-media-addiction-prediction/
│
├── main.py                              # Main script
├── Students Social Media Addiction.csv  # Dataset
├── README.md                            # Project documentation
└── requirements.txt                     # Dependencies (optional)
```

## 🔍 Key Features

- Data cleaning (handling missing values)
- Label encoding for categorical variables
- Feature scaling for improved model performance
- Train-test split for proper evaluation
- Random Forest algorithm for robust predictions

## 📝 Data Preprocessing Steps

1. **Missing Value Handling**: Rows with missing data are removed
2. **Feature Selection**: Irrelevant columns are dropped
3. **Encoding**: Categorical variables are converted to numerical using LabelEncoder
4. **Scaling**: Features are standardized using StandardScaler

## 🎓 Future Improvements

- Feature engineering to create new meaningful features
- Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
- Try other algorithms (XGBoost, Gradient Boosting, Neural Networks)
- Add cross-validation for more robust evaluation
- Create visualizations for feature importance
- Deploy model as a web application

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Aadit Saini

## 📧 Contact

For questions or feedback, please reach out at aaditsaini3@gmail.com

---

**Note**: This project is for educational purposes to understand machine learning applications in behavioral analysis.