class carro():
    def __init__(self, motor) -> None:
        self.motor = motor
        self.drs = True

ferrari1 = carro('v8')
ferrari2 = carro('2022')

assert ferrari1.motor == 'v8'
assert ferrari2.motor == '2022'
assert ferrari1.drs 