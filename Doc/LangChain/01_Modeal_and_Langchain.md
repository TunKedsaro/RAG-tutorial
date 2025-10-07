![[Pasted image 20251003100252.png]]
![[Pasted image 20251003100208.png]]
- ปกติแล้วเราจะเขียนให้ LLM เนี้ยมันทำงานได้ต่อเนื่องกัน เราเรียกว่า ==ChainLLM, LLM cascading==
- แล้วให้ LLM แต่ละตัวแต่ละ Prompt ทำงานแต่ละอย่าง โดยเอา Output ตัวนึ่งไป Feed อีกตัวหนึ่ง
- อย่างเช่น
	- LLM ตัว 1 : ระบุประเภท
	- LLM ตัว 2 : ระบุ Spec ของสิ่งที่จะทำ
	- LLM ตัว 3 : Generate code
- ซึ่งนี้คือเหตุผลของการกำเนิด ==Langchain==
![[Pasted image 20251003102717.png]]
- 1 การแบ่งออกเป็น component
- 2 เรามีอะไรที่สามารถหยิบออกมาแล้วสามารถใช้งานได้เลย 
![[Pasted image 20251003104328.png]]
- Model (LLM) ตรงกลาง : chat model, completion model
- Prompt (ซ้าย) : 
	- template
	- prompt builder
	- เอาทั้งคู่มาประกอบกัน
- Output parser:
	- เลือก Outpuut format
		- JSON
		- XLM
- 