# Data Pipeline Engineering for E-commerce Analytics

A batch-oriented ELT (Extract, Load, Transform) data pipeline built with DuckDB and Python for analyzing Brazilian e-commerce transactions from the Olist Public Dataset.

## Project Overview

This project transforms the highly normalized Olist Public Dataset (9 CSV files) into an analytics-optimized data model, delivering critical KPIs related to sales velocity, customer distribution, and operational metrics to downstream Business Intelligence tools.

### Key Features

- **Idempotent Pipeline**: Uses `CREATE OR REPLACE TABLE` for reliable re-execution without data duplication
- **Dimensional Flattening**: Core analytical model (`customers_with_orders`) for simplified BI querying
- **Automated Orchestration**: Sequential DAG execution via Python subprocess
- **Analytical Outputs**: Time-series and categorical data exports for BI visualization
- **Local-First Architecture**: Self-contained stack requiring no external cloud dependencies

##  Architecture

### Technology Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Orchestration** | Python (subprocess) | Simple, low-overhead dependency management |
| **Data Warehouse** | DuckDB | In-process, columnar OLAP database for high-performance analytics |
| **Transformation Logic** | DuckDB SQL | Declarative and performant ELT methodology |
| **Data Serving** | Exported CSVs | Standardized output for BI tool consumption |
| **Business Intelligence** | Metabase | Dashboard visualization and reporting |

### Pipeline Flow

```
Raw CSV Files → Load (DuckDB) → Transform (SQL) → Export (CSV) → BI Dashboard
```

The pipeline enforces a strict DAG structure:
1. **Load**: Ingest raw CSV files into DuckDB tables
2. **Transform**: Create denormalized analytical models
3. **Export**: Generate aggregated data for visualization
4. **Serve**: Consume in Metabase for business insights

##  Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Faima1997/olist-data-pipeline.git
cd olist-data-pipeline
```

2. **Install dependencies**
```bash
pip3 install -r requirements.txt
```

### Usage

Run the complete ELT pipeline:
```bash
python3 scripts/batch_pipeline.py
```

This will execute the following stages sequentially:
- Transform data and create analytical models
- Export dashboard data (orders by status, orders by city)
- Export aggregated time-series data (weekly orders)

### Validation

Verify database integrity:
```bash
python3 scripts/show_schema.py
python3 scripts/check_data.py
```

## � Project Structure

```
olist-data-pipeline/
├── data/
│   ├── raw/                          # Source CSV files
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_orders_dataset.csv
│   │   └── ...
│   ├── exported/                     # Output CSV files for BI
│   │   ├── weekly_orders.csv
│   │   ├── orders_by_city.csv
│   │   └── orders_by_status.csv
│   └── olist.duckdb                  # DuckDB database file
├── scripts/
│   ├── batch_pipeline.py             # Main orchestration script
│   ├── load_data.py                  # Data ingestion
│   ├── transform_data.py             # Analytical modeling
│   ├── export_dashboard1_data.py     # Categorical exports
│   ├── export_aggregated_data.py     # Time-series exports
│   ├── show_schema.py                # Schema validation
│   └── check_data.py                 # Data validation
├── requirements.txt
└── README.md
```

## Key Findings

### Temporal Analysis
- **Highest Order Volume**: 3,008 orders during the week starting November 20, 2017
- **Insight**: Sharp peak correlates with Black Friday shopping season, demonstrating the pipeline's capability to capture critical seasonal business events

### Categorical Analysis
- **Top City**: São Paulo dominates transaction volume
- **Business Impact**: Critical for logistical planning and regional marketing strategies
- **Order Success Rate**: 97.02% of orders successfully delivered

##  Analytical Outputs

The pipeline generates three key data products:

1. **weekly_orders.csv**: Time-series data showing order volume trends
2. **orders_by_city.csv**: Top 10 cities by order volume
3. **orders_by_status.csv**: Order fulfillment status distribution

## 🔧 Technical Details

### Data Model

**Core Table: `customers_with_orders`**

| Column | Type | Description |
|--------|------|-------------|
| customer_id | VARCHAR | Join key |
| customer_unique_id | VARCHAR | Analytical dimension |
| customer_zip_code_prefix | VARCHAR | Geospatial dimension |
| customer_city | VARCHAR | Geographic dimension |
| customer_state | VARCHAR | Regional dimension |
| order_id | VARCHAR | Fact key |
| order_status | VARCHAR | Order lifecycle dimension |

### Idempotency Design

All data ingestion uses `CREATE OR REPLACE TABLE` to ensure:
- No data duplication on re-runs
- Pipeline can be safely executed multiple times
- Simplified error recovery and debugging

##  Known Limitations

### Current Architecture Constraints

1. **Fragile Orchestration**: Subprocess-based orchestration lacks built-in fault tolerance and monitoring
2. **Scaling Boundary**: In-process DuckDB limits data volume to available RAM
3. **Model Governance**: Transformation logic embedded in Python files rather than version-controlled SQL

### Recommended for
- Prototypes and proof-of-concepts
- Small to medium datasets (< 100GB)
- Local development and testing
- Single-node analytical workloads

## Future Enhancements

### Planned Improvements

1. **Dedicated Workflow Orchestration**
   - Migrate to Apache Airflow or Prefect
   - Implement professional-grade scheduling and monitoring
   - Add error recovery and retry logic

2. **Transformation Management**
   - Adopt dbt (data build tool) for SQL modeling
   - Implement version control for transformations
   - Add automated testing and documentation

3. **Cloud Readiness**
   - Refactor to cloud-native solutions (AWS/GCP)
   - Implement horizontal scalability
   - Add data lake integration

4. **Git LFS Integration**
   - Migrate large files to Git Large File Storage
   - Improve repository hygiene and clone performance

##  Dashboard Preview

The exported data powers a comprehensive Metabase dashboard featuring:
- Total order metrics (99,441 orders)
- Temporal trends (weekly sales visualization)
- Operational health (97.02% delivery success rate)
- Geographic distribution (customer penetration by state)
- Risk analysis (canceled orders by state)
- Top cities performance metrics

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

##  License

This project was developed as part of the Data Pipeline Engineering course.

## Author

**Fahima PK** - Student ID: 60319693

##  Acknowledgments

- Olist for providing the public e-commerce dataset
- DuckDB team for the excellent analytical database
- Course instructors for guidance and support

---

**Note**: This pipeline was developed for educational purposes and demonstrates batch ELT principles for e-commerce analytics.
