# ga4-bigquery-ml-pipeline
End-to-end data pipeline analyzing user hesitation and purchase probability using GA4, BigQuery, and R.

```mermaid
graph TD
    subgraph Phase 1: Data Collection
        User(User Browser) -->|Scroll & Idle Behavior| GTM[GTM: Custom Listeners]
        GTM -->|Enriched Event Dispatch| GA4[(GA4 Cloud)]
    end

    subgraph Phase 2: Data Engineering
        GA4 -->|Raw Nested Export| BQ{BigQuery: SQL Layer}
        BQ -->|Unnest & Harmonize| Flat[(Flat Analytical Table)]
    end

    subgraph Phase 3: Analysis & Visualization
        Flat -->|Data Import| R_Env[R Studio: Statistical Modeling]
        Flat -->|Live Connection| Looker[Looker Studio: Business Dashboard]
        
        R_Env -.->|Export Insights| Looker
    end

    %% Styling to make it visually attractive
    style Phase 1 fill:#f9f2f4,stroke:#333,stroke-width:2px
    style Phase 2 fill:#e2f0cb,stroke:#333,stroke-width:2px
    style Phase 3 fill:#cdecf9,stroke:#333,stroke-width:2px
