import  st_group, st_human



st1 = st_human.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = st_human.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = st_group.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student('Jobs') 
gr.find_student('Jobs2')  # None

gr.delete_student('Taylor')
print(gr) # Only one student