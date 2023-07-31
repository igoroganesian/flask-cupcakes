"""Flask app for Cupcakes"""

import os

from flask import Flask, request, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Cupcake, DEFAULT_IMAGE

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)


@app.get('/api/cupcakes')
def get_cupcakes():
    """ get data about all cupcakes

    returns JSON
      {
        "cupcakes": [
         {
            "id": ...,
            "flavor": ...,
            "size": ...,
            "rating": ...,
            "image_url": ...,
        }
      ]
    }
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """ get data about specific cupcake

    returns JSON
    {
      "cupcake": {
        "id": ...,
        "flavor": ...,
        "size": ...,
        "rating": ...,
        "image_url": ...,
        }
    }
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post('/api/cupcakes')
def create_cupcake():
    """ create cupcake from posted JSON data & return it

        accepts {flavor, size, rating, and (optional) image_url}

      Returns JSON {'cupcake': {id, flavor, size, rating, image_url}}
    """
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image_url = request.json['image_url'] or None #required

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image_url=image_url
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    """ updates cupcake with data from request body;
    may include flavor, size, rating, and/or image_url

    returns updated JSON
        {cupcake:
            {id, flavor, size, rating, image_url}}
    or 404
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # data_dict = request.json

    # cupcake.flavor = data.get('flavor', cupcake.flavor)
    # breakpoint()

    if request.json['flavor']:
        cupcake.flavor = request.json['flavor']

    if request.json['size']:
        cupcake.size = request.json['size']

    if request.json['rating']:
        cupcake.rating = request.json['rating']

    if 'image_url' in request.json:
        cupcake.image_url = request.json['image_url'] or DEFAULT_IMAGE

    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)


@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """ removes cupcake record with cupcake_id from API
    responds with: {deleted: cupcake-id}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"deleted": cupcake_id})