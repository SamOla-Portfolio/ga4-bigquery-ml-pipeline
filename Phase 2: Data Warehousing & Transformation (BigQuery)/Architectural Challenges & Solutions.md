In this phase, the goal was to take the raw, messy data from Google Analytics and turn it into a clean, organized table ready for statistical analysis. This was done natively using SQL in Google Cloud's BigQuery.

**The Engineering Process**
1. Flattening the Data (Unnesting)
Raw GA4 data is nested, meaning multiple pieces of information are bundled together in a single row. I wrote SQL queries to "unpack" this data, organizing it so that every row clearly represents a single user session alongside its specific behavioral metrics (like hesitation time and scroll depth).

2. Handling Naming Changes (Schema Drift)
Data systems sometimes change how they name variables over time. I designed the SQL logic to be flexible, ensuring the pipeline continues to capture the correct target variables even if the underlying parameter names shift slightly in the backend.

3. Fixing Split Numbers (Data Type Correction)
A common quirk with GA4 data is that it sometimes splits numerical values randomly between "integer" and "decimal" columns. I built SQL logic to evaluate, merge, and fix these split columns back into a single, reliable number.

**The Data Flow**

```mermaid
graph LR
    Raw[Raw GA4 Events] --> SQL[SQL Cleaning & Formatting]
    SQL --> Flat[Clean, Flat Table for Analysis]
