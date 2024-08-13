from birds_v1 import Duck, Crow, Mallard

birds = [
    Duck(),
    Crow(),
    Mallard(),
]

for bird in birds:
    bird.fly()
    bird.swim()
    bird.eat()
    # The class of bird can do many things
    # Add a new behavior of the bird below
    # bird.flap_wing()
    # run the script - what do you observe ?
