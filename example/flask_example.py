from respond import Responder, JSONResponse, TextResponse, XMLResponse

from flask import Flask


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/txt")
def txt():
    """ Return a text response with an HTTP 200 OK status """
    return Responder.text.ok("hi")


@app.route("/json")
def json():
    """ Return a JSON response with an HTTP 200 OK status """
    data: dict = {"data": ["here", "you", "go"]}
    return Responder.json.ok(data)


@app.route("/xml")
def xml():
    """ Return an XML response with an HTTP 200 OK status """
    data: str = """<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://www.example.com/</loc>
      <lastmod>2005-01-01</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
   </url>
</urlset> 
    """
    return Responder.xml.ok(data)


@app.route("/json/bad-request")
def json_bad_request():
    """ Return a JSON response with an HTTP 400 BAD REQUEST status """
    return Responder.json.bad_request({"error": {"message": "You did something wrong"}})


@app.route("/json/internal-server-error")
def json_internal_server_error():
    """ Return a JSON response with an HTTP 500 INTERNAL SERVER ERROR status """
    return Responder.json.internal_server_error({"error": {"message": "We did something wrong"}})


@app.route("/json/created")
def json_created():
    """ Return a JSON response with an HTTP 201 CREATED status """
    return Responder.json.created({"data": {"here": ["is", "what", "you", "created"]}})


if __name__ == "__main__":
    app.run()
