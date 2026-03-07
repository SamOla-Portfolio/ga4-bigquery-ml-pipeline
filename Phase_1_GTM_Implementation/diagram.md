**Phase 1: Strategic Behavioral Architecture**
This phase serves as the foundation of the project, focusing on the Data Acquisition Layer. The objective was to design a tracking system that captures high-fidelity "Behavioral Signals" without compromising user privacy or site performance.

# 1. Logic Flow & Privacy Governance
The tracking ecosystem follows a Consent-First architecture. By decoupling behavioral listeners from the core site initialization, we ensure 100% compliance with global privacy standards (GDPR/CCPA).

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
