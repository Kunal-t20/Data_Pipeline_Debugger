# Machine Learning Pipeline Debugger

A lightweight, rule-based debugging tool for machine learning pipelines that detects, classifies, and explains common ML failures using structured logs and a knowledge base.

The goal is to help engineers quickly understand what failed, why it failed, and how to fix it, without relying on black-box AI decisions.

# Problem

Machine learning pipelines frequently fail due to:

Schema changes

Missing features

Invalid or corrupted data

Shape mismatches

Resource limits

Unstable or non-converging training

These failures usually appear as long, noisy logs that require manual debugging and repeated searches.

This tool converts raw logs into structured, explainable debugging output.

Core Philosophy

Rules decide.
Retrieval explains.

Error classification is deterministic and rule-based

Knowledge retrieval is used only for explanation

The system avoids guessing when confidence is low

This keeps the debugger predictable, explainable, and reliable.

## High-Level Flow
Log File
  → Ingestion
  → Parsing
  → Classification (WHAT failed)
  → Root Cause Analysis (WHY it failed)
  → Knowledge Base Retrieval (HOW to fix)
  → Suggestions

## Project Structure

```
.
├── config/
│   └── setting.yaml
├── data/
│   └── sample_log/
├── docs/
│   └── error_catlog.md
├── src/
│   ├── ingestion/
│   ├── parsing/
│   ├── classification/
│   ├── analysis/
│   ├── knowledge_base/
│   ├── suggestion/
│   ├── utils/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```


# Key Components
Ingestion

Safely loads log files and handles missing or invalid inputs.

Parsing

Converts raw logs into structured error events.

Classification

Uses rule-based logic to categorize errors such as:

SchemaMismatch

MissingColumn

DataQuality

ShapeMismatch

ResourceLimit

TrainingInstability

ConvergenceFailure

Unknown

Root Cause Analysis

Explains why the error likely occurred in plain language.

Knowledge Base

Retrieves relevant documentation using:

Sentence Transformers for embeddings

FAISS for similarity search

This layer supports explanation only and never affects decisions.

Suggestions

Provides short, actionable steps to fix the issue.

Example Output
Category   : SchemaMismatch
Stage      : preprocessing
Confidence : 0.85

Root Cause:
Input data structure or data type does not match what the model was trained to expect.

Related Guidance:
The structure of the data is different from what the pipeline expects.
This usually happens when column types change or categorical values appear
where numeric values are required.



## Installation
pip install -r requirements.txt

## Usage
python src/main.py


Log paths and document paths can be updated in main.py or moved to configuration later.

Design Decisions

Rule-based classification instead of LLM decisions

Retrieval used only for explanation, not control

Modular, layered architecture

Minimal dependencies

CLI-first design


## Future Improvements

CLI arguments for log paths

Config-driven behavior via setting.yaml

MLflow integration

Improved suggestion engine

Web or API interface