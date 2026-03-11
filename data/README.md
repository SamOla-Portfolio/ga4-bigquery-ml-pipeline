## Data Dictionary

This directory contains the datasets used and generated during Phase 2 (Data Processing & Machine Learning) of the Friction Simulation project.

### 1. `raw_ga4_events.csv`
This file contains the raw, denormalized event data exported directly from Google Analytics 4 via BigQuery.
* **Schema:** Follows the standard GA4 BigQuery export schema, including nested and repeated fields (e.g., `event_params`).
* **Note on Nulls:** The dataset contains a high volume of `NULL` values by design. GA4 logs all event types into a single table, meaning columns reserved for specific parameter types (`string_value`, `int_value`, `double_value`) will remain null unless explicitly triggered by the event payload.

### 2. `processed_ml_features.csv`
This is the cleaned, ML-ready dataset generated via SQL transformations in BigQuery. It flattens the nested raw data and aggregates event-level interactions into structured, user-level features.
* **`client_id`** *(String)*: The unique identifier for the simulated user session.
* **`hesitation_seconds`** *(Float)*: The independent variable (Feature - X). Represents the exact time (in seconds) the user spent hesitating before making a decision. Extracted from the `hesitation_time` parameter.
* **`is_buyer`** *(Integer)*: The dependent variable (Target Label - Y). Contains `1` if the user completed a purchase (`purchase_success`), and `0` if the user abandoned the session.
