from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    request,
    flash
)

from app import db
from app.models import (
    Restaurant,
    MenuItem,
    User,
    Order,
    OrderItem
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)


main = Blueprint("main", __name__)


# ================= HOME =================

@main.route("/")
def index():
    return render_template("index.html")


# ================= REGISTER =================

@main.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            flash("Email already registered!")
            return redirect(url_for("main.register"))

        user = User(
            name=name,
            email=email,
            password=password,
            role="customer"
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.")

        return redirect(url_for("main.login"))

    return render_template("register.html")


# ================= LOGIN =================

@main.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        if user and user.password == password:

            login_user(user)

            return redirect(
                url_for("main.index")
            )

        flash("Invalid email or password!")

    return render_template("login.html")


# ================= LOGOUT =================

@main.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("main.index")
    )


# ================= RESTAURANTS =================

@main.route("/restaurants")
def restaurants():

    restaurants = Restaurant.query.all()

    return render_template(
        "restaurants.html",
        restaurants=restaurants
    )


# ================= RESTAURANT MENU =================

@main.route("/restaurant/<int:restaurant_id>")
def restaurant_menu(restaurant_id):

    restaurant = Restaurant.query.get_or_404(
        restaurant_id
    )

    return render_template(
        "menu.html",
        restaurant=restaurant
    )


# ================= ADD TO CART =================

@main.route("/add-to-cart/<int:item_id>")
def add_to_cart(item_id):

    item = MenuItem.query.get_or_404(
        item_id
    )

    cart = session.get("cart", {})

    item_id = str(item.id)

    if item_id in cart:

        cart[item_id] += 1

    else:

        cart[item_id] = 1

    session["cart"] = cart
    session.modified = True

    return redirect(
        url_for("main.cart")
    )


# ================= CART =================

@main.route("/cart")
def cart():

    cart = session.get("cart", {})

    cart_items = []
    total = 0

    for item_id, quantity in cart.items():

        item = MenuItem.query.get(
            int(item_id)
        )

        if item:

            subtotal = item.price * quantity

            cart_items.append({
                "item": item,
                "quantity": quantity,
                "subtotal": subtotal
            })

            total += subtotal

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# ================= CHECKOUT =================

@main.route("/checkout")
def checkout():

    cart = session.get("cart", {})

    if not cart:

        return redirect(
            url_for("main.cart")
        )

    cart_items = []
    total = 0

    for item_id, quantity in cart.items():

        item = MenuItem.query.get(
            int(item_id)
        )

        if item:

            subtotal = item.price * quantity

            cart_items.append({
                "item": item,
                "quantity": quantity,
                "subtotal": subtotal
            })

            total += subtotal

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )


# ================= PLACE ORDER =================

@main.route(
    "/place-order",
    methods=["POST"]
)
@login_required
def place_order():

    cart = session.get("cart", {})

    if not cart:

        return redirect(
            url_for("main.cart")
        )

    total = 0
    order_items = []

    for item_id, quantity in cart.items():

        item = MenuItem.query.get(
            int(item_id)
        )

        if item:

            subtotal = item.price * quantity

            total += subtotal

            order_items.append({
                "item": item,
                "quantity": quantity
            })

    order = Order(
        total_amount=total,
        status="Order Placed",
        user_id=current_user.id
    )

    db.session.add(order)
    db.session.commit()

    for order_item in order_items:

        new_item = OrderItem(
            quantity=order_item["quantity"],
            price=order_item["item"].price,
            order_id=order.id,
            menu_item_id=order_item["item"].id
        )

        db.session.add(new_item)

    db.session.commit()

    session.pop("cart", None)

    return render_template(
        "order_success.html",
        order=order
    )