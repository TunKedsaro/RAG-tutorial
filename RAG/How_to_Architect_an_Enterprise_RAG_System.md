source : https://galileo.ai/blog/mastering-rag-how-to-architect-an-enterprise-rag-system

- This give us about professional and enterprice RAG system practice.
- This is Architecture of RAG
![[01.png]]
1. User authentication
	1. Access Control
	2. Data Security
	3. User Privacy
	4. Legal Compliance
	5. Accountability
	6. Personalization and Customization
2. Input guardrail
	1. Anonymization
	2. Restrict substrings
	3. Restrict topics
	4. Restrict code
	5. Restrict language
	6. Detect prompt injection
	7. Limit tokens
	8. Detect tocixity
3. Query rewriter
	1. Rewrite based on history
	2. Create subqueries
	3. Create similar queries
4. Encoder
	1. Leveraging MTEB benchmarks
	2. Custom evaluation
	3. Evaluation by annotation
	4. Evaluation by mode
	5. Evaluation by clustering
	6. How to Select a Text Encoder
	7. Querying cost
	8. Indexing cost
	9. Storage Cost
	10. Language Support
	11. Search Latency
	12. Privacy
5. Document ignestion
	1. Document parser
	2. Document formats
	3. Table recognition
	4. Image recognition
	5. Metadata extraction
	6. Chunker
	7. Indexer
	8. Scalability issues
	9. Real-time index updates
	10. Consistency and atomicity
	11. Optimizing storage space
	12. Security and access control
	13. Monitoring and maintenance
6. Data storage
	1. Embeddings
	2. Documents
	3. Chat history
	4. User feedback
7. Vector database
	1. Recall VS Latency
	2. Cost
	3. Insertion speed VS Query speed
	4. In-memory VS On-disk index storage
	5. Full-Text search VS Vector Hybrid search
	6. Filtering
	7. Techniques for improving retrieval
8. Hypothetical document embeddings (HyDE)
	1. Query routing
	2. Reranker
	3. Maximal Marginal Relevance (MMR)
	4. Autocut
	5. Recursive retrival
	6. Sentence window retrieval
9. Generatorr
	1. API considerations
	2. Performance
	3. Generatioin quality enhancers
	4. Security
	5. User experience
	6. Self-hosted inference
	7. Private API services
	8. Prompting techniques for improving RAG
	9. Output guardrail
	10. User feedback
	11. User interaction and feedback collection
	12. Issue identification and diagnostic inspection
	13. Data improvement strategies
	14. Evaluation and testing protocols
10. Observability
	1. Prompt analysis and optimization
	2. Traceability in LLM applications
	3. Information retrieval enhancement
	4. Alerting
	5. Caching
	6. Enhanced production inference
	7. Accelerated development cycles
	8. Data storage
	9. Multi-tenancy