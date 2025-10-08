class Villa(House):

    def __inti__(self, address, size, luxury_level)
        # Call parent class cosnstructor
        super().__init__(address, size)
        #Add a new isntance variable
        self.luxury_level = luxury_level
        
    def describe(self)
        #Extend parent's method
        base_description = super().describe()
        return f"{base_description}, Luxury Level: {self.luxury_level}"
    