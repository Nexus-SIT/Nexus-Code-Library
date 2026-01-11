# Nexus Code Library

Welcome to the central code repository for our club. This repository serves two purposes:
1.  **Academic Archive:** A reliable source for syllabus-compliant lab programs.
2.  **Dev Playground:** A space to experiment, optimize simple algorithms, and share scripts.

> **Note to Contributors:** This is not a dump. We follow standard Git workflows. Direct pushes to the `main` branch are disabled. You must submit a Pull Request (PR).

---

## 📂 Repository Structure

We enforce a strict folder hierarchy to keep things organized.

### 1. `academic-labs/` (Strict Compliance)
Code in this directory must match the college syllabus exactly. It is used for reference during exams/labs.
* **Structure:** `sem-no / subject / main.py`
* **Requirement:** Must compile without errors and match lab manual output.
* **No "Refactoring":** Keep it simple and compliant with what the professors expect.

### 2. `playground/` (Open Season)
This is where you show off. Simple programs, algorithms, data structures, and automation scripts go here.
* **Structure:** `Topic / specific_script.py`
* **Requirement:** Clean code, readable variable names, and comments explaining *why* you did it that way.
* **Optimization:** If a program (e.g., `fibonacci.py`) already exists, you can only add yours if it is **faster** or uses a **different algorithm**.

---

## 🚫 The "Auto-Reject" List
Your Pull Request will be closed immediately if:
1.  **You upload Binaries:** No `.exe`, `.o`, `.out`, or `node_modules`. Source code only.
2.  **Bad File Names:**
    * ❌ `prog1.c`, `test.py`, `my_code.cpp`
    * ✅ `binary_search.c`, `wifi_scanner.py`, `linked_list.cpp`
3.  **No Documentation:** Every folder must have a `README.md` or comments explaining how to run the code.

---

## 🛠 How to Contribute

We simulate a real-world open-source environment.

1.  **Fork** this repository.
2.  **Clone** your fork:
    ```bash
    git clone https://github.com/Nexus-SIT/Nexus-Code-Library.git
    ```
3.  **Create a Branch** (Never code on main):
    ```bash
    git checkout -b feature/add-bubble-sort
    ```
4.  **Add your code** and **Commit**:
    ```bash
    git commit -m "feat: added bubble sort algorithm in python"
    ```
5.  **Push** to your fork and open a **Pull Request**.

---

### maintainers
* @ManishRShetty(https://github.com/ManishRShetty)
