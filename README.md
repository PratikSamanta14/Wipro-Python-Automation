# Selenium-PythonAutomation

A collection of hands-on assignments exploring web element identification and interaction using **Selenium WebDriver** with Python. Each assignment builds on the last — starting from basic locator strategies and progressing to CSS selectors for dynamic and nested elements.

## 📋 Overview

| # | Assignment | Core Concept | Status |
|---|-----------|---------------|--------|
| 1 | Web Element Identification | Locating elements with `By.ID`, `By.NAME`, `By.TAG_NAME`, `By.LINK_TEXT`, `By.CLASS_NAME` | ✅ |
| 2 | Multiple Element Identification | Finding and iterating over lists of elements (`find_elements`) | 🔜 |
| 3 | CSS Selector Challenge | CSS selectors with wildcards for dynamic attribute values | 🔜 |
| 4 | Child Nodes Using CSS | CSS child/descendant selectors for nested elements | 🔜 |

## 🛠️ Tech Stack

- **Selenium WebDriver** (Python bindings)
- **WebDriver Manager** (for automatic driver binaries)
- Browser: Chrome / Firefox

## 📁 Repository Structure

```
Selenium-PythonAutomation/
│
├── assignment1_element_identification/
│   └── locate_by_strategies.py
│
├── assignment2_multiple_elements/       
│   └── find_all_links.py
│
├── assignment3_css_wildcard/            
│   └── css_wildcard_selector.py
│
├── assignment4_child_nodes/            
│   └── css_child_selector.py
│
├── requirements.txt
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

1. **Clone the repository**
   ```bash
   git clone https://github.com/Soumick2004/Selenium-PythonAutomation.git
   cd Selenium-PythonAutomation
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` should include:
   ```
   selenium
   webdriver-manager
   ```

4. **Run an assignment**
   ```bash
   python assignment1_element_identification/locate_by_strategies.py
   ```

## ▶️ Usage

Each assignment folder contains a standalone script. Update the target webpage URL at the top of each script before running, then execute it directly — the browser will launch, perform the locating/interaction steps, and print or log the results to the console.

## ✅ Learning Outcomes

By completing these assignments, this repo demonstrates:
- Proficiency with all major Selenium locator strategies
- Handling single vs. multiple element retrieval
- Writing robust CSS selectors, including wildcard/attribute-based selectors
- Navigating and interacting with nested DOM structures

## 📄 License

This assignment repo is for wipro python automation course using selenium.

---
