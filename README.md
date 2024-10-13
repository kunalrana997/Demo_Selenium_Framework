# Demo_Selenium_Framework
Demo selenium framework, built in python and pytest

## **Steps to setup:**
- Use python version >= 3.10
- python3 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt

## **To run all test and get Report**
`pytest --maxfail=1000 -s -v --html=reports/report.html`

- One can see html report at path: `reports/report.html`
- Failed screen shots are available at path: `reports/tests`
- **Note that screenshots are attached in report for failed test cases**

