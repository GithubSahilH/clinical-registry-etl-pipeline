# clinical-registry-etl-pipeline
End-to-end data pipeline and business intelligence portal transforming 240k+ rows of fragmented multi-year AIHW clinical data into interactive visual analytics using Python (Pandas) and Tableau.
# Australian Public Health Intelligence Pipeline & Dashboard

## Project Overview
This project demonstrates an end-to-end data engineering and business intelligence solution utilizing the Australian Institute of Health and Welfare (AIHW) Alcohol and Other Drug Treatment Services database. The pipeline ingests over 240,000 fragmented, raw clinical records collected across multi-year registries, standardizes structural anomalies programmatically, and deploys a production-grade interactive executive dashboard.

---

## Technical Architecture

### 1. Extraction & Data Engineering (Python / Pandas)
The primary challenge of this dataset was overcoming historical data fragmentation and quality degradation across independent source files:
* **Schema Drift Mitigation:** Programmatically reconciled column variations (e.g., matching mismatched naming conventions like `TreatmentDays` and `Treatment Duration Days`) into a single, unified database schema.
* **Data Typo Recovery:** Developed an algorithmic string-repair function to target and reverse Excel export errors that corrupted the "10–19" youth age demographic bracket into arbitrary calendar dates ("Oct-19").
* **ASCDO Clinical Decoding:** Engineered a dynamic fallback dictionary mapper based on the Australian Standard Classification of Drugs of Concern (ASCDO). The script automatically decoded numeric indices into categorical strings and handled unexpected values by evaluating the clinical division identifier digits (e.g., mapping code variations to broader drug classes).

The final optimized dataset was compiled into a standardized core repository: `merged_australian_treatment_data.csv`.

### 2. Business Intelligence & Visual Analytics (Tableau)
With a clean data foundation established, the data was modeled within Tableau to build a high-fidelity, interactive analytics suite:
* **Executive Metrics (KPIs):** Built centralized, high-impact scorecards monitoring total caseload volume (240,816 episodes) and computing the precise system-wide average duration of care (50.04 days).
* **Demographic Intake Matrix:** Deployed a data heatmap highlighting high-volume patient clustering across validated age groups and primary substances.
* **Operational Care Pathways:** Structured horizontal stacked bar charts detailing treatment modality distributions (Counselling vs. Rehabilitation vs. Withdrawal/Detox) ranked by substance demand.
* **Interactive Cross-Filtering:** Configured dashboard action filters enabling users to click specific demographic segments in the matrix to dynamically filter operational resource insights across the entire application interface.

---

## Key Clinical Insights
* **System Capacity & Load:** Successfully mapped a total operational footprint of 240,816 patient episodes with a system mean treatment window of 50.04 days.
* **Resource Optimization:** While standard outpatient counseling manages the highest absolute patient traffic volume, high-acuity, substance-dependent modalities (like residential detox and rehabilitation units) require tighter strategic bed-allocation management.

---

## Repository Structure
* `/scripts` : Contains the automated Python data cleaning, schema merging, and dictionary decoding scripts.
* `/data` : Directory for data schema references (Note: Raw datasets are omitted or zipped due to scale).
* `/dashboards` : Contains the packed Tableau Workbook (`.twbx`) file.
* `/assets` : High-resolution images and screenshots of the operational dashboard interface.
