- Precision@K and Recall@K are common metrics that help to evaluate the performance of ranking alg.
- ==Precision@K== (ความแม่นยำ) measure how many items with the top K positions are relevant.
	- It's show how many recommended items are genuinely relevant
- ==Recall@K== (ความครอบคลุม) nmeasure the share of relevant items captured within the top K positions.
	- 
- We can use ==F-score== to balance between Precision and Recall at K.
- Range value of ==Precision==, ==Recall== and ==F-score== is 0 - 1 (Higher values mean better)
- ==Precision== and ==Recall== only reflect the number of relevant items in the top K without evaluating the ranking quality inside a list.
- ==Precision@K==
	- Precision@K = $\frac{\text{Relevant in top K}}{\text{K}}$

- ==Recall@K==
	- Recall@K = $\frac{\text{Relevant in top K}}{\text{All of Relevant}}$

![[06.png]]