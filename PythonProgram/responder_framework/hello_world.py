import responder

api = responder.API()


# @api.route("/")
# def hello_world(req, resp):
#     resp.text = "hello, world!"

@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}

api.run(port=8000)
