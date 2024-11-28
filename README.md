# Frog&Canary Technical Task

This repository contains solutions to two algorithmic challenges implemented in Python. 

1. **Test Plan**: Test plan contains the test cases for the camera functionality in the BDD format
2. **Alphanumeric Sort**: Sorts a string with mixed characters based on specific rules.
3. **Background Script**: Manages file operations in a "tmp" folder.

---

## 📋 Project Structure & Setup

```

├── alphanumeric_sort.py        # Implementation of the alphanumeric sorting algorithm
├── background_script.py        # Implementation of the background script for file management
├── tmp/                        # Temporary folder (created automatically by the script)
├── README.md                   # Project documentation

---

Setup: 

git clone git@github.com:AttiaMinAllah/frog-canary.git
cd <repository-folder>

Execution
python3 alphanumeric_sort.py
- enter any string input and get it sorted
python3 background_script.py

- Add test files(test_file.txt) in tmp folder once its been created so you see the folder being zipped 

---

🎯 Design Decisions & Tradeoffs
Testplan: I write test cases in BDD format because BDD tests are ready to be automated and easy to read. 

Alphanumeric Sort
Approach: Python's sorted() function with a custom key to define character precedence.
Why?: Simple and efficient for small strings but may require optimization for large inputs.

Background Script
Approach: Uses Python's os and tarfile modules to manage files and archiving.
Why?: Exits after processing 10 files. Can be extended for continuous monitoring or larger file counts.



