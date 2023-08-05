class Cat:
    def __init__(self, name, gender, age, breed, registration_document, status):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed
        self.registration_document = registration_document
        self.status = status



    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def getBreed(self):
        return self.breed

    def getRegistration_document(self):
        return self.registration_document

    def getStatus(self):
        return self.status