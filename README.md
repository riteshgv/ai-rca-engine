# AI RCA Engine (Self-Learning Log Analyzer)

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


## Tech Stack
- Python
- Transformers (later)
- Vector DB (FAISS / Chroma)
- Tavily API for internet search
- FastAPI for Web UI
- Typer for CLI
