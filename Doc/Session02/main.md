![[Pasted image 20251014124610.png]]
![[Pasted image 20251014124632.png]]
 ![[Pasted image 20251014124854.png]]
 - Generative AI : 
	 - จะโฟกัสเกี่ยวกับการสร้าง ไม่ว่าจะเป็น text, image, music  (การ Gen รูปหรืออะไรพวกนี้)
	 - จะเป็นการวัดผลแบบครั้งเดียว อย่างความถูกต้องของผลงาน (แม่นไม่แม่น)
 - Agentic AI : 
	 - จะเป็นสิ่งที่เกี่ยวการกระทำ Acting ต่างๆ โดยมันจะออกแบบทั้งระบบ
	 - จะเป็นการวัดทั้ง Flow ทั้งระบบ (เป็นการวัดว่า Flow ที่เราให้มัน success หรือเปล่า)
![[Pasted image 20251014130505.png]]
![[Pasted image 20251014130657.png]]
- Agent มันดีแต่ว่าไม่ใช่ว่ามันจะเข้าได้กับทุกๆ งานบางอย่างมันก็ Overforce engineering
![[Pasted image 20251014131735.png]]
- ==Agent คือ Flow==
- Multi agent มันจะมี agent หลายตัว
- Agent แต่ละตัวก็มีความเก่งหรือว่ามี Task งานเฉพาะที่แตกต่างกัน
![[Pasted image 20251014134738.png]]
![[Pasted image 20251015104523.png]]
- Single agent
	- ถ้าหากมี load เพิ่มมันเหมือนทำงานอยู่คนเดียว มันอาจจะมีคอขวดเพิ่มขึ้นได้
- Multi-Agent system
	- มันจะทำงานได้ดีกว่า มันจะทำงานแบบ Parallel 
	- สามารถทำ Load balance ได้ดีกว่า
	- Multiple interacting agents มันจะสามารถคุยกันระหว่าง Agent แต่ละตัวได้
![[Pasted image 20251015105051.png]]
- User 
	- รับเรื่องจากลูกค้า
- Orchestrator
	- เป็นเหมือนกับหัวหน้าที่คอยรับคำสั่งจาก User แล้วแจกจ่ายงานไปให้ Agent หรือ ตัวแทน ต่างๆ
- Planner agent
	- เป็นคนที่รับเรื่องและวางแผนว่า ถ้าเป้าหมายคือแบบนี้แล้วควรจะวางแผนยังไง
- Executor agent
	- คนลงมือทำ
- Memory agent
	- สมุดบันทึกกหรือฐานข้อมูลของทีม
	- เก็บข้อมูลสำคัญต่างๆ ที่เกิดขึ้นระหว่างการทำงาน
- External Tools/APIs
	- Tools จาก Third party
![[Pasted image 20251015110104.png]]
- ถ้าหากงานมัน complex สูง -> Multi-Agent System
- ถ้าหากงานมันไม่ complex  -> Single Agent ถ้าหากว่ามีอาการคอขวดหรือล้มอาจจะ Scale มัน
![[Pasted image 20251015110601.png]]
![[Pasted image 20251015111026.png]]
- Tools calling คือความสามารถอย่างหนึ่งของ LLM
- LLM จะถูกเทรนแล้วมีมัน
- LLM เนี้ยมันจะใช้ tool calling เมื่อมันไม่รู้ข้อมูลจริงๆ ที่ถูกต้องมันจะถูกเรียกให้ไปเชื่อมต่อ API เพื่อหา fact
- ส่วนมากแล้ว Tools ต่างๆ ที่ไปเรียกมันกจะ Return response กลับมาในรูปของ JSON
- ประโยชน์ของ Tools calling
	- มันสามารถที่จะเปลี่ยนข้อมูลบางอย่างได้ เช่น ลูกค้าซื้อของแล้ว อยากเปลี่ยนที่อยู่
![[Pasted image 20251015112217.png]]
![[Pasted image 20251015112609.png]]![[Pasted image 20251015121255.png]]
![[Pasted image 20251015122145.png]]
![[Pasted image 20251015122323.png]]
![[Pasted image 20251015155803.png]]
- Memory
	- Long-term knowledge store : ความรู้ถาวร
	- Short-term scratchpad : กระดาษจดชั่วคราว 
	- Episodic logs of past tasks : บันทึกสิ่งที่เคยทำก่อนหน้า อย่างโหลดไฟล์ เผื่อจะได้ไม่ทำซ้ำ
	- Refresh & retrieval : ทบทวนให้มันจำแม่น
- Context
	- Current user goal & instructions
	- Recent conversation turns : 
	- tools results & environment state
	- System constraints & policies
![[Pasted image 20251015160553.png]]
58:18
![[Pasted image 20251015161657.png]]
- ReAct != React.js!
- ReAct หมายถึง การกระทำ
![[Pasted image 20251015162514.png]]
- Agent = Flow การทำงาน
	- Though : คิดว่าถ้าอยากจะ finish งานที่ได้รับจะต้องทำอะไรบ้าง step เป็นยังไง
	- Action : ทำตามแผน
	- Observation : ดูผลลัพธ์ที่ได้แล้วเอามาทำงานต่อ
- ทุกวันนี้พอมันสามารถที่จะเชื่อมกับ Tools ภายนอกสามารถเข้าถึง API ทำให้มันลด Hallucination ได้เยอะ
- ReAct เป็นเหมือนสมองที่คอยคิดและตัดสินใจ, MCP เป็นเหมือนสะพานเชื่อมที่ปล่อยให้สามารถเข้าถึง Tools ต่างๆ ได้
- เมื่อ ReAct + MCP = Agent ที่ฉลาดคิดและสามารถเชื่อมต่อกับโลกภายนอกได้ดี
![[Pasted image 20251015163446.png]]
![[Pasted image 20251015163514.png]]
- ADK เป็นเนื้อหาค่อนข้างใหม่
![[Pasted image 20251015163831.png]]
![[Pasted image 20251015164134.png]]
01:14:11
01:22:28
Lab 1