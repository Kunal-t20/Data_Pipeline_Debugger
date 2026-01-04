Error Catalog — Machine Learning Pipeline Debugger

In a machine learning pipeline, errors usually occur when the data shape or content does not match what the model was trained to handle.

This catalog explains five common error categories in simple language.



1️⃣ SchemaMismatch
What it is

The structure of the data is different from what the pipeline expects (for example, column names or data types do not match).

Why it happens

Column renamed
e.g., User_ID → ID

Data type changed
e.g., numeric Price becomes text "Contact for Price"

Extra / unexpected columns added

Impact

Pipeline may crash

Or produce incorrect results

Fix

Validate schema before model input

Convert data types properly

Define strict schema rules

Prevention

Enforce schema contracts

Fail early when schema changes

Add validation tests



2️⃣ MissingColumn
What it is

A required feature/column is completely missing.

Why it happens

Dropped during preprocessing

API / database did not send it

Developer forgot to extract it

Fix

Restore or backfill missing features

Update extraction logic

Prevention

Automatic checks for required features

Schema validation before inference



3️⃣ DataQuality
What it is

The pipeline runs, but the data is invalid or unreliable.

Common issues

Missing values

Impossible values (e.g., Age = −500)

Duplicate rows

Data drift over time

Garbage In → Garbage Out

Fix

Clean missing values

Handle outliers

Remove duplicates

Monitor drift

Prevention

Add validation rules

Track data distributions



4️⃣ ShapeMismatch
What it is

The size (shape) of the data does not match what the model expects.

Why it happens

Wrong batch size

Incorrect reshape

Deep-learning layer mismatch

Fix

Check and verify tensor shapes

Standardize feature pipeline

Prevention

Shape checks in preprocessing

Unit tests for input format



5️⃣ InferenceFailure
What it is

Prediction fails during the final inference step.

Why it happens

Out of memory

Timeout

Unseen input / unexpected values

Serialization failure

Fix

Handle unknown inputs

Improve resource allocation

Add retry or fallback logic

Prevention

Production inference checks

Model validation before deployment

Monitoring & alerts



# summary:

| Error Type       | Meaning                         |
| ---------------- | ------------------------------- |
| SchemaMismatch   | Data structure changed          |
| MissingColumn    | Required field missing          |
| DataQuality      | Data is messy or invalid        |
| ShapeMismatch    | Data size doesn’t match         |
| InferenceFailure | Model crashes during prediction |



### Philosophy

> **Rules decide.  
RAG only explains.**

This keeps the system:
✔ Predictable  
✔ Explainable  
✔ Reliable