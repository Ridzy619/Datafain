import time
start_time = time.time()
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

          stud_age = int(line[2].strip()) # Get student's age
          ages.append(stud_age) # Append to students' ages list

          tests = line[4::2] #  Get all test scores for student
          tests = list(map(int, tests))
          test_scores.append(tests) # Append to the list of test scores for all students

          exams = line[5::2] #  Get all test scores for student
          exams = list(map(int, exams))
          exam_scores.append(exams) # Append to the list of test scores for all students

          class_.append(line[3].strip())

  return students, subjects, test_scores, exam_scores, ages, class_

## GENERATE DATA OF STUDENTS

# number_of_students = 10
def generate_data(n_students = 10, subjects = None):
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

def check_parser(parse_file, file_name = 'students_records.txt', parse = parse):
  result = parse_file(file_name)
  actual = parse(file_name)
  var_names = ['students,', 'subjects,', 'test_scores,', 'exam_scores,', 'ages,', 'class_']
  assert len(result) == len(actual), f"Number of outputs expected is {len(actual)}, number of outputs gotten is {len(result)}"

  for i, j, name in zip(result, actual, var_names):
    if type(j) == list:
      assert not set(i).isdisjoint(j), f"You need to review {name}. There is no matching item to the expected items"
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


def grader(score):
  if score >= 70:
    return "A"
  if score >= 60:
    return "B"
  if score >= 50:
    return "C"
  if score >= 40:
    return "D"
  if score < 40:
    return "F"



def total(test_scores, exam_scores):
  '''
  The output will be a list of lists of subject scores of each student
  e.g., [[64, 70], [84, 79]] for the example above. The list is of each
  student and the sublist is of each subject
  '''
  # Create a list of total scores of each student
  stud_total_scores = []
  for stud_tests, stud_exams in zip(test_scores, exam_scores):

    # Create a list of total scores for each subject
    subject_totals = []
    for sub_test, sub_exam in zip(stud_tests, stud_exams):

      # Append the sum of test and exam scores to subject totals
      subject_totals.append(sub_test + sub_exam)

    # Append the subject totals for each student to the stud_total_scores variable.
    stud_total_scores.append(subject_totals)

  return stud_total_scores



def stud_scores(subjects, total_scores):

  # Create an empty list of stud_scores
  stud_scores = []

  # Loop through the list of scores of each student and zip it with the subjects list
  # e.g: zip ['Mathematics', 'English'] and [64, 80]; zip ['Mathematics', 'English'] and [84, 79]
  for sub_scores in total_scores:

    # Zip each subject score with subjects list to match them up
    sub_score = list(zip(subjects, sub_scores))
    
    # Append each zipped object to the list created above
    stud_scores.append(sub_score)
  

  return stud_scores

import sys
def pprint(names, stud_scores, file, ages): # file argument allows us to specify the file we want out output written to
  file = open(file, 'w')
  
  # Create a variable for total calss average that gets update with the average score of each student at the loop below executes
  class_average_sum = 0

  # Loop through names and student scores in order to get the scores of all the subjects for each student
  for name, sub_scores in zip(names, stud_scores):
    
    # Create a variable that averages the student's performance
    stud_scores_sum = 0

    # Print the student's name
    print(name, file=file)

    # Print the headings and format it with appropriate spacing
    print(f'{"Subject":>20}:  |{"Score":<6}  |{"Grade"}', file=file)
    print("_" * 40, file = file) # Just a dash line

    # Loop through each (subject, score) tuple pair in the list sub_scores and print each subject and corresponding score.
    for subject, score in sub_scores:

      # Print and format the subjects, score and grade of each subject
      print(f'{subject:>20}:  |{score:<6.2f}  |{grader(score)}', file=file)

      # Adding each subject's score to the stud_average variable
      stud_scores_sum += score
    # Calculate the mean score
    average = stud_scores_sum/ len(sub_scores)
    print(f'\n{"Average":>20}:  |{average:<6.2f}  |{grader(average)}', file=file)
    print("\n", "+" * 40, end = '\n'*2, file=file)

    # Add average of each student to the class_average_sum
    class_average_sum += average
  
  # Calculate the class mean
  class_average = class_average_sum/len(names)
  av_age = sum(ages)/len(ages)
  print('Class Performance Summary'.center(40, '>'), file=file)
  print("\n", "+" * 40, end = '\n'*2, file=file)
  print(f'{"Number of Students":>20}\n{"in Class":>20}   |{len(ages): <6}', file=file)
  print(f'{"Average Class":>20}\n{"Age:":>20}   |{av_age: <6.2f}', file=file)
  print(f'{"Average Class":>20}\n{"Performance:":>20}   |{class_average: <6.2f}   |{grader(class_average)}', file=file)
  file.close()




def process_result(file_path = "students_records.txt", file = 'Project_output.txt'):
  names, subjects, test_scores, exam_scores, ages, class_ = parse(file_path)
  # Get total scores of tests and exams
  total_scores = total(test_scores, exam_scores)

  # Get a mapping of subjects to total scores
  student_scores = stud_scores(subjects, total_scores)

  # Print out a formatted ouput of report
  pprint(names, student_scores, file, ages)
  print(f"Program done running. Output has been saved as {file}")

print("Import completed! You are ready to execute your project")


if __name__ == "__main__":
    import sys
    try:
        arg = sys.argv[1]
        if arg.isdigit():
            generate_data(int(arg))
            process_result()
        else:
            process_result(arg)
    except IndexError:
        generate_data()
        process_result()
    print(f"Total runtime: {(time.time() - start_time):.2f} seconds")
