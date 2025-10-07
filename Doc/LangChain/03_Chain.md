![[Pasted image 20251006103400.png]]
- Chain เป็นส่วนประกอบที่สำคัญเกือบจะที่สุดแล้วสำหรับ Langchain
- เราสามารถที่จะเอามันไป Reusable ได้ในอนาคต
- มันประกอบไปด้วย
	- Models
	- Prompts
	- Output Parser
- Chain เนี้ยมันสามารถทำให้ Simple ก็ได้หรือทำให้มันซับซ้อนก็ได้
![[Pasted image 20251006103613.png]]
- Chain เนี้ยมันสามารถทำให้เรา Combine component ต่างๆเข้าด้วยกันได้
![[Pasted image 20251006103840.png]]
- LLM chain อันนี้เป็นอันที่เรียบง่ายที่สุด
- หน้าที่ของมันคือ เชื่อม Prompt แล้วโยนให้ LLM
![[Pasted image 20251006103930.png]]
- SequentialChain เป็นการ LLM หลายๆตัวมา chain ต่อกันเป็นสายโซ่
- Prompt -> LLM -> Context สักอย่าง -> LLM
![[Pasted image 20251006104108.png]]
- SimpleSequentialChain 
	- Input Output เป็นแบบ 1 ต่อ 1
- SequentialChain
	- เป็น Chain ที่ซับซ้อน
	- สามารถใช้ได้ในหลายหลายกรณี
![[Pasted image 20251006104449.png]]
- RouterChain เป็น Chain ที่ซับซ้อน
- อย่างเช่นมี Input 1 อย่างแต่ว่ามีมีชำนาญหลายคน 1 Input อาจจะต้องใช้ความรู้ความสามารถจากคนที่ถูกต้องเลยต้อง Rout ไปเรื่อยๆ 