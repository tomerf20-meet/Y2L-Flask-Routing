from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def Add_Product(name, price, picture_link, description):
	product_object = Product(
        Name=name,
        Price=price,
        Picture_Link=picture_link,
        Description=description)
    session.add(product_object)
    session.commit()
    print(Name)

def Update_Product(id, name, price, picture_link, description):
	product_object = session.query(
		Product).filter_by(
    	id=id).first()
	product_object.name = name
	product_object.price = price
	product_object.picture_link = picture_link
	product_object.description = description
	session.commit()

def Delete_Product(id):
	product_object = session.query(
		Product).filter_by(
		id=id).delete()
	sesson.commit()

def Query_All():
	products = session.query(
		Product).all()
	return products

print(Query_All())

def Query_by_Id(id):
	product = session.query(
    	Product).filter_by(
    	id=id).first()
	return product

def Add_to_Cart(productID):
	cart_object = Cart()
	cart_object.productID = productID
	session.add(cart_object)
	session.commit()




Add_Product("Olive Pizza", 15.99, "https://slice.seriouseats.com/images/2011/08/20110822-olives-poll-way-or-no-way.jpg", "Best Olive Pizza in the Area")




