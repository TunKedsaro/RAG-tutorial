## Retrieval-efficiency techniques beyond vanilla dense search

1. **HyDE (Hypothetical Document Embeddings)**  *
    – Generate a pseudo-answer or doc with LLM → embed → retrieve against DB.  
    – Helps when the query is short/ambiguous.
    
2. **Query Expansion / Rewriting**  
    – Synonym expansion, sub-query decomposition, history-aware rewrites, multi-lingual rewrites.  
    – Increases recall by covering different phrasings.
    
3. **Multi-Query Retrieval (MQR)**  
    – Generate several variations of the query, embed all, retrieve top-K from each, then merge results.
    
4. **Reranking with Cross-Encoders**  *
    – After retrieval, use a heavier cross-encoder (e.g., miniLM-cross-encoder) to reorder.  
    – Higher precision, especially when initial recall is noisy.
    
5. **Hybrid Retrieval (Sparse + Dense)**  
    – BM25/keyword + dense vectors (ANN).  
    – Handles cases where keywords matter (names, numbers, rare entities).
    
6. **Reciprocal Rank Fusion (RRF)**  
    – Merge multiple retrieval methods (BM25, dense, multi-query) with reciprocal ranking.  
    – Strong ensemble baseline.
    
7. **MMR (Maximal Marginal Relevance)**  
    – Diversify retrieved results (balance relevance vs novelty).  
    – Prevents redundancy, covers more angles.
    
8. **Pseudo-Relevance Feedback (PRF / Rocchio)**  
    – Use top-N retrieved docs to re-formulate query vector → second retrieval.  
    – Similar spirit to classical IR feedback loops.
    
9. **Learning-to-Rank (LTR)**  
    – Train a reranker on your labeled query-doc pairs.  
    – Outperforms static heuristics if you have eval data.
    
10. **Late Interaction Models (ColBERT-style)**  
    – Efficient interaction between query tokens & doc tokens at retrieval stage.  
    – Often balances precision with scale.
    
11. **Caching / Pre-computation**  
    – Cache embeddings for hot queries.  
    – Pre-compute doc summaries/answers for frequent intents.
    
12. **Approximate NN Tricks (HNSW, PQ, IVF)**  
    – Not about quality but efficiency/latency scaling.  
    – You trade off recall vs speed vs memory.