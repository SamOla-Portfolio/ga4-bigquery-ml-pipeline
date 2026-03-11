### QA Testing & Troubleshooting

During the testing phase, I identified and resolved the following data ingestion issues to ensure the pipeline worked correctly:

* **1. Tag Firing & Consent (GTM)**
  * **Bug:** Tracking tags were firing before the user actually accepted cookies.
  * **Fix:** Updated GTM triggers to require explicit `analytics_storage` consent before firing the GA4 tags, ensuring strict GDPR compliance.

* **2. Invalid Data Format (GA4 API)**
  * **Bug:** The Python script successfully sent data, but GA4 silently rejected it and dropped the events.
  * **Fix:** Used the **GA4 Event Builder** to validate the payload. I corrected the `client_id` format, removed reserved event names, and added the mandatory `params` object to pass Google's strict data filters.

* **3. Invisible Test Data (GA4 Reports)**
  * **Bug:** The Python test sessions were not appearing in GA4 Real-Time reports or DebugView.
  * **Fix:** Added the `debug_mode: 1` parameter to the Python script and changed GA4's Reporting Identity to `Device-based` so the synthetic data could be monitored during the test runs.
