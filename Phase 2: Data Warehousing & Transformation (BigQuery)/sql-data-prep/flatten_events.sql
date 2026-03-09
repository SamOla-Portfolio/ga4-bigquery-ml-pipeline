-- =====================================================================================
-- Phase 2: Data Flattening (GA4 Schema to Tabular)
-- Description: Extracts nested event parameters from GA4's native BigQuery export
--              and flattens them into a session-centric format for ML model training.
-- =====================================================================================

WITH session_data AS (
  SELECT
    -- Extract the custom session ID generated during the frontend/API phase
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'session_id') AS session_id,
    
    -- Extract hesitation time (Proxy for cognitive load / psychological friction)
    MAX(IF(event_name = 'hesitation_complete', 
        (SELECT COALESCE(value.double_value, value.float_value) FROM UNNEST(event_params) WHERE key = 'hesitation_time'), 
        NULL)) AS hesitation_time,
    
    -- Extract scroll depth (Proxy for user motivation)
    MAX(IF(event_name = 'scroll_tracking', 
        (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'percent_scrolled'), 
        NULL)) AS scroll_depth,
    
    -- Boolean flag for conversion success (Dependent variable for Logistic Regression)
    MAX(IF(event_name = 'purchase_success', 1, 0)) AS is_buyer
    
  FROM
    -- Uses wildcard (*) to dynamically query all daily batch exports
    `friction-data-warehouse.analytics_526814492.events_*` 
  WHERE
    event_name IN ('hesitation_complete', 'scroll_tracking', 'purchase_success')
  GROUP BY
    session_id
)

SELECT
  session_id,
  hesitation_time,
  scroll_depth,
  is_buyer
FROM
  session_data
WHERE
  session_id IS NOT NULL;
