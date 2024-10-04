grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

grades_0 = []
grades_1 = []
grades_2 = []
grades_3 = []
grades_4 = []

grades_0 = grades [0]
grades_1 = grades [1]
grades_2 = grades [2]
grades_3 = grades [3]
grades_4 = grades [4]

r_all = [sum (grades_0) / len (grades_0), sum (grades_1) / len (grades_1), (sum (grades_2) / len (grades_2)), (sum (grades_3) / len (grades_3)), (sum (grades_4) / len (grades_4))]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted (students)

fin_list = {}
fin_list= dict(zip(students, r_all))
print (fin_list)