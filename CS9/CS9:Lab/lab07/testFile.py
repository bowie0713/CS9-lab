from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException
import pytest

def test_Custompizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp2 = CustomPizza("M")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
Price: $10.00\n"
    cp3 = CustomPizza("L")
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n"
    cp1.addTopping("cheese")
    cp1.addTopping("sausage")
    cp1.addTopping("egg")
    cp2.addTopping("ham")
    cp2.addTopping("blue cheese")
    cp3.addTopping("turkey")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ cheese\n\
\t+ sausage\n\
\t+ egg\n\
Price: $9.50\n"
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ ham\n\
\t+ blue cheese\n\
Price: $11.50\n"
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ turkey\n\
Price: $13.00\n"

def test_specialty():
    sp1 = SpecialtyPizza("L", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Carne-more\n\
Price: $16.00\n"
    sp2 = SpecialtyPizza("M", "HI!")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: HI!\n\
Price: $14.00\n"
    sp3 = SpecialtyPizza("S", "Delivery")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Delivery\n\
Price: $12.00\n"

def test_pizzaorder():
    cp2 = CustomPizza("M")
    cp2.addTopping("ham")
    cp2.addTopping("blue cheese")
    sp3 = SpecialtyPizza("S", "Delivery")
    order = PizzaOrder(81314) #12:30:00PM
    order.addPizza(cp2)
    order.addPizza(sp3)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 81314\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ ham\n\
\t+ blue cheese\n\
Price: $11.50\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Delivery\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $23.50\n\
******\n"
    sp1 = SpecialtyPizza("L", "Bowie")
    cp1 = CustomPizza("L")
    cp1.addTopping("mushroom")
    #sp3 = SpecialtyPizza("S", "Delivery")
    order2 = PizzaOrder(121111) #12:30:00PM
    order2.addPizza(sp1)
    order2.addPizza(cp1)
    order2.addPizza(sp3)
    assert order2.getOrderDescription() == \
"******\n\
Order Time: 121111\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Bowie\n\
Price: $16.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ mushroom\n\
Price: $13.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Delivery\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $41.00\n\
******\n"

def test_orderqueue():
    bh = OrderQueue()
    cp2 = CustomPizza("M")
    cp2.addTopping("ham")
    cp2.addTopping("blue cheese")
    sp3 = SpecialtyPizza("S", "Delivery")
    order = PizzaOrder(81314) 
    order.addPizza(cp2)
    order.addPizza(sp3)

    bh.addOrder(order)

    sp1 = SpecialtyPizza("L", "Bowie")
    cp1 = CustomPizza("L")
    cp1.addTopping("mushroom")
    #sp3 = SpecialtyPizza("S", "Delivery")
    order2 = PizzaOrder(121111) 
    order2.addPizza(sp1)
    order2.addPizza(cp1)
    order2.addPizza(sp3)

    bh.addOrder(order2)

    sp4 = SpecialtyPizza("M", "Hey")
    order3 = PizzaOrder(225501)
    order3.addPizza(sp4)

    bh.addOrder(order3)

    assert bh.processNextOrder() == \
"******\n\
Order Time: 81314\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ ham\n\
\t+ blue cheese\n\
Price: $11.50\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Delivery\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $23.50\n\
******\n"
    assert bh.processNextOrder() == \
"******\n\
Order Time: 121111\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Bowie\n\
Price: $16.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ mushroom\n\
Price: $13.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Delivery\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $41.00\n\
******\n"
    assert bh.processNextOrder() == \
"******\n\
Order Time: 225501\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Hey\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $14.00\n\
******\n"
    with pytest.raises(QueueEmptyException):
        bh.processNextOrder()








    



