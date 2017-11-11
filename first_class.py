class Human:
    lifespan = 80
    birth = int(input("Which year were you born?"))
    current_year = 2017
    def life(self):
        age = self.current_year - self.birth
        if self.birth < 2000 and self.birth > 1990:
            print("Woohoo.. you're a 90's kid!")
        elif self.birth > 2000:
            print("Holy fuck you are young!!")

        print("You are currently " + str(age) + " years old")

        death = self.lifespan - age
        death_year = self.birth + self.lifespan
        print("You are likely to die " + str(death) + " years from now, " + " in " + str(death_year))



samwel = Human()
samwel.life()
