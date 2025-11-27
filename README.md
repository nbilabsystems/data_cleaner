# ✨ Data Cleaning & Report Generator
<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" />
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen.svg" />
  <img src="https://img.shields.io/badge/Reports-PDF%20Output-orange.svg" />
  <img src="https://img.shields.io/badge/Cleaning-Data%20Pipeline-lightgrey.svg" />
  <img src="https://img.shields.io/badge/Made%20With-Love%20%26%20Python-red.svg" />
</p>

A professional-grade Python tool that loads messy CSV/Excel files, cleans them, generates analytical summary statistics, and produces a polished PDF report. Built for real-world data workflows and designed to be extended into enterprise‑level pipelines.

---

## ✨ Features

- 📥 **Intelligent Data Loading**  
  Auto-detection of CSV/Excel formats with safe error handling.

- 🧹 **Advanced Cleaning Engine**  
  - Duplicate detection  
  - Missing value handling  
  - Numeric/boolean normalization  
  - Automatic datetime conversion  
  - Column name normalization  
  - Transparent change log (per-column notes)

- 📊 **Summary Statistics Module**  
  Global dataset analytics + per-column statistical breakdowns.

- 📄 **PDF Report Generation**  
  Clean, elegant A4 PDF summarizing all cleaning & analysis steps.

- 🚀 **CLI Interface**  
  Run from the command line using arguments:
  ```
  --input
  --output
  --report
  ```

- 🧩 **Modular Architecture**  
  Each component is separated and extendable for enterprise use.

---

## 🧠 Cleaning Engine Overview

The core cleaning logic performs:

- Duplicate removal  
- Type normalization  
- Median fill for numeric values  
- Boolean normalization  
- Datetime standardization  
- Missing-value auditing  
- Per-column action logs  

The engine returns:  
- A cleaned `DataFrame`  
- A `CleaningSummary` object containing all metrics and notes  

---

## 🔄 Before vs After Cleaning

Your dataset is automatically transformed through a multi-stage pipeline.

### **Before Cleaning**
- 5,000 rows  
- 5,456 missing values  
- Inconsistent date formats  
- Columns with mixed data types  
- Random strings in numeric columns  
- Null or corrupted entries  
- No summary statistics  
- No structured PDF report  

### **After Cleaning**
- All numeric columns cleaned and filled with median values  
- Datetime fields normalized to valid `datetime64` format  
- All types enforced (int, float, string, datetime)  
- Clear missing-value reduction  
- Cleaned CSV exported  
- Professional PDF report generated  
- Summary statistics automatically computed  

---

## 🛠 Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd data_cleaner
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### How to Run the DataCleaner Tool

### ▶️ Step-by-Step Instructions

1. **Activate your virtual environment**
   ```bash
   source .venv/bin/activate
   ```

2. **Run the main script**
   ```bash
   python3 main.py
   ```

3. **Enter the path to your CSV file** when prompted.

4. The tool will automatically:
   - Load your dataset  
   - Clean and standardize it  
   - Generate `*_cleaned.csv`  
   - Generate `*_report.pdf`

5. All output files are saved in the project directory.

## 📦 Output Files

After running the tool you will get:

```
your_file.csv  
your_file_cleaned.csv  
your_file_report.pdf  
```

These are fully generated automatically.

## 💻 Example CLI Interaction

```bash
$ python3 main.py
Enter path to CSV file: sample_large_dataset.csv

Loading dataset...
Cleaning...
Generating statistics...
Exporting cleaned CSV and PDF report...

Done! 🎉
Cleaned file: sample_large_dataset_cleaned.csv
Report file: sample_large_dataset_report.pdf

### Basic usage (auto-generated output names)
```bash
python3 main.py --input your_data.csv
```

### Full control over filenames
```bash
python3 main.py     --input raw_data.csv     --output cleaned_data.csv     --report analysis_report.pdf
```

---

## 📦 CLI Arguments

| Argument  | Required | Description |
|----------|----------|-------------|
| `--input` | ✔️ Yes | CSV/Excel path |
| `--output` | ❌ No | Cleaned CSV output path |
| `--report` | ❌ No | PDF report path |

Defaults are derived automatically from the input filename.

---

## 📊 Sample Output

After running:
```bash
python3 main.py --input sample_large_dataset.csv
```

You will get:

- `sample_large_dataset_cleaned.csv`  
- `sample_large_dataset_report.pdf`  
- Full cleaning summary in your terminal  

---

## 📝 Example PDF

The tool generates reports including:

- Rows before/after  
- Missing values before/after  
- Duplicate removal  
- Global dataset metrics  
- Column-by-column breakdown  

The PDF uses **ReportLab** for professional A4 formatting.

---

## 🔭 Future Improvements

This public version is intentionally simplified.  
The internal private version includes (or can include):

- Timestamped reports  
- Automatic schema detection  
- Outlier detection  
- Multi-file batch processing  
- GUI mode  
- API mode  
- Docker packaging  
- Automated email reports  
- Cloud integration  

This repository demonstrates **core engineering quality**, but the production edition can be expanded dramatically.

---

## 🧪 Development Structure

```
data_cleaner/
├── data_loader.py
├── cleaning_engine.py
├── summary_stats.py
├── report_template.py
├── export_utils.py
├── main.py
├── requirements.txt
└── sample data files...
```

---

## 🤝 Author & Notes

This is a demonstration version showcasing real engineering skill.  
The core engine can scale into enterprise-level data cleaning pipelines.

## 📄 License
This project is released under the MIT License.


