- ==It's assesses how unique the recommended items are to users.==
- It's measures the degree to which the suggested items differ from popular ones
- How to compute ?
	- Negative logarithm (base2) of probability of encountering a given item in a training set.
	- then average the novelty inside the list and across users
- Novelty reflects the system's ability to recommend items that are not well-known in the dataset
### Intuition
- High novelty corresponds -> long-tail items that few users interacted with
- Low novelty corresponds -> popular items