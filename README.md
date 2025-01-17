# CyberScope - A Comprehensive Analysis Repository

## Overview
Welcome to the **CyberScope - A Comprehensive Analysis Repository**, a centralized resource for collecting, analyzing,
and experimenting with publicly available datasets in the cybersecurity domain. This repository is designed to facilitate
exploratory data analysis, model building, and research for a wide variety of use cases, including intrusion detection,
malware analysis, network traffic monitoring, phishing detection, and more.

## Objectives
This repository serves as a one-stop resource to:

1. **Centralize Access to Datasets**: Provide links and summaries for diverse cybersecurity datasets.
2. **Enable Analysis**: Develop scripts, tools, and notebooks to analyze and derive insights from these datasets.
3. **Foster Learning**: Encourage a deeper understanding of cybersecurity through practical, hands-on experimentation.
4. **Support Research**: Help researchers and enthusiasts in building models and conducting experiments in cybersecurity.

---

## Dataset Categories
The following categories of datasets are included in this repository:

### 1. **Network Traffic**
- **Unified Host and Network Dataset**: Host and network events from Los Alamos National Laboratory.
- **Comprehensive, Multi-Source Cyber-Security Events**: 58 days of de-identified data from LANL.
- **CTU-13 Dataset**: Labeled botnet, normal, and background traffic.
- **PCAP Files**: Collection of malware traffic, network forensics, and more.
- **IoT Device Captures**: Traffic from the setup of 31 IoT devices.

### 2. **Malware Analysis**
- **UNSW-NB15 Data Set**: Includes nine families of attacks.
- **Malware Training Sets**: Samples from families like APT1, Crypto, Locker, and Zeus.
- **Microsoft Malware Classification Challenge**: Data from 9 malware families.
- **The Drebin Dataset**: Android malware data with 5,560 applications.

### 3. **Web Application Security**
- **HTTP DATASET CSIC 2010**: Requests for testing web attack protection systems.
- **Web Attack Payloads**: A collection of payloads used in web attacks.
- **Machine-Learning-driven Web Application Firewall**: Good and bad queries for WAF.

### 4. **URLs & Domain Names**
- **Malicious URLs Dataset**: 2.4M URLs labeled as malicious or benign.
- **Ransomware Tracker**: Blocklists for ransomware botnet traffic.
- **URLhaus**: Malicious URLs for malware distribution.

### 5. **Authentication and Host Logs**
- **User-Computer Authentication Associations**: Authentication events over 9 months from LANL.
- **ADFA Intrusion Detection Datasets**: Host-based intrusion detection data.

### 6. **Phishing Detection**
- **Phishing Websites Data Set**: Features for predicting phishing websites.
- **AZSecure Data**: Web forums and phishing-related data.

### 7. **Fraud Detection**
- **Credit Card Fraud Dataset**: Highly unbalanced data of fraudulent transactions.

### 8. **Other Categories**
- **Honeypots**: Data collected from AWS honeypots.
- **Passwords**: Sanitized password frequency lists from Yahoo.
- **Binary Analysis**: Ember dataset for PE file analysis.

---

## Repository Structure

```plaintext
├── dags/                      # Dagster pipelines for orchestrating data workflows
│   ├── pipelines/             # Defined pipelines for ETL, analysis, and ML tasks
│   ├── solids/                # Modular pipeline components for data processing steps
│   └── resources/             # Config files and resource definitions for Dagster
│   └── example.yaml           # Example YAML configuration files for the Dagster pipelines
│
├── datasets/                  # Dataset links, metadata, and raw data storage
│   ├── raw/                   # Raw, unprocessed datasets
│   ├── processed/             # Cleaned and transformed datasets
│   └── metadata/              # Dataset descriptions, schemas, and source information
│
├── notebooks/                 # Jupyter notebooks for exploratory analysis and testing
│   ├── eda/                   # Notebooks for Exploratory Data Analysis (EDA)
│   ├── graph-analysis/        # Graph-based analysis notebooks
│   └── model-experiments/     # Notebooks for model training and evaluation
│
├── scripts/                   # Python scripts for various tasks
│   ├── ingestion/             # Scripts for data ingestion from external sources (Kaggle, APIs)
│   ├── preprocessing/         # Scripts for data cleaning and feature engineering
│   ├── analysis/              # Scripts for statistical and graph-based analysis
│   ├── visualization/         # Scripts for data visualization and dashboards
│   └── utils/                 # Utility functions and helpers (logging, config parsing)
│
├── models/                    # Model files and training logic
│   ├── pre-trained/           # Pre-trained models for baseline comparisons
│   ├── custom/                # Custom models developed for the project
│   └── pipelines/             # ML model pipelines integrated with Dagster
│
├── graphs/                    # Graph-related analysis and data representation
│   ├── graph_data/            # Graph datasets and adjacency matrices
│   ├── graph_scripting/       # Graph-specific Python scripts (NetworkX, PyGraph, etc.)
│   └── graph_visualizations/  # Graph plots and visualizations
│
├── results/                   # Outputs and results from various runs
│   ├── logs/                  # Logs from pipeline runs and error tracking
│   ├── visualizations/        # Plots and charts generated from the analysis
│   └── reports/               # Summarized results and insights (PDF, Markdown, etc.)
│
├── duckdb/                    # DuckDB database integration and queries
│   ├── db/                    # DuckDB database files
│   ├── queries/               # DuckDB SQL queries for data analysis
│   └── utils/                 # Scripts for querying and managing the DuckDB database
│   └── schema/                # Schema definitions for the DuckDB database
│
├── tests/                     # Unit tests and integration tests
│   ├── pipelines/             # Tests for Dagster pipelines
│   ├── data_quality/          # Data validation tests
│   └── models/                # Tests for model accuracy and consistency
│
├── environments/              # Environment and dependency management
│   └── requirements.txt       # Python package requirements
│   └── ...                    # Other environment files
│
├── configs/                   # Configuration files for orchestrators and tools
│   ├── dagster.yaml           # Dagster configuration
│   ├── duckdb.yaml            # DuckDB connection settings
│   └── ml_config.yaml         # ML model and training configurations
│
├── docs/                      # Project documentation
│   ├── architecture.md        # System architecture and design choices
│   ├── usage_guide.md         # How to run pipelines and scripts
│   └── CONTRIBUTING.md        # Contribution guidelines
│
├── .gitignore                 # Ignore unnecessary files and folders
├── LICENSE                    # License information
├── README.md                  # Project overview and usage instructions
└── Makefile                   # Automate common tasks like `make test`, `make run`
```

---

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cybersecurity-dataset-analysis.git
   cd cybersecurity-dataset-analysis
   ```

2. **Set Up the Environment**:
   - Install the required dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

3. **Download Datasets**:
   - Visit the [Kaggle Datasets Page](https://www.kaggle.com) for downloading datasets.
   - Store the downloaded datasets in the `datasets/` directory.

4. **Run Analysis**:
   - Use the notebooks in the `notebooks/` folder to explore datasets.
   - Modify or extend the scripts in the `scripts/` folder for custom analysis.

---

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you would like to:
- Add new datasets.
- Improve existing analysis scripts.
- Report bugs or suggest new features.

---

## License
This repository is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
Special thanks to the organizations and researchers who have made these datasets publicly available, including:
- Los Alamos National Laboratory
- Canadian Institute for Cybersecurity
- Kaggle
- Common Crawl
- And many more contributors to the cybersecurity community.

### Reference Links

- [Cyber-security Datasets - Kaggle](https://www.kaggle.com/discussions/general/335189)

---

## Contact
For any questions or suggestions, please feel free to reach out via GitHub or email.
