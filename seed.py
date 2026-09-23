from app import create_app, db
from app.models import Restaurant, MenuItem

app = create_app()

with app.app_context():

    # Remove old restaurant data
    MenuItem.query.delete()
    Restaurant.query.delete()

    # Restaurant 1
    restaurant1 = Restaurant(
        name="Spice Garden",
        description="Delicious Indian food",
        location="Kolar",
        image="spice-garden.jpg",
        rating=4.5
    )

    # Restaurant 2
    restaurant2 = Restaurant(
        name="Pizza Paradise",
        description="Fresh and cheesy pizzas",
        location="Kolar",
        image="pizza-paradise.jpg",
        rating=4.7
    )

    # Restaurant 3
    restaurant3 = Restaurant(
        name="Burger House",
        description="Juicy burgers and tasty fries",
        location="Kolar",
        image="burger-house.jpg",
        rating=4.4
    )

    db.session.add_all([
        restaurant1,
        restaurant2,
        restaurant3
    ])

    db.session.commit()

    # Menu items for Spice Garden
    item1 = MenuItem(
        name="Masala Dosa",
        description="Crispy dosa with potato masala",
        price=80,
        restaurant_id=restaurant1.id
    )

    item2 = MenuItem(
        name="Paneer Butter Masala",
        description="Creamy paneer curry",
        price=180,
        restaurant_id=restaurant1.id
    )

    # Menu items for Pizza Paradise
    item3 = MenuItem(
        name="Margherita Pizza",
        description="Classic cheese pizza",
        price=199,
        restaurant_id=restaurant2.id
    )

    item4 = MenuItem(
        name="Farmhouse Pizza",
        description="Pizza loaded with fresh vegetables",
        price=249,
        restaurant_id=restaurant2.id
    )

    # Menu items for Burger House
    item5 = MenuItem(
        name="Cheese Burger",
        description="Burger with cheese and fresh vegetables",
        price=149,
        restaurant_id=restaurant3.id
    )

    item6 = MenuItem(
        name="French Fries",
        description="Crispy golden fries",
        price=99,
        restaurant_id=restaurant3.id
    )

    db.session.add_all([
        item1,
        item2,
        item3,
        item4,
        item5,
        item6
    ])

    db.session.commit()

    print("Restaurant and menu data added successfully!")