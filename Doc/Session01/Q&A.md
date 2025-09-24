Q : Chunk คืออะไร ? และการแบ่ง Chunk ควรทำอย่างไร?
A : Chunk คือส่วนย่อยๆของข้อมูล (เช่น ข้อความ) ที่ถูกแบ่งออกมาจากเอกสารหรือต้นฉบับที่มีขนาดใหญ่ เพื่อให้ง่ายต่อการประมวลผลโดย Embedding Model และ LLM หลักการแบ่ง Chunk มีหลายวิธี เช่น
- แบ่งตาขนาดคงที่ (Fixed-size)
- แบ่งตามตัวคั่น (Recursive Character Splitting)
- แบ่งตามความหมาย (Semantic Chunking)
การเลือกวิธีการแบ่ง chunk ที่เหมาะสมขึ้นอยู่กับ
- ประเภทของข้อมูล
- ข้อจำกัดของ Model
- Task ที่ต้องการทำ

Q : ถ้าข้อมูลไม่ได้เป้น Document Text ที่ยาวมากควรแบ่ง Chunk อย่างไรเพื่อให้ Search หาได้ใกล้เคียง?
A : แม้ข้อมูลจะไม่ยาวมาก การแบ่ง Chunk ก็ยังอาจมีประโยชน์ถ้าข้อมูลนั้นยังยาวเกินกว่าที่ Embedding Model จะรับได้ หรือถ้าต้องการให้แต่ละ Chunk มีความหมายที่เฉพาะเจาะจงอาจจะพิจารณาแบ่งตามย่อหน้า, ประโยค หรือโครงสร้างของข้อมูลนั้นๆ โดยยอาจจะไม่จำเป้นต้องมี Overlab มากเท่าข้อมูลยาวๆ

Q : ข้อมูลที่เป็น Structure เช่น Product Master จาก Database สามารถนำเข้า RAG ได้ไหม? อย่างไร?
A : ได้ ปกติทั่วไปจะมี 3 ขั้นตอน
	1. แปลงข้อมูล Structured เป็น Text โดยนำข้อมูลจากแต่ละแถว/Record ใน Database มาสร้างเป็นข้อความที่มีความหมายและมีบริบท (Context) เพียงพอเช่น "สินค้า A ราคา 100 บาทมีคุณสมบัติ X, Y, Z อยู่ในหมวดหมู่ C"
	2. สร้าง Vector Embedding : นำข้อความที่แปลงแล้วไปผ่าน Embedding Model
	3. จัดเก็บและใช้งาน : เก็บ Embedding ใน Vector DB แล้วใช้ RAG ค้นหาและให้ LLM สร้างคำตอบตามปกติ 

Q : RAG สำหรับภาษาไทยใช้งานได้ดีแค่ไหน? และมี Embedding Model/LLM ตัวไหนแนะนำสำหรบภาษาไทย?
A : RAG สำหรับภาษาไทยสามารถใช้งานได้ดีในระดับหนึ่ง โดยเฉพาะกับข้อมูลที่มีการจัดเรียงดีและมี Context ชัดเจนเพื่อความแม่นยำสูง ควรใช้ Embedding Model และ LLM ที่รองรับภาษาไทยโดยตรง
Embedding Models (รองรับไทย)
- wangchanberta
- multilingual-e5
- LaBSE
- paraphrase-multilingual-MiniLM-L12-v2
LLMs (รองรับไทย) 
- GPT-4, Claude3
- Gemini 1.5
- WangchanGLM
- ThaiLLaMA
- Mistral/Mixtral (ที่ Fine-tuned ภาษาไทย)

Q : เปรียบเทียบ Pinecone กับ Qdrant หรือ Vector DB ตัวอื่นที่ใช้แบบ Local ถ้าใช้งานแบบ Local ควรเลือกตัวไหน?
A : 
- ประเภทของ Vector database
	- Pinecone : เป็น Managed Service บน Cloud ใช้งานง่าย, Scale ได้ดี, เหมาะกับคนที่ไม่ต้องการจัดการ Infrastructure เองแต่มีค่าาใช้จ่ายตามการใช้งาน
	- Qdrant, Weaviate, Milvus : เป็น Open-source Vector DB ที่สามารถติดตั้งใช้งานได้เอง (self-host) หรือบางตัวก็มี Cloud service ให้บริการมีความยืดหยุ่นสูง, custom ได้เยอะอาจจะประหยัดกว่าในระยะยาวถ้ามีีทีมดูแล
	- FIASS, Chroma : เป็น Library/DB ที่เบาและเหมาะกับการทำงานแบบ Proof of Concept หรือระบบที่ไม่ใหญ่มากใช้งานง่าย
- การเลือก : ขึ้นอยู่กับขนาดของโปรเจคท์, งบประมาณ, ความเชี่ยวชาญของทีม, และความต้องการด้าน Performance/Scalbility 

Q : สำหรับ GCP ใช้อะไรเป็น Vector database?
A : มี 3 Options
1. ==Vertex AI Matching Engine== (หรือ Vector Search) : เหมาะกับการใช้งานร่วมกับ Vertex AI/LLMs อื่นๆ ของ Google, Scale ได้ดี, ใช้งานง่าย
2. Open-source Vector DBs บน GKE (Google Kubernetes Engine) เช่น Milvus, Weaviate, Qdrant สามารถติดตั้งและจัดการได้เองบน GKE
3. BigQuery Vector Extensions : เหมาะสำหรับงานที่ต้องการทำ Analytics หรือมี Workload อยู่บน BigQuery อยู่แล้ว

Q : Dense กับ Sparse (Indexes/Data) ต่างกันอย่างไร?
A : 
- Dense Vectors/Embeddings เป็น Vector ที่ส่วนใหญ่ของค่าใน Vector ไม่ใช่ศูนย์ (non-zero) มักจะได้มาจาก Neural Network Embedding Models และ==จับความหมายเชิงลึก (Semantic)== ได้ดี
- Sparse Vectors : เป็น Vector ที่ส่วนใหญ่ของค่าเป็นศูนย์ (zero) มักจะใช้แทนข้อมูลแบบ Keyword-based (เช่น TF-IDF, BM25 เน้นการจับคู่คำที่ตรงกัน)
- สำหรับ RAG เรามักจะใช้ Dense Embeddings สำหรับ Semantic Search แต่บางครั้งอาจใช้งานร่วมกับ Sparse Search (Hybrid Search) เพื่อเพิ่มประสิทธิภาพ

Q : LangChain คืออะไร?
A : LangChain เป้น Framework หรือ Library ที่ช่วนในการพัฒนาแอปพลิเคชันที่ขับเคลื่นอด้วย LLMs ให้ง่ายขึ้นโดยมีเครื่องมือและ Abstraction ต่าๆ
- สำหรับการทำ Chaining (เชื่อมต่อการทำงานของ LLM กับ Component อื่นๆ)
- การจัดการ Prompt
- การเชื่อมต่อกับ Memory
- การสร้าง Agent
- การเรียกใช้ Tools ต่างๆ เพื่อเป็น "Orchestrate" การทำงานของระบบ AI ที่ซับซ้อน

Q : Guardrails จำเป็นต้องพึ่งพาความสามารถของ LLM ในการวิเคราะห์ Context หรือ Software จัดการได้เอง ?
A : ทั้งคู่ทั้ง ความสามารถของ LLM ทั้งตัวหลักและตัวรองช่วยวิเคราะห์ Context เพื่อตัดสินใจว่าจะ Handle อย่างไร
- Software สามารถจัดการได้สำหรับปัญหาง่ายๆ เช่น การกรองคำหยาบ, การป้องกันการตอบนอกเรื่องที่กำหนดไว้ล่วงหน้า
- LLM เอาไว้ใช้จัดการกับปัญหาที่ซับซ้อน อาจจะต้องใช้ LLM ตัวหลักและ LLM ตัวรอง เพื่อช่วยวิเคราะห์ Context เพื่อให้ตัดสินใจได้ถูกว่าจะ Handle ยังไง

Q : Reranker Model จำเป็นต้องใช้ Prompt ไหม? หลักการทำงานคืออะไร ? ทำไมไม่ใช้ Reranker ตั้งแต่แรก?
A : 
- Prompt : Reranker Model บางตัวอาจจะใช้ Prompt เพื่อช่วย Focus ในการจัดอันดับให้ตรงกับ Query มากขึ้น แต่บางตัวก็อาจจะไม่ต้องใช้ ขึ้นอยู่กับการออกแบบ Model
- หลักการของ Reranker มักจะเป้นโมเดลที่ซับซ้อนกว่า (เช่น Cross-Encoder) ที่จะนำผลลัพธ์จำนวนหนึ่ง (เช่น Top K Chunks) ที่ได้จาก Retriever (ซึ่งมักใช้ Semantic Search ที่เร็วกว่า เช่น Bi-Encoder) มา "จัดอันดับใหม่" โดยพิจารณาความสัมพันธ์ ระหว่าง Query กับแต่ละ Chunk อย่างละเอียดอีกครั้ง เพื่อให้ได้ผลลัพธ์ที่เกี่ยวข้องมากที่สุดอยู่ด้านบนสุด
- แล้วทำไมไม่ใช้แต่แรก ? เพราะว่า Reranker Model ที่ละเอียดมักจะใช้เวลาประมวลผลนานกว่า Semantic Search แบบ Bi-Encoder มากการใช้ Retriever ค้นหาแบบเร็วเมื่องกรอง Candidate จำนวนมากออกไปก่อนแล้วค่อยใช้ Reranker กับ Candidate จำนวนน้อยๆ จะมีประสิทธิภาพโดยรวมดีกว่า

Q : "Instruct" Models ต่างกับ "Non-Instruct" Models อย่างไร?
A : 
- Non-Instruct Model คือ Base Model (เช่น GPT-3 davinci) เป็นโมเดลภาษาทั่วไปที่สามารถใช้ในการ "ต่อข้อความ" (Text Completion) ได้ดีแต่อาจจะไม่ได้ทำตามคำสั่งโดยตรงเสมอไป ต้องมีการออกแบบ Prompt (Prompt Engineering) ที่ดีเพื่อให้ได้ผลลัพฑ์ตามต้องการ
- Instruct Models (เช่น GPT3.5-Instruct, Gemini) เป็นโมเดลที่ถูก Fine-tuned มาโดยเฉพาะเพื่อหใ้ "ทำตามคำสั่ง" (Instructions) ของผู้ใช้ได้ดี เหมาะกับงานที่ต้องการคำตอบที่ตรงไปตรงมาเช่น การตอบคำถาม, สรุปความ, แปลภาษา



![[Pasted image 20250924183238.png]]