![[02.png]]
![[04.png]]
1. Missing content (FP1)
	- A question is posed that cannot be answered with the available documents.
	- The RAG system responds with a message like "Sorry, I don't know"
	- It's maybe question is not clear.
2. Missed the top ranked documents (FP2)
	- Thee answer to a question is present in the document but It' not rank highly enough to be results return.
	- Only the top K documents are returned. K being a value selected based on performance.
3. Not in context (FP3)
	- Documents containing the answer are retrieved from the database but fail to make a context for generating a response.
4. Not extracted (FP4)
	- The answer is present in the context, but the model fails to extract the correct information
	- cause is noise
5. Wrong format (FP5)
	- Output format is not correct that we want.
6. Incorrect specificity (FP6)
	- The output is overly specific, failing to address the user's needs.
7. Incomplete (FP7)
	- Incomplete answers are accurate but lack some information.