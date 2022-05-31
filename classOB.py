class Student:
    # [assignment] Skeleton class. Add your code here
    #Constructor
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    # Method 
    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, new_track=["PY","CONDA"]):
        self.track = new_track

    def get_score(self, get_score):
        self.score = get_score
        if changed(self.age,int):
            print(self.name, self.age, self.track, self.score)
        else:
            print("your age must be an integer, keep trying")

        

Bob = Student("Bob", 26, ["PY","CONDA"], 20.90)
Peter = Student("Peter", 34, ["UI","UX"], 30.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(30.00))

