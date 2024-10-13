
# **Demo Selenium Framework**

A robust Selenium-based test automation framework built using Python and Pytest, designed for efficient and scalable test execution, incorporating the **Page Object Model (POM)** design pattern for better code maintainability.

---

## **Project Setup Instructions**

### **Prerequisites:**
- Ensure you have **Python 3.10** or a higher version installed.
  
### **Steps to Set Up the Framework:**
1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - For **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - For **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Page Object Model (POM)**

This framework implements the **Page Object Model (POM)** design pattern, ensuring:
- **Separation of concerns**: Each web page is represented by a corresponding class, making the code more modular and easier to manage.
- **Maintainability**: UI element locators and interaction methods are encapsulated in page-specific classes, reducing code duplication and simplifying updates when the UI changes.

---

## **Running Tests and Generating Reports**

### **Run All Tests with Report**
To execute all tests and generate an HTML report:

```bash
pytest --maxfail=1000 -s -v --html=reports/report.html
```

- **Test Report**: The HTML report will be available at: `reports/report.html`
- **Failed Test Screenshots**: Screenshots for any failed test cases will be saved at: `reports/tests`
- Screenshots are also **automatically attached** to the report for failed test cases, providing detailed insights into failures.

---

## **Running a Particular Test or Function**

### **Run a Specific Test File**
To run tests from a specific test file:

```bash
pytest path/to/test_file.py
```

### **Run a Specific Test Function**
To run a specific test function inside a test file:

```bash
pytest path/to/test_file.py::test_function_name
```

For example, to run the `test_login` function inside the `test_user_auth.py` file:

```bash
pytest tests/test_user_auth.py::test_login
```

This allows you to focus on running individual test cases without executing the entire test suite.

---

## **Additional Information**

- The framework captures screenshots for failed tests, aiding in efficient debugging.
- The generated HTML report provides a comprehensive view of test execution, including pass/fail statuses, test durations, and error details.
- The **Page Object Model (POM)** architecture makes it easier to scale and maintain automated tests as the application grows.

---