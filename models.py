from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


"""Models for Cupcake app"""

DEFAULT_IMAGE="https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """ Cupcake model w/ flavor, size, rating, image_url;
        serialize method for formatting as dictionary"""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    flavor = db.Column(
        db.String(50),
        nullable=False
    )

    size = db.Column(
        db.String(15),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    image_url = db.Column(
        db.String(500),
        nullable=False,
        default=DEFAULT_IMAGE
    )

    def serialize(self):
        """ serialize to dictionary """

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image_url": self.image_url,
        }


def connect_db(app):
    """Connect this database to provided Flask app"""

    app.app_context().push()
    db.app = app
    db.init_app(app)
