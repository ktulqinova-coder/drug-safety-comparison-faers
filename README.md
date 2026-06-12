# Comparative Safety Profile Analysis: Ibuprofen vs Acetaminophen

*Based on FDA Adverse Event Reporting System (FAERS) — 20+ million real-world reports*

## About the Project

Ibuprofen and acetaminophen (paracetamol) are among the most widely used
over-the-counter analgesics in the world. But how do their real-world
safety profiles compare?

This project analyzes adverse event reports from the openFDA API to compare:
- the most frequently reported adverse reactions for each drug,
- the structure of **serious** outcomes (hospitalization, death, disability),
- demographic patterns (sex distribution of reports),
- reporting dynamics over time (2004–present).

## Why I Built This

I am a pharmaceutical technologist transitioning into data analytics.
Pharmacovigilance — monitoring drug safety — is a core discipline of my
original profession. In this project I combine domain expertise in
pharmaceuticals with Python-based data analysis.

## Data Source

- **openFDA Drug Adverse Event API** (FAERS database)
- 20+ million publicly available reports submitted to the FDA since 2004
- Data retrieved programmatically via REST API (see `fetch_faers_data.py`)

⚠️ *Disclaimer: FAERS contains spontaneous reports that do not prove
causation. Reporting rates are affected by drug usage volumes and
reporting bias. This analysis describes reporting patterns, not
comparative drug risk. (This limitation is discussed in the notebook.)*

## Key Findings

<!-- Fill in after the analysis. Examples of the format: -->
1. ...
2. ...
3. ...

## What I Did

- **Data collection:** retrieved aggregated statistics through the openFDA
  REST API with Python `requests`
- **Data quality work:** handled inconsistent drug naming
  (brand names vs generic names), unknown/missing demographic values,
  and discussed reporting bias as a data-quality limitation
- **Exploratory analysis:** reaction frequency comparison, serious vs
  non-serious outcome structure, time-series of report volumes
- **Domain interpretation:** explained observed differences
  (e.g., hepatotoxicity signals for acetaminophen vs gastrointestinal
  signals for ibuprofen) from a pharmaceutical standpoint

## Tools

Python · pandas · matplotlib · seaborn · requests · Jupyter Notebook

## Repository Structure

```
├── README.md
├── fetch_faers_data.py        # data collection script (openFDA API)
├── analysis.ipynb             # main analysis notebook
└── data/                      # CSV files produced by the script
```

## How to Reproduce

```bash
pip install requests pandas matplotlib seaborn
mkdir data
python fetch_faers_data.py
jupyter notebook analysis.ipynb
```
