# Wipro Python Automation

A collection of hands-on automation work using **Selenium WebDriver**, Python, pytest, and related test automation tools. It includes four Selenium assignments and a capstone e-commerce automation project.

## 📋 Overview

| # | Assignment | Core Concept | Status |
|---|-----------|---------------|--------|
| 1 | Web Element Identification | Locating elements with `By.ID`, `By.NAME`, `By.TAG_NAME`, `By.LINK_TEXT`, `By.CLASS_NAME` | ✅ |
| 2 | Multiple Element Identification | Finding and iterating over lists of elements (`find_elements`) | ✅ |
| 3 | CSS Selector Challenge | CSS selectors with wildcards for dynamic attribute values | ✅ |
| 4 | Child Nodes Using CSS | CSS child/descendant selectors for nested elements | ✅ |

## 🛠️ Tech Stack

- **Selenium WebDriver** (Python bindings)
- **WebDriver Manager** (for automatic driver binaries)
- Browser: Chrome / Firefox

## 📁 Repository Structure

The project root is named `Wipro-Python-Automation`:

```text
Wipro-Python-Automation/
│
├── Assignments/assignment-1/
│   ├── assignment1.py
│   ├── index.html
│   ├── README.md
│   └── requirements.txt
│
├── Assignments/assignment-2/
│   ├── asssignment2.py
│   ├── index.html
│   ├── README.md
│   └── requirements.txt
│
├── Assignments/assignment-3/
│   ├── assignment3.py
│   ├── index.html
│   ├── README.md
│   └── requirements.txt
│
├── Assignments/assignment-4/
│   ├── assignment4.py
│   ├── index.html
│   ├── README.md
│   ├── requirements.txt
│   └── sample.xml
│
├── capstone-project/
├── Certificates/
├── Reports/
├── Installation Guide.mp4
└── README.md
```

## 📖 Assignment Details

### Assignment 1: Web Element Identification
Identify and locate different web elements on a given webpage using:
- `By.ID`
- `By.NAME`
- `By.TAG_NAME`
- `By.LINK_TEXT`
- `By.CLASS_NAME`

**Example task:** Locate the username field by ID, the password field by Name, and a link by Link Text.

```python
driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "password")
driver.find_element(By.LINK_TEXT, "Forgot password?")
```

### Assignment 2: Multiple Element Identification
Identify multiple elements of the same type on a webpage and use Selenium to find and work with the list of elements returned by `find_elements`.

**Example task:** Find all links on a webpage and print their text.

```python
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text)
```

### Assignment 3: CSS Selector Challenge
Locate web elements using CSS selectors, including selectors with wildcards for elements having varying or dynamic attribute values (`^=`, `$=`, `*=`).

**Example task:** Use a CSS wildcard selector to locate elements whose ID starts with `user_`.

```python
driver.find_elements(By.CSS_SELECTOR, "[id^='user_']")
```

### Assignment 4: Child Nodes Using CSS
Identify and locate child/nested web elements using CSS child selectors and interact with the required elements.

**Example task:** Locate a button inside a specific `div` using a CSS child selector.

```python
driver.find_element(By.CSS_SELECTOR, "div.container > button")
```

## ⚙️ Setup & Installation

**🎥 Visual Guide:** For a complete walkthrough of the setup process, please watch the included `Installation Guide.mp4` file located in the root directory.

1. **Clone the repository**
   ```bash
   git clone https://github.com/PratikSamanta14/Wipro-Python-Automation.git
   cd Wipro-Python-Automation
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   Navigate to any assignment folder to install its specific dependencies:
   ```bash
   pip install -r Assignments/assignment-1/requirements.txt
   ```

4. **Run an assignment**
   Execute the target python file within its respective assignment directory:
   ```bash
   python Assignments/assignment-1/assignment1.py
   ```

## ▶️ Usage

Each assignment folder contains a standalone script and a local `index.html` file. Ensure the target webpage URL is correctly pointed to the local HTML file (or a remote server if modified) before running. Execute it directly — the browser will launch, perform the locating/interaction steps, and print or log the results to the console.

## ✅ Learning Outcomes

By completing these assignments, this repo demonstrates:
- Proficiency with all major Selenium locator strategies
- Handling single vs. multiple element retrieval
- Writing robust CSS selectors, including wildcard/attribute-based selectors
- Navigating and interacting with nested DOM structures and XML data such as `Assignments/assignment-4/sample.xml`.

## 🧪 Capstone Project

The `capstone-project/` directory contains a pytest-based e-commerce automation flow for [automationexercise.com](https://automationexercise.com). It uses the Page Object Model, JSON/Excel test data, screenshots, and an HTML execution report.

```bash
cd capstone-project
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
pytest
```

See [`capstone-project/README.md`](capstone-project/README.md) for configuration, browser options, and test details.

## 📜 Certificates & Reports

- `Certificates/` contains completed automation course certificates.
- `Reports/` contains module completion reports.
- `capstone-project/reports/execution_report.html` is generated by the capstone test run.

## 📄 License

This project is for educational purposes as part of coursework/lab assignments.

---
