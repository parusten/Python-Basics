#zip chai jaba use garne jaba two or more lists haru eutai tuple ma combine garera rakhna paryo vane


# zip(iterable1,iterable2,iterable3.....)    output: (it1.1,it2.1,it3.1), (it1.2,it2.2,it3.2)
student = ['sandip', 'binaya', 'prajwol']
nepali = [100, 92, 90]
updated_coll = tuple(zip(student, nepali))
print(tuple(updated_coll))
# dict_marks = {name: marks for name, marks in updated_coll}
# print(dict_marks)