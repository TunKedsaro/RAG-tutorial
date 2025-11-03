- Mean average precision (MAP) 
	- is a ranking quality metric. It considers the number of relevant recommendations and their position in the list
	- Precision@K told use only how many items that show in K but don't care about order MAP helps address this.
- ==Map @ K is calculated as an arithmetic mean of the Average Precision (AP) at K across all users or queries==
- To compute the Average Precision (AP) @K we must average the precision at each relevant position in the K-long ranked list.
- Range of value is 0 <= MAP <= 1
	- 1 : corresponds to an ideal ranking with all relevant items at the top. (Higher values of MAP mean better performance)

### How to calculate MAP
- ==Mean Average Precision (MAP) @ K is a quality metric that helps evaluate the ability of the recommender or ranking system and return relevant items in the top-K result while placing more relevant items at the top==
- ![[Pasted image 20251029184813.png]]
	- K is a chosen cutoff point
	- U is the total number of users
	- AP is the average Precision for a given ranking list
- For Precision  we have to ==compute Precision for every user list== to get a picture of the "overall correctness"
- ==Optimizing for Precision in top-K would make sense==
- But precision limitation is It's don't care about order of relevant items like this
	- ![[Pasted image 20251029192002.png]]

### Average Precision (AP)
- Average Precision (AP) @K is computed as an average of Precision values at all the relevant positions within K
- ![[Pasted image 20251029194315.png]]
- N : total number of relevant items for a  particular user
- Precision (k) : is the precision calculated at each position
- rel (k) : 
	- 1 if the item at position k is relevant
	- 0 otherwise
![[Pasted image 20251029195142.png]]
- if the relevant items is top 3 the value is 1 if It's not It's less to 0
![[15.png]]

### Intuition behind MAP
- Value of range 0 <= MAP <= 1
- Higher MAP is better
- Meaning
	- MAP = 1 : The case of perfect ranking when all relevant documents are at the top of the list
	- MAP = 0 : No relevant objects are retrieved

- However, Marginal changes in the MAP value between 0 and 1 can be less intuitive.
- We can not got immediate real-world interpretation.



![[16.png]]
![[17.png]]
![[18.png]]


### Summary
- ==This metric helps reflect a combination of valuable properties how many relevant results the model can capture and how well they are usually ranked==
