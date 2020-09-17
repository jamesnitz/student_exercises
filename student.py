from nss_human import nss_human

class Student(nss_human):
  def __init__(self, first_name, last_name, slack):
    super().__init__(first_name, last_name, slack)
    self.exercises = []