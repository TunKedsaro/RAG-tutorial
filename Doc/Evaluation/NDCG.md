source : https://www.evidentlyai.com/ranking-metrics/ndcg-metric
- NDCG 
	- is metric that evaluate the quality of recommendation and information retrieval system.
	- It's compares rankings to an ideal order where all relevant items are at the top of the list
	- NDCG can handle binary and numerical relevance score
- NDCG helps measure a machine learning algorithm's ability to sort items based on relevance.
- NDCG = DCG / ideal DCG
- We can aggregate the NDCG results across all users to get overall measure of the ranking quality in the dataset
- Value range ==0 <= NDCG <= 1==
- ==NDCG is a metric that help evaluate the ranking quality with a similar priciple==
	- We assume that there is ideal ranking with all the items sorted in decreasing order
	- NDCG help to measure how close the alg output comes to this perfect order.
- ![[Pasted image 20251030150521.png]]

### NDCG formula
![[Pasted image 20251030151055.png]]

### Relevance score
- It's a ground truth or target value necessary for evaluating ranking system quality
	- binary level => 0,1
	- numerical score => 1 - 5
- A ranking or recommender system typically returns a sorted list of the relevant items. ==if you deal with search and retrieval, this can be a list of items or answers most relevant to a specific query==
- To evaluate ranking quality We have to got Ground truth to the that we get from user like 
	- Click rate
	- E commerce : 
		- Click -> 1
		- adding favorite -> 2
		- Putting basket -> 3
		- Complete -> 5
	- ==But this way is very complex to implement in production==
- The best way is having a binary option "Relevant or Not" label
- When we have the ground truth, we can define how good of our system is by comparing the ranked list.

### Cumulative gain (CG)
- ![[Pasted image 20251030154739.png]]
- The cumulative gain is a sum of scores of all relevant items among the top-K results in the list.
- Example
	- binary : if we recommend 5 item and user click 3 of 5 we got CG = 1+1+1 = 3
	- Grade : if we recommend 5 item then user interesting it we got CG =5+5+5+5+5 = 25
- The limitation is It's not take into account the ordering if we change the position of the relevant items the outcome will be the same.
![[Pasted image 20251030160325.png]]
- If we swap position the cummulative gain stays the same
- but we know that for recommendation system the second is better than first
- So we should add something to discount the point

### Discounted gain (DCG)
![[Pasted image 20251030160456.png]]
- ==We will add weight to relevant items that appear lower==
- ==A common way to add this for industry is a logarithmic penalty==
- - ![[Pasted image 20251030162822.png]]
- ![[Pasted image 20251030162802.png]]
- Let's take an example of DCG computation
- ![[Pasted image 20251030163045.png]]
- ==But there are limitation sometime DCG@10 > DCG@3 It's not becuase It's better but because the length of list so we have to sue NDCG==

### Normalized DCG (NDCG)
![[Pasted image 20251030163828.png]]!
![[19.png]]

### Interpretation
- Value range 0<= NDCG <= 1
- Meaning
	- 1 is best sort like ideal
	- 0 is worse
