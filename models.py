from app import db

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    sale = db.Column(db.Float)

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    name = db.Column(db.String)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String)
    size = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    nova_posta = db.Column(db.String)
    status = db.Column(db.String, default = "Очікування")
