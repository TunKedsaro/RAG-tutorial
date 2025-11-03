source : https://www.evidentlyai.com/ranking-metrics/mean-reciprocal-rank-mrr

- Mean Reciprocal Rank (MRR) is one of the metrics that help evaluate the ==quality of recommendation and information retrieval systems==.
- MRR reflect how soon on average we can find a relevant item for each user within the first K position.
- It's helps understand the average of the first relevant item across all user lists.
- ![[13.png]]
- ![[14.png]]
- Mean Reciprocal Rank (MRR) is a ranking quality metric. It considers the position of the first relevant item in the ranked list.
- ==We can calculate MRR as the mean of Reciprocal Ranks across all users or queries.==
- MRR values in range from 0 to 1, where "1" indicates that the first relevant item is always at the top.
- ==Higher MRR means better system performance==.

### Identify relevant items
- ![[Pasted image 20251029162019.png]]
- when we want to measure ranking metrics MRR needs the ground truth. We mush identify which 
- We can use something like capture which ones they clicked then tread it as reflection of relevance.
- ==All we need is a binary "yes" or "no" for every recommended item.==

### How to interpret the MRR
- value is ==0<= MRR <= 1==
- MRR = 1 : when the first recommendation is always relevant
- MRR = 0 : when there are no relevant recommendations in top-K.

### What is a good MRR?
- It's depend on use case
- Example if we have a recommender system that suggests a set of five items out of many thousand possibilities, an MRR of 0.2 might be acceptable. (This mean 0.2 -> 2/10 -> 1/5 user gonna got relevant item at position 5

### Pros and Cons of the MRR
- MRR is excellent for scenarios with a single correct answer
- MRR is easily interpretable (It's easy to explain with other one or stakeholder)
- MRR disregards the relevance of items beyond the first one.