#กระรับค่าข้อมูลทางแป้นพิมพ์ผ่าน Python ด้วยคำสั่ง "input"
name=input(" ป้อนชื่อ: ")
year_born=input(" ป้อนปีเกิด: ")
old = (2023-int(year_born))
print("----------------------------------")
print(f"ยินดีต้อนรับ {name} เกิดปี {year_born} อายุ {old}" )
#แปลงข้อมูลข้อความเป็นตัวเลข int() และ float() 
#แปลงข้อมูลตัวเลขเป็นข้อความ str()
print("ยินดีต้อนรับ",name,"เกิดปี",year_born,"อายุ",old) 
print("ยินดีต้อนรับ "+ name +" เกิดปี "+ year_born +" อายุ "+ str(old)) 
print("ยินดีต้อนรับ {} เกิดปี {} อายุ {}" .format(name,year_born,old)) 
print("ยินดีต้อนรับ %s เกิดปี %s อายุ %d" %(name,year_born,old)) 