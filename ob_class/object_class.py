class Length(float):
    def to_cm(self):
        return super().__str__() + 'cm'

pencil_length = Length(16)
print(pencil_length.to_cm())
