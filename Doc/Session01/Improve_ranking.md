- Index Routing (Query/Skill Routing)
	- ส่งคำถามไปยังดัชนีที่เหมาะสม (เช่น Tech, Docs, Policy, FAQ)
	- วิธีการส่งก็คือการจัดการด้วย Rule หรือ LLM-router
	- ดีมากเมื่อมีหลายคอร์ปัส/หลายภาษา/หลายสิทธ์
- Reranking (Cross Encoder)
	- หลังจากที่เราได้ Top-N มาแล้ว เราจะใช้ Model เรียงค่า Top-N ใหม่อีกครั้ง โดยอาจจะใช้ Model อย่าง MiniLM-cd, bge-reranker
- MMR (Maximal Marginal Relevance)
	- เลือกผลลัพธ์ให้เกี่ยวข้อง และไม่ซ้ำซ้อน
	- ลดความซ้ำของ Chunk คล้ายๆกันครอบคลุมมุมมองมากขึ้น
- AutoCut/Dynamic Top-K
	- กำหนด K แบบไดนามิกจากคะแนนความคล้ายสูตรที่ใช้บ่อย เรียงคะแนน cosine -> เลือก K จนกว่า sim[i] - sim[i+1] เกิน gap_threshold หรือหยุดเมื่อ sim[i] < abs_threshold
- Recursive Retrieval
	1. Hierarchical/Parent-Child : เป้นการดึง หัวข้อย่อย (chile) ก่อนแล้วตามมาด้วย ส่วนแม่ (parent) -> คอนเท็กซ์ครบ
	2. Question Decomposition : แตกคำถามใหญ่เป็น sub-queries -> รวมผล