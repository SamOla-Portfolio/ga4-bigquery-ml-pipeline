### QA & Troubleshooting

During the development and deployment of this data pipeline, several technical bottlenecks were identified and resolved to ensure data integrity and compliance.

* **Consent Management & Tag Sequencing (Race Conditions):**
    * **Issue:** Asynchronous loading of the Termly Consent Management Platform (CMP) created race conditions, causing Google Analytics 4 (GA4) and Hotjar tags to attempt firing before the consent state was fully resolved.
    * **Resolution:** Restructured Google Tag Manager (GTM) triggers. Shifted the GA4 Configuration tag from `Initialization` to `All Pages` and applied "Additional Consent Checks" requiring `analytics_storage` to be explicitly granted. This eliminated premature cookie deployment and ensured strict GDPR compliance.

* **GA4 Measurement Protocol Validation (Silent Drops):**
    * **Issue:** The Python ingestion script received HTTP 204 (Success) responses, but data was silently dropped by GA4 and failed to reach BigQuery.
    * **Resolution:** Debugged the JSON payload against the GA4 Event Builder strict validation rules. 
        * Corrected the `client_id` format to match browser cookie standards (e.g., `[0-9]+\.[0-9]+`).
        * Replaced reserved event names (e.g., `purchase`) with custom event names to bypass strict e-commerce parameter requirements.
        * Appended mandatory `params` objects to all events and injected server-side `consent` signals (`ad_user_data`, `analytics_storage`) directly into the payload to prevent data filtering.

* **Identity Resolution & Debug Routing:**
    * **Issue:** Synthetic server-side sessions were filtered out of GA4 Real-time reports and the DebugView interface.
    * **Resolution:** Adjusted the GA4 Property's Reporting Identity from `Blended` to `Device-based` to prevent Google Signals from hiding non-browser traffic. Embedded the `debug_mode: 1` parameter (as an integer) into the payload to successfully route test batches to the DebugView endpoint for real-time validation prior to the 500-session production run.
