class Student:
    name = ""

    def __init__(self , name, **kwargs):
        self.name = name

        for key, values in kwargs.items():
            setattr(self, key, values)
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()

myself = Student("Jayd")

print(myself.feedback(60))