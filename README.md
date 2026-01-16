

# GenAI Document Summarization Pipeline on AWS

## Overview
This repository contains a technical assessment solution for designing and partially implementing a **GenAI-powered Document Summarization Pipeline using AWS services**.  
The goal of this project is to demonstrate practical understanding of **GenAI concepts, AWS architecture decisions, prompt engineering, error handling, and cost/performance trade-offs**, rather than building a production-ready system.

The pipeline accepts user-uploaded documents, processes and chunks them when required, dynamically generates summarization prompts, and uses **Amazon Bedrock (Claude 3 Sonnet)** to produce concise and accurate summaries.

---

## Architecture Summary

The solution is designed using a **serverless and event-driven architecture** on AWS:

- **Amazon S3** – Stores uploaded documents and final summaries
- **AWS Lambda** – Handles document processing, chunking, and orchestration logic
- **Amazon Bedrock (Claude 3 Sonnet)** – Performs GenAI-based document summarization
- **AWS Step Functions** – Orchestrates the end-to-end workflow
- **Amazon API Gateway** – Exposes upload and summary retrieval APIs
- **Amazon CloudWatch** – Logging, monitoring, and observability

This architecture ensures scalability, fault tolerance, low operational overhead, and controlled costs.

---

## Repository Structure

```

document-summarization-pipeline/
│
├── src/
│   ├── bedrock_client.py        # Bedrock inference with safe fallback
│   ├── document_processor.py   # Document reading, chunking, metadata extraction
│   ├── prompt_engineering.py   # Dynamic prompt construction logic
│   ├── retry_logic.py          # Exponential backoff retry handling
│   └── sample.txt              # Sample input document
│
├── README.md                   # Project overview (this file)
└── requirements.txt            # Python dependencies

````

---

## Implementation Highlights

### 1. Document Processing
- Reads plain-text documents from file paths
- Estimates token count based on character length
- Automatically splits documents exceeding 5,000 tokens
- Returns structured metadata including chunk count and token estimates

### 2. Prompt Engineering
- Dynamically adjusts summarization style based on document length
- Handles edge cases such as empty or very short documents
- Enforces factual accuracy and prevents introduction of external information

### 3. GenAI Inference
- Uses **Claude 3 Sonnet via Amazon Bedrock**
- Configured with low temperature to reduce hallucinations
- Includes a safe mock fallback for local execution without AWS credentials

### 4. Error Handling & Retry Logic
- Simulates transient AWS failures
- Implements exponential backoff retry strategy
- Logs attempts, failures, and final outcomes

---

## GenAI Safety Considerations

- **Hallucination Mitigation**:  
  Controlled prompts, chunk-level summarization, low temperature, and explicit instructions to avoid adding new information.

- **Prompt Injection Protection**:  
  Clear separation of system instructions and user content, structured prompt templates, and input validation.

- **Cost Optimization**:  
  Model selection trade-offs, document chunking, caching, and batch-oriented processing.

---

## How to Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
````

2. Run individual components:

```bash
python src/document_processor.py
python src/prompt_engineering.py
python src/retry_logic.py
```

3. Bedrock inference:

* Requires AWS credentials and Bedrock access
* Automatically falls back to a mock response if credentials are unavailable

---

## Notes

* This project is **intentionally not production-hardened**
* Focus is on **architecture decisions, GenAI reasoning, and AWS integration**
* Designed for **technical assessment and evaluation purposes**

---

## Author

**Sonu Kumar**
AI / GenAI Engineer
AWS • Python • Prompt Engineering • LLM Systems

```
