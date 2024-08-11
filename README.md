# A WebApp to Diagnose Human Pyrexia Cases using Machine Learning

<div align="center"><img src="https://github.com/user-attachments/assets/b3aa3566-a3c6-4f64-a180-d572a6e328fb"></div>

This repository contains the implementation of a machine learning-driven web application designed to diagnose human pyrexia (fever). The application employs classical machine learning algorithms to classify the likelihood of a patient having fever based on their symptoms and medical history. The project highlights the integration of machine learning models into a web-based application, offering a practical tool for preliminary medical diagnosis.

The model is built, trained, and evaluated within a Jupyter Notebook environment before being deployed as a Flask-based web application. The web interface enables users to input relevant symptoms and receive a real-time diagnostic prediction generated by the trained model.

A dataset has been developed, consisting of symptoms of pyrexia patients, obtained from pyrexia patients admitted to the hospital in five districts of Bangladesh. In addition, the collected data is analyzed in detail. The dataset is used to evaluate the accuracy of various machine learning algorithms to determine the most effective one for the task. 

## Dataset

<div align="center"><img src="https://github.com/user-attachments/assets/389dba97-ea52-4a6e-a94c-8a8570e98b52"></div>

The dataset contains symptoms of 153 patients admitted at the hospitals and diagnosed with either Dengue, Typhoid or Malaria collected between September,2019 to December,2019. The dataset was collected in accordance with the 29 features, designed for the purpose. 

Fig (a) represents the distribution of 153 data records according to each class. The dataset is minor unbalanced which can be negligible in this case. Data was recorded and collected from various divisions of Bangladesh. Since it was collected from a wide geographical region, the dataset contains a good amount of variance in this perspective. Figure (b) shows the number of patient records collected from each division. Most number of patient records were registered from Chittagong which includes hill districts like Rangamati, Bandarban and Khagrachori. The diseases are most common in the Chittagong division due to presence of hill districts.

## Machine Learning Model
### List of Features
<div align="center"><img src="https://github.com/user-attachments/assets/520f9845-1195-4a28-b4a2-6de090ff4830"></div>

### Model Performance
For the evaluation process and to determine the best-performing model,  the model accuracy, precision, recall and F1 score of each trained model has been calculated. For high-quality performance evaluation, the dataset has been splitted into 75% and 25% for training and testing consecutively. 

<div align="center"><img src="https://github.com/user-attachments/assets/d0c199c5-efcb-4b9f-b93a-c14a13070a58"></div>

## Key Features
- Machine Learning Classifier: The project implements a robust classification model utilizing machine learning techniques to assess the probability of fever in a patient. The model’s architecture and hyperparameters are optimized for diagnostic accuracy.

- Web-Based Deployment: The machine learning model is encapsulated within a Flask web application, providing a user-friendly interface for non-technical users to interact with the diagnostic tool.

- Data-Driven Insights: The classifier is trained on a dataset comprising historical cases of pyrexia, ensuring that the diagnostic outputs are grounded in empirical data. The training process includes data preprocessing, feature engineering, and model validation steps.




## Installation
To set up the environment for this project, ensure that you have Python installed along with the necessary libraries. The following Python packages are required:

- Flask (for web application deployment)
- Scikit-learn (for model development)
- Pandas (for data manipulation)
- Numpy (for numerical operations)
- Jupyter Notebook (for model training and experimentation)

## Usage
The project can be executed in two primary modes: model development via the Jupyter Notebook and deployment as a web application using Flask.

### Running the Jupyter Notebook
1. Clone the repository:
```bash
git clone https://github.com/Dipon12/A-WebApp-to-Diagnose-Human-Pyraxia-Case-using-Machine-Learning-Approach.git
cd A-WebApp-to-Diagnose-Human-Pyraxia-Case-using-Machine-Learning-Approach
```

2. Execute the Jupyter Notebook:
```bash
jupyter notebook "Fever Classifier.ipynb"
```

3. Model Training and Evaluation:

- The notebook guides the user through data preprocessing, model training, hyperparameter tuning, and performance evaluation, utilizing metrics such as accuracy, precision, recall, and F1-score to assess model efficacy.

## Deploying the Web Application

1. Launch the Flask Application:
```bash
python app.py
```

2. Access the Diagnostic Tool:
- Navigate to `http://127.0.0.1:5000/` in your web browser to interact with the fever diagnosis tool. The application accepts user inputs via a web form and returns a diagnostic prediction based on the trained model.

## Files
- `Fever Classifier.ipynb`: Contains the full implementation of the machine learning model, including data processing, model training, and evaluation.
- `app.py`: The Flask application script that serves the web-based diagnostic tool.
- `README.md`: This document, providing detailed project documentation.
