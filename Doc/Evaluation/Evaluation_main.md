# 10 metrics to evaluate recommender and ranking systems

ref : https://www.evidentlyai.com/ranking-metrics/evaluating-recommender-systems

### What is a recommender system?
- A recommender system is a specialized information filtering system, trained to predict user preferences or ratings for a given item.
- The goal of recommendation system is rank documents relevant to a particular query.
- It's returns a list of sorted items that might be relevant for a specific user.
- In a technical sense, The recommender system is to establish a mapping function to predict the utility for various user-item pair then sort the items bases on their calculated utility.
### Evaluation principles
- Input data that we want 
	- ==Predictions==
	- ==Ground truth==
- Before putting recommender system we should evaluation it offline before.
- When we monitor live recommendation on a e-commerce website we can monitor it then got more data detail like ==user clicks==, ==upvote==, ==purchase==
- Building a proper ==event-tracking process== within the application to capture necessary user actions is crucial to production recommender system monitor

### What is the relevance?
- Relevant recommendation are the ==good and accurate of recommendation system==
- ==We have to record the chosen action and match it with a recommended item==
- Relevance is often a simple binary score
	- Did the user click on it?
	- Did the user give it a like?
	- Add it to cart?
- Relevance can be graded relevance score.
	- We can assign specific values to different user action like
		- 1 -> if the user click on an item
		- 2 -> if they save it as a favorite
		- 3 -> if they add it to the cart
		- 4 -> if they complete the purchase
	- Then use simple rule base like 1-3 is dislike (0) and 4-5 is like (1)
### Top K
- Top K parameter is the evaluation cutoff point. (It's represent the number of top-ranked items to evaluate)
- It's like we can focus on top 10 recommendations only.
### Type of metrics
- To evaluate a recommendation or ranking system we need 
	- The model predictions
	- The ground truth
	- The K
- ![[07.png]]
- We can group the recommender or ranking quality metric into three categories
	- 1. Predictive metric
		- Reflect the "correctness" of recommendations 
		- Show how well the system finds relevant items
	- 2. Ranking metric
		- They reflect the ranking quality
		- How well the system can sort the items from more relevant to less relevant
	- 3. Behavioral metrics
		- These metrics reflect specific properties of the system
		- Such as how diverse or novel the recommendations are

### Map flow
- Predictive quality metric
	- Precision at K
	- Recall at K
	- F-score
- Ranking quality metrics
	- MRR
	- MAP
	- Hit rate
	- NDCG
- Behavioral metrics
	- Diversity
	- Novelty
	- Serendipity
	- Popularity bias


### Predictive quality metrics
- ==If your system has a binary relevance label, you can borrow metrics from classification task such as  Precision@K, Recall@K and F-measure
	- ##### Precision@K
		- It's measures the proportion of relevant items among the top K items
		- But there is a rub. Precision values vary depending on the number of relevant items a user has. If there are a total of 3 relevant items the maximum precision at ten is capped at 30%
		- ==It's makes it hard to compare or average Precision across all users in the dataset==
		- ![[08.png]]
	- ##### Recall@K
		- It's measures the coverage of relevant items in the top K.
		- Recall help measure coverage how many relevant items the system captured in the top K.
		- It's works well for applications with only few relevant items
		- ![[09.png]]
	- ##### F-score
		- F Beta score is a metric that balances Precision and Recall.
		- The F Beta score is a good metric when you care about both properties between correctness of prediction and ability to cover as many relevant items as possible with the top-K
		- ![[10.png]]
		- ![[11.png]]
		- The Beta > 1 -> Prioritize recall
		- The Beta < 1 -> 
	- Limit is It's hard to compare with other field list like this situation
	- ![[12.png]]
### Ranking quality metrics
- It's assess the ability to order the items based on their relevance to the user or query.
- For ideal scenario all the relevant items should appear ahead of the less relevant.
	- MRR (Mean Reciprocal Rank) 
		- Shows how soon you can find the first relevant item.
		- ![[14.png]]
	- 