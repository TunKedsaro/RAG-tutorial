resource : https://www.researchgate.net/publication/389412924_Intelligent_Resume_Evaluation_Tool_Based_on_Machine_Learning_for_Analysis_And_Career_Advancement

![[Pasted image 20251107181250.png]]
IV Project description
1. Upload Resume as
	- Upload PDF, Docx, txt
2. Extract resume
	- PDFplumber for PDF Python-docx for DOCX file
	- Structure data -> raw text
3. Clean & Process Text
	- clean unimportant text to ready to feature extraction
	- unclean text -> clean text
4. Information extraction
	- NLP (Spacy) use for extract data
	- PhraseMatcher is use to match skills with a specific skill list.
	- Every data in rusume extracted to use to analyze in and grading later
5. ML classification
	- Pickle load model
	- text -> model -> numberic featuers
	- TF-IDF
	- Predict the most relevant job categories.
6. Gen score & Recommendation
	- criteria
		- 10 points : Personal information
		- 20 points : schooling
		- 30 points : pertinent ability
		- 50 points : work exp


VI Methodology
A. Data collections
B. Preprocessing and cleaning
- REGEX
C. eature engineer
	- Spacy : Phasematchers
	- 