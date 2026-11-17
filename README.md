# 🧪 Automated Web Testing Suite (Python + Selenium)

An automated functional testing framework built using **Python, Selenium WebDriver, and Pytest** to test critical web authentication workflows, input validation, and error-handling mechanisms.

---

## 🎯 Test Scenarios Covered
| Test ID | Test Scenario | Expected Outcome | Status |
|---|---|---|---|
| **TC-01** | Valid User Login | Access granted, success message displayed | ✅ Automated |
| **TC-02** | Invalid Password Attempt | Error alert: "Your password is invalid!" | ✅ Automated |
| **TC-03** | Non-existent Username | Error alert: "Your username is invalid!" | ✅ Automated |
| **TC-04** | Empty Submission Check | Error alert preventing empty login | ✅ Automated |

---

## 🛠️ Tech Stack
- **Language:** Python 3
- **Automation Engine:** Selenium WebDriver (v4)
- **Test Runner & Assertions:** Pytest
- **Browser:** Headless Chrome
- **Design Pattern:** Explicit Waits & Fixture-based Driver Lifecycle

---

## ⚙️ Setup & Execution

### 1. Clone the repository
```bash
git clone https://github.com/Ankita-tech04/web-automation-testing-suite.git
cd web-automation-testing-suite
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests with detailed output
```bash
pytest -v -s test_login_suite.py
```

---

## 👩‍💻 Author
**Ankita Das**  
- **LinkedIn:** [Ankita Das](https://www.linkedin.com/in/ankita-das-535967319/)  
- **GitHub:** [@Ankita-tech04](https://github.com/Ankita-tech04)
