from nss_human import nss_human
class Instructor(nss_human):
  def __init__(self, first_name, last_name, slack_handle, specialty):
    super().__init__(first_name, last_name, slack_handle)
    self.specialty = specialty

  def assign_exercise(self, student, exercise):
    student.exercises.append(exercise)
