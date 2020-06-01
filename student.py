from cohort import Cohort
class Student:
  def __init__(self, first_name, last_name, slack):
    self.first_name = first_name
    self.last_name = last_name
    self.slack_handle = slack
    self.exercises = []
    self.cohort = Cohort