class Cat:
  def __init__(self, name, age, disease, characteristics,spouse):
    self.name = name
    self.age = age
    self.disease = disease
    self.characteristics = characteristics
    self.spouse=spouse
  def show_details(self):
      print("Name:", self.name)
      print("Age:", self.age)
      print("Disease:", self.disease)
      print("Characteristics:", self.characteristics)
      print("Spouse:", self.spouse)


cat1 = Cat("cat1", 2, "none", "friendly" ,"none")
cat2 = Cat("cat2", 5, "none", "shy" ,"none")
cat3 = Cat("cat3", 3, "none", "playful" ,"none")
cat4 = Cat("cat4", 4, "none", "lazy" ,"none")
cat5 = Cat("cat5", 6, "none", "energetic" ,"none")
cat6 = Cat("cat6", 1, "none", "curious" ,"none")
cat7 = Cat("cat7", 8, "none", "affectionate" ,"none")
cat8 = Cat("cat8", 7, "none", "calm" ,"none")
cat9 = Cat("cat9", 3, "none", "friendly" ,"none")
cat10 = Cat("cat10", 5, "none", "timid" ,"none")