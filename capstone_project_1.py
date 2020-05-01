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
def pprint(names, stud_scores, file): # file argument allows us to specify the file we want out output written to
  
  # Create a variable for total calss average that gets update with the average score of each student at the loop below executes
  class_average_sum = 0

  # Loop through names and student scores in order to get the scores of all the subjects for each student
  for name, sub_scores in zip(names, stud_scores):
    
    # Create a variable that averages the student's performance
    stud_scores_sum = 0

    # Print the student's name
    print(name)

    # Print the headings and format it with appropriate spacing
    print(f'{"Subject":>20}:  |{"Score":<6}  |{"Grade"}')
    print("_" * 40) # Just a dash line

    # Loop through each (subject, score) tuple pair in the list sub_scores and print each subject and corresponding score.
    for subject, score in sub_scores:

      # Print and format the subjects, score and grade of each subject
      print(f'{subject:>20}:  |{score:<6}  |{grader(score)}')

      # Adding each subject's score to the stud_average variable
      stud_scores_sum += score
    # Calculate the mean score
    average = stud_scores_sum/ len(sub_scores)
    print()
    print(f'{"Average":>20}:  |{average:<6}  |{grader(average)}')
    print("\n", "+" * 40, end = '\n'*2)

    # Add average of each student to the class_average_sum
    class_average_sum += average
  
  # Calculate the class mean
  class_average = class_average_sum/len(names)
  print(f'{"Average Class":>20}\n{"Performance:":>20}  |{class_average: <6}   |{grader(class_average)}')




def process_result(names, subjects, tests, exams, file = sys.stdout):
  # Get total scores of tests and exams
  total_scores = total(test_scores, exam_scores)

  # Get a mapping of subjects to total scores
  student_scores = stud_scores(subjects, total_scores)

  # Print out a formatted ouput of report
  pprint(names, student_scores, file)

print("Import completed! You are ready to execute your project")
