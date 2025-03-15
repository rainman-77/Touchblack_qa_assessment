# Touchblack QA Assessment

This repository contains automated test scripts for the demo site [Demoblaze](https://www.demoblaze.com/index.html) written in Python using **Selenium** and **pytest**.

## Dependencies

1. The required Python libraries are already listed in the `requirements.txt` file.
2. Run the following command to install them:
   ```bash
   pip install -r requirements.txt
   
## Configuration

Open the `config.ini` file and update the settings if needed.

## Commands to Run Tests in Terminal

1. **To run all test scripts without reporting:**
   ```bash
   pytest tests
   
2. To run tests and generate Allure reports and view it:
    ```bash
    pytest tests --alluredir=./allure_reports_json
    allure generate allure_reports_json -o allure_report --clean
    allure open allure_report
3. Log files are generated automatically as per settings in conftest.py.

## Framework Structure

- **tests/**: Contains all the test scripts.
- **page_objects/**: Contains the page object model structure for the project.
- **configurations/**: Contains configuration files, including the `config.ini` used to manage settings.
- **logs/**: Stores log files generated during test execution.
- **allure_report/**: Generated Allure reports can be viewed by running the `allure open` command as described above.

## Tools & Libraries Used

- **Python**: The primary programming language for scripting the tests.
- **Selenium**: For web automation and interaction with the browser.
- **pytest**: For test execution.
- **Allure**: For generating beautiful HTML reports.
- **pytest-order**: For ordering the execution of test cases and test classes.
- **openpyxl**: For data-driven testing using Excel.

## Sample Output / Screenshots

The sample output can be viewed by running the following command which will open the generated Allure report in your default browser.:
```bash
allure open allure_report
```

## Instructions for Setting Up and Running the Framework

Follow these steps to set up and run the test automation framework on your local machine:

### 1. Clone the Repository

To get a copy of the repository to your local system, run the following command in your terminal:

```bash
git clone https://github.com/rainman-77/Touchblack_qa_assessment.git
```

Alternatively, you can download the repository as a ZIP file directly from GitHub and extract it to your desired location.

### 2. Navigate to the Project Directory
Once you have the repository, navigate into the project folder:
```bash
cd Touchblack_qa_assessment
```

### 3. Set Up a Virtual Environment (Recommended)
It's recommended to use a virtual environment to manage project dependencies. To create a virtual environment, run:

For macOS/Linux:
```bash
python3 -m venv venv
```

For Windows:
```bash
python -m venv venv
```

Activate the virtual environment:

For macOS/Linux:
```bash
source venv/bin/activate
```

For Windows:
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
Install the required libraries listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 5. Configuration
Open the config.ini file located in the configurations/ folder and modify the settings as per your requirements. 
For example, you may need to set your preferred browser, browser mode etc

### 6. Running the Tests
After setting up the environment, you can run the tests. Use the above command shown in section [Commands to Run Tests in Terminal](#commands-to-run-tests-in-terminal)

### 7. Check Logs
Log files are generated automatically based on the settings in conftest.py. You can find these log files in the logs/ folder.


