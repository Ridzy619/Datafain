def parse(file):
  with open(file, 'r') as f:
      # Read first line containing headers and split it at ',' into a list
      header = f.readline().split(",") 
      subjects = header[4::2] # Since Each subject will have test and exam (e.g. English Test, English Exam), pick just one.
      subjects = [subject.strip().replace(" Test", "") for subject in subjects] # use list comprehension to remove 'test' part of the subject names
      subjects = [subject.strip().replace(" Exam", "") for subject in subjects] # use list comprehension to remove 'test' part of the subject names


      students = []
      test_scores = []
      exam_scores = []
      ages = []
      class_ = []
      for line in f:
          line = line.strip("\n")
          line = line.split(",")
          stud_fullname = line[0] + line[1] # Get student's full name
          students.append(stud_fullname) # Append to the list of students' names

          stud_age = line[2] # Get student's age
          ages.append(stud_age.strip()) # Append to students' ages list

          tests = line[4::2] #  Get all test scores for student
          test_scores.append(tests) # Append to the list of test scores for all students

          exams = line[5::2] #  Get all test scores for student
          exam_scores.append(exams) # Append to the list of test scores for all students

          class_.append(line[3].strip())

  return students, subjects, test_scores, exam_scores, ages, class_

## GENERATE DATA OF STUDENTS

number_of_students = 10
def generate_data(n_students = number_of_students, subjects = None):
  import requests
  import numpy as np
  
  # Read the file and create names and surnames variables
  
  out = requests.get("https://raw.githubusercontent.com/Ridzy619/Datafain/master/names.txt").content.decode().split("\n\n")
  names, surnames = out
  names = names.split('\n')[:50]
  surnames = surnames.split('\n')
  names.extend(surnames[:50])

  
  n = n_students
  if not subjects:
    subjects = ["English", "Mathematics", "Basic Science", "Basic Technology", "Creative Art", "Literature", "Civic Education"]
  m = len(subjects)
  with open("students_records.txt", "w") as file:
    header = ['Name,', 'Surname,', 'Age,', 'Class,']
    class_ = np.random.randint(1, 9)
    for sub in subjects:
      header.extend([sub+ " Test," , sub + " Exam,"])
    header[-1]=header[-1].replace(",", "")
    header.append("\n")
    file.writelines(header)
    for i in range(n):
      
      file.write(f"{np.random.choice(names).strip()}, {np.random.choice(surnames).strip()}, {np.random.randint(10, 15)}, Basic {class_},")
      
      for i in range(m):
        file.write(f"{np.random.randint(10, 30)},")
        file.write(f"{np.random.randint(20, 70)}")
        if i < m-1:
          file.write(",")
      file.write("\n")
  print(f"File generation completed! It has {n_students} students records and {m} subjects.\nThe file has has been saved as 'students_records.txt'")

def check_parser(parse_file, file_name = 'students_records.txt', parse = checker.parse):
  result = parse_file(file_name)
  actual = parse(file_name)
  var_names = ['students,', 'subjects,', 'test_scores,', 'exam_scores,', 'ages,', 'class_']
  assert len(result) == len(actual), f"Number of outputs expected is {len(actual)}, number of outputs gotten is {len(result)}"

  for i, j, name in zip(result, actual, var_names):
    if type(j) == list:
      assert not set(i).isdisjoint(b), f"You need to review {name}. There is no matching item to the expected items"
      assert set(j).issubset(set(i)) or set(i).issubset(set(j)), f"Items in {name} don't match the expted items. Difference is: {set(i).interset(set(j))}"
      assert len(i) <= len(j), f"There is a partial match. {set(i).difference(set(j))} are not supposed to be in {name}"
      assert len(i) >= len(j), f"There is a partial match. {set(j).difference(set(i))} are not found in {name}"
      assert i == j, "You are almost there. Just a little more adjustment and you will be there"
      
      
      # for k, (m, n) in enumerate(zip(i, j)):
      #   if type(j) == list:
      #     assert not set(i).isdisjoint(b), f"You need to review {name}. The sub"
      #     assert set(j).issubset(set(i)) or set(i).issubset(set(j)), f"Items in {name} don't match the expted items. Difference is: {set(i).interset(set(j))}"
      #     assert len(i) <= len(j), f"There is a partial match. {set(i).difference(set(j))} are not supposed to be in {name}"
      #     assert len(i) >= len(j), f"There is a partial match. {set(j).difference(set(i))} are not found in {name}"
      #     assert i == j: "You are almost there. Just a little more adjustment and you will be there"

      #     assert j in i or i in j, f"String {j} expected, {i} gotten."
      #     assert len(i) == len(j), f"There is a partial match. {j} expected, {i} gotten."
      #   if j.isdigit():
      #     assert j == i, f"Number {j} expected, {i} gotten"
  print("CONGRTULATIONS! You have passed all the checks. You may proceed to run the other cells to complete the program")

if __name__ == "__main__":
    generate_data(number_of_students)
