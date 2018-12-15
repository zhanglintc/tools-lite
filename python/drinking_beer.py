#!/usr/bin/python

class Drinker:
    def __init__(self):
        self.cash = 10
        self.beer_drinked = 0

        self.caps = 0
        self.bottles = 0

    def buy_beer(self):
        """ each beer $2 """

        beer = int(self.cash / 2)

        self.cash -= beer * 2
        self.caps += beer
        self.bottles += beer
        self.beer_drinked += beer

        print "after buy_beer()"
        self.show_off()

    def cap_to_beer(self):
        """ 4 caps 1 beer """

        beer = int(self.caps / 4)

        self.caps -= beer * 4
        self.caps += beer
        self.bottles += beer
        self.beer_drinked += beer

        print "after cap_to_beer()"
        self.show_off()

    def bottle_to_beer(self):
        """ 2 bottles 1 beer """

        beer = int(self.bottles / 2)

        self.bottles -= beer * 2
        self.caps += beer
        self.bottles += beer
        self.beer_drinked += beer

        print "after bottle_to_beer()"
        self.show_off()

    def going_on(self):
        return self.cash >= 2 or self.caps >= 4 or self.bottles >= 2

    def show_off(self):
        print "cash: %s" % self.cash
        print "caps: %s" % self.caps
        print "bottles: %s" % self.bottles
        print "drinked: %s" % self.beer_drinked
        print

idx = 0
Jim = Drinker()
while Jim.going_on():
    idx += 1
    print "----- round %s -----" % idx

    Jim.buy_beer()
    Jim.cap_to_beer()
    Jim.bottle_to_beer()

print "----- final -----"
Jim.show_off()




