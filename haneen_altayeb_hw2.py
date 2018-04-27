class Waiter(object):
    def __init__(self, order):
        self.food = ["salad", "main meal"]
        self.order = order
    def serving_food(self):
        order = raw_input("choose a food\n")
        if order in self.food:
            print "okay  \n\n"
            print "In the kitchen\n"
            print "The waiter : cook Adel, the next order is " + order + ", how long will it take?"
            cook.prepare_food()
        else:
            print "The Waiter :The food you ordered is not available"

class Customer(Waiter):
    def __init__(self, name):
        Waiter.__init__(self, order=Waiter)
        self.name = name

    def order_food(self):
        print"In the resturant\n"
        print"The Waiter : Welcome " + self.name + ", here is the menu"
        print self.food
        w1.serving_food()

class Cook(Customer):
    def __init__(self, name):
        Customer.__init__(self, name=Customer)
        self.name = name

    def prepare_food(self):
        print "The cook : The order will be ready in 15 minutes\n\n"




c1=Customer("Haneen")
c2=Customer("Sara")
c3=Customer("Raheel")
w1=Waiter("Waiter1")
cook=Cook("Adel")

c1.order_food()
c2.order_food()
c3.order_food()















