# Insurance Risk Prediction

This project aims to predict the risk level of insurance applicants using machine learning models. By analyzing customer data such as age, gender, income, health status, and claim history, the system estimates the likelihood of future insurance claims or losses. The goal is to help insurance companies assess risk more accurately, streamline underwriting processes, and make data-driven decisions.

Key features include:
- Data preprocessing and cleaning scripts
- Exploratory Data Analysis (EDA) notebooks
- Machine learning model training and evaluation
- Modular code structure for easy extension and maintenance

## Project Structure

 ├── .dvcignore 
 ├── .gitignore 
 ├── README.md 
 ├── requirements.txt 
 ├── .dvc/ 
 ├── env/ 
 ├── notebooks/ 
           │ ├── EDA.ipynb 
           │ └── README.MD 
           
├── scripts/ │ 
             └── data_prep.py 
├── src/ │ 
         └── data/ 
├── tests/ 
└── vscode/


## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [DVC](https://dvc.org/) (for data version control)

### Installation

1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd Insurance_Risk_prediction-
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) Pull data with DVC:
    ```sh
    dvc pull
    ```

## Usage

- **Data Preparation:**  
  Use the [`scripts/data_prep.py`](scripts/data_prep.py) script for data cleaning and preprocessing.

- **Exploratory Data Analysis:**  
  Open and run the [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb) notebook for EDA.

- **Source Code:**  
  Core logic and model code can be found in the [`src/`](src/) directory.

## Testing

Add your tests in the [`tests/`](tests/) directory and run them using your preferred test runner.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

