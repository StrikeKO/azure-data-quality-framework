# \# azure-data-quality-framework

# 

# Reference implementation that demonstrates the Azure, Databricks, and Data Quality engineering skill set.

# ---

# 

# \## Key Features

# 

# \* \*\*Databricks (PySpark)\*\* streaming \& batch pipelines

# \* \*\*Great Expectations\*\* rule sets covering completeness, accuracy, timeliness, validity, consistency, uniqueness

# \* \*\*Real‑time alerts\*\*: Azure Functions posts to Teams/email when thresholds are breached

# \* \*\*Metrics lakehouse\*\*: Delta tables in Cosmos DB \& Power BI dashboards

# \* \*\*CI/CD\*\*: GitHub Actions with lint‑test‑deploy, Terraform IaC

# 

# \## Architecture

# 

# ```

# (Event Hub) ==> Databricks Bronze ==> GE DQ Checks ==> Silver ==> Metrics Writer ==> Cosmos DB/Power BI

# &nbsp;                                        ↑                              ↓

# &nbsp;                                    Azure Function  <==  Threshold Breach

# ```

# 

# \## Quick Start

# 

# 1\. \*\*Clone\*\*

# 2\. \*\*Provision\*\* Azure resources: `cd terraform \&\& terraform init \&\& terraform apply`

# 3\. \*\*Import notebooks\*\* into Databricks \& run `01\_ingest\_streaming.py`

# 4\. Configure expectations in `dq/expectations.yml` and schedule with Jobs API

# 5\. Run `scripts/deploy\_alerts.sh` to create Function app for notifications

# 

# \## Repository Structure

# 

# ```

# ├── notebooks/

# │   ├── 01\_ingest\_streaming.py

# │   ├── 02\_batch\_etl.py

# │   └── 03\_quality\_metrics.py

# ├── dq/

# │   ├── expectations.yml

# │   └── checkpoints.yml

# ├── terraform/

# │   └── main.tf

# ├── scripts/

# │   └── deploy\_alerts.sh

# └── README.md

# ```

# 

# 



