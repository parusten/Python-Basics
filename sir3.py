student = ['sandip', 'binaya', 'prajwol']
nepali = [100, 92, 90]
# dic_student = {}     # any other way??
# # for each in student:
# # #      updating the dict with new items from the list givem
# #     dic_student[each] = len(each)
# dic_student = {each: len(each) for each in student}       #This is another way to use loop like as above
# print(dic_student)





dic_marks = {}     # any other way??
# for i in range(len(student)):
#     # updating the dict with new items from the list givem
#     dic_marks[student[i]] = nepali[i]
  
dic_marks = {student[i]:nepali[i] for i in range(len(student))}
print(dic_marks)         