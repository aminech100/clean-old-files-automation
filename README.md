# 🧹 File Cleanup Automation Script

A lightweight and efficient Python utility designed to automate the maintenance of local directories by safely purging files older than a specified age limit.

## 🚀 Features

- **Age-Based Filtering:** Automatically checks file modification timestamps (`os.path.getmtime`) and compares them against a customizable day limit (default: 10 days).
- **CLI Integration:** Accepts target folder paths directly via command-line arguments using `sys.argv`.
- **Safe Validation Checks:** Verifies directory existence before execution and isolates logic strictly to files, skipping nested directories safely.
- **Execution Summary:** Outputs a detailed console report summarizing total files deleted and preserved during the cleanup session.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `os`, `sys`, `time`, `datetime`

## 📦 Usage

Run the script from your terminal by passing the target directory path as an argument:

```bash
python main.py /path/to/target/folder
```
