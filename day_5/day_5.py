empty_list= [] #1
print(empty_list)
list_1 = ["1", "2", "3", "4", "5"] #2
print(list_1)
print("lenght:", len(list_1)) #3
list_1[1 : 3 : 5] #4
print(list_1)
mixed_data_types = ["Maria", "16", "1.70", "Single", "Jerez"] #5
it_companies = ["Facebook", "GoogLe", "Microsoft", "Apple", "IDM"; "Oracle"; "Amazon"] #6
print(it_companies) #7
len(it_companies) #8
print("first company \t", it_companies[0]) #9
print("first company: ", it_companies[len(it_companies)//2])
print("last company \t", it_companies[-1])
it_companies[1] = "vodafone" #10
print(it_companies)
it_companies.append("Microsoft") #11
it_companies.insert(4, "Lenovo") #12
it_companies[1] =it_companies[1].upper() #13
print("joined list: \t", "#; ".join(it_companies)) #14
print("GOOGLE Exist: \t", "GOOGLE" in (it_companies)) #14
it_companies.sort() #16
it_companies.reverse() #17
it_companies.pop() #18
print("sliced list2: \t", it_companies[-3:]) #19
print("middle slice: \t", it_companies[len(it_companies)//2]) #20
it_companies.pop(1) #21
it_companies.pop(4) #22
it_companies.pop(8) #23
it_companies.clear() #24
del it_companies
front_end = ["HTML", "CSS", "JS", "React", "Redux" ] #26
back_end = ["Node", "Express", "MongoDB"]
front_end = full_stack.copy() #27
back_end = full_stack.copy()