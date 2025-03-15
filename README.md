# Touchblack QA Assessment

This repository contains automated test scripts for the demo site [Demoblaze](https://www.demoblaze.com/index.html) written in Python using **Selenium** and **pytest**. Below are the steps to verify and execute the scripts.

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