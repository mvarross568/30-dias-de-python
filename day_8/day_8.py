dog = {} #1
dog ["name"] = "lusytolo" #2
dog ["breed"] = "retriever"
dog ["legs"] = "4"
dog ["age"] = "5"
student_dictionary = {"first_name": "maria", "last_name": "varela",  "gender": "Female", "age":"16", "marital status":"single", "skills": "creativity", "country": "spain", "city": "jerez","address":"s.josefina"} #3
print(len(dog)) #4
value_of_skills = student_dictionary ["skills"].values() #5
type(student_dictionary["skills"]) 
student_dictionary["skills"].append("leadership","responsibility") #6
keys = dog.keys #7
print(keys)
values = dog.values #8
print(dog.items()) #9
dog.pop("first_name") #10
del dog #11


