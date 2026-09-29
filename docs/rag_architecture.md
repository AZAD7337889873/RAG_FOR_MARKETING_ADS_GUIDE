# RAG Architecture

## Objective

The RAG layer provides marketing knowledge and business rules to the
LLM.

The LLM should not be responsible for inventing historical campaign
performance.

Historical performance should come from the structured campaign data.

ML predictions should come from the trained models.

RAG should provide domain knowledge and business rules.


## Knowledge Sources

The knowledge base contains:

### Platform Guidelines

- Google Ads
- Meta Ads
- TikTok Ads
- LinkedIn Ads
- Amazon Ads

### Marketing Strategy

- Budget allocation
- Campaign optimization
- CTR optimization
- Conversion optimization
- ROAS optimization

### Business Rules

- Recommendation rules
- Budget rules


## RAG Pipeline

```text
Knowledge Documents
        |
        v
Document Loader
        |
        v
Text Chunking
        |
        v
Embeddings
        |
        v
Chroma
        |
        v
Retriever
        |
        v
Relevant Context
        |
        v
Prompt
        |
        v
Ollama