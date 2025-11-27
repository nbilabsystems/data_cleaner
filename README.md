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

## 📄 License

This project is provided under a simple open-source license for educational and portfolio purposes.  
You are free to modify and extend it.

---

## 🤝 Author & Notes

This is a demonstration version showcasing real engineering skill.  
The core engine can scale into enterprise-level data cleaning pipelines.  

