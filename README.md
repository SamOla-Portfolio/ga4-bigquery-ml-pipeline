# ga4-bigquery-ml-pipeline
End-to-end data pipeline analyzing user hesitation and purchase probability using GA4, BigQuery, and R.

```mermaid
graph TD
    Start(User Interaction) --> Consent{Consent Layer}
    Consent -- No --> Privacy[🛑 Privacy Shield: No Data Processed]
    Consent -- Yes --> Engine[🚀 GTM Behavioral Engine]
    
    Engine --> Listeners[Activate Custom Listeners]
    Listeners --> Standard[Standard Event Stream]
    Listeners --> Enrichment[Custom Behavioral Enrichment]
    
    Standard --> Cloud(GA4 Analytics Cloud)
    Enrichment --> Cloud
