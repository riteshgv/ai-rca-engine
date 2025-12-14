# AI RCA Engine (Self-Learning Log Analyzer)

## Installation

```bash
git clone https://github.com/<your-username>/ai-rca-engine.git
cd ai-rca-engine
pip install -e .

Usage (CLI):
rca --file tests/sample_logs/app1.log

This project is an AI-powered Root Cause Analysis engine that:

- Reads logs from any application or system
- Detects anomalies using ML models
- Uses LLMs for intelligent RCA
- Searches Internet for unknown errors
- Generates real-time fixes and suggestions
- Works via CLI, Web UI, or API
- Self-learns from new logs over time

## Day 1 Progress
- WSL Setup  
- Python Virtual Environment  
- Installed base packages  
- Created full project folder structure  
- Added README  
- Prepared for coding ingestion pipeline (Day 2)

## Day 2 Progress
- Log Ingestion Pipeline
- Completed ingestion module to read raw log files
- Built log_ingestion.py for file loading and JSON normalization
- Added parsers.py to extract timestamp, level, and message
- Ensured clean Python package structure using absolute imports
- Tested ingestion with sample log file using python -m execution
- Confirmed output in structured JSON format
- Prepared clean ingestion flow for preprocessing (Day 3)

## Day 3 Progress
- Preprocessing + Chunking
- Implemented log cleaning and contextual chunking logic
- Added chunker.py for window-based grouping of logs
- Created automated test module test_preprocessing.py
- Successfully downloaded Sentence Transformer model during tests
- Verified module execution using python -m src.preprocessing.test_preprocessing
- Confirmed chunker produces meaningful grouped text blocks
- Preprocessing pipeline now ready for embedding & vector storage

## Day 4 Progress
Embedding + Vector Database
- Implemented embedding pipeline using Sentence Transformer
- Added local vector database using ChromaDB
- Created test script to validate end-to-end “chunk → embed → store → search”
- Successfully generated embeddings and performed semantic search
- System now capable of AI-powered log retrieval for future RCA engine

## Day 5 Progress
Root Cause Reasoning Engine
- Added LLM reasoning layer for RCA using Transformers pipeline (offline model)
- Integrated chunking + embedding + vector search + reasoning
- Built RCAEngine to perform end-to-end analysis
- Implemented test script to validate RCA flow
- System can now ingest logs, search similar incidents, and generate RCA automatically


## Day 7 Progress

- Converted project into installable Python package
- Added CLI executable (rca)
- Enabled system-wide usage via pip
- Verified end-to-end RCA via CLI

## Day 8 Progress

- Implemented evidence-based confidence scoring
- Derived confidence from vector similarity distances
- Removed hard-coded confidence values
- Improved RCA trustworthiness and explainability


## Tech Stack
- Python
- Transformers (later)
- Vector DB (FAISS / Chroma)
- Tavily API for internet search
- FastAPI for Web UI
- Typer for CLI
