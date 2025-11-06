# classes all go in here
#!/usr/bin/env python3
import random


class User:
    # class variable to store all user full names
    all_names = []

    # initializer / instance attributes
    def __init__(self, fist_name, last_name, email):
        self.first_name = fist_name
        self.last_name = last_name
        self.email = email
        User.add_name(fist_name, last_name)

    # instance method
    def send_email(self, receiver, message):
        print(f"{self.email} to {receiver}: {message}")

    # class method to add and check names
    @classmethod
    def add_name(cls, first, last):
        fullname = first + " " + last
        cls.all_names.append(fullname)

    @classmethod
    def user_exists(cls, fullname):
        return fullname in cls.all_names


class Teacher(User):  # inherits from User
    # initializer / instance attributes
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.knowledge = [
            "strr is a data type in Python",
            "programming is hard, but it's worth it",
            "JavasScript async wec request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytesy -x flag to fail fast",
        ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]


class Student(User):
    def __init__(self, first_name, last_name, email, gpa):
        super().__init__(first_name, last_name, email)
        self.gpa = gpa
        self._knowledge = []

    def learn(self, knowledge_string):
        self._knowledge.append(knowledge_string)

    @property
    def knowledge(self):
        return self._knowledge if self._knowledge else "I don't know anything yet!"

    @knowledge.setter
    def knowledge(self, value):
        self._knowledge = value


sandy = Teacher("Sandy", "Williams", "SandyWilliams@uni.edu")
bob = Student("Bob", "Dylan", "bob.dylan11@uni.edu", 3.4)
millie = Student("Millie", "Brown", "millie.brown4@uni.edu", 3.8)

bob.learn(sandy.teach())
bob.learn(sandy.teach())
bob.learn(sandy.teach())
bob.learn(sandy.teach())

print(f"Millie knows : {millie.knowledge}")
print(f"Bob knows: {bob.knowledge}")

sandy.send_email("bob.dylan11@uni.edu", "class is canceld for monday")
millie.send_email("millie.brown@uni.edu", "class is canceld for monday")
millie.send_email("sandy.williams@uni.edu", "thank you for the update")


print(User.user_exists("Bob Dylan"))
print(User.user_exists("Alice Wonderland"))
