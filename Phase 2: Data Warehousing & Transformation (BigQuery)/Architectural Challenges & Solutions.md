**Technical Architecture & Constraints Overcome**
# Data Simulation phase
1. Bypassing GA4 "Silent Failures" via Debug Routing

Challenge: The Measurement Protocol API returned HTTP 204 (Success) codes, yet the payload was not surfacing in BigQuery. The API silently drops malformed data during backend processing rather than returning standard HTTP 400 errors.

Solution: Engineered a temporary routing switch to direct Python pipeline traffic to Google's validation endpoint (/debug/mp/collect). This forced the API to return explicit JSON validation messages, exposing the underlying schema conflicts without guessing.

2. Resolving the NAME_RESERVED Schema Conflict

Challenge: Initial payloads explicitly included session_start events to ensure session integrity in BigQuery. However, the debug server revealed that GA4 strictly locks these system-reserved names for client-side tracking, completely rejecting the server-to-server payload.

Solution: Refactored the payload to send only non-reserved custom events (hesitation_complete, scroll_tracking). By passing a consistent session_id and engagement_time_msec parameter inside these custom events, the GA4 backend engine automatically stitches the timeline together and retroactively calculates the session_start metrics.

# Data flatten by SQL

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
