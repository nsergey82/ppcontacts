from flask import Flask, redirect
from w3ds.utils import VaultIO, envelope_to_py
import os

app = Flask(__name__, static_folder="static", static_url_path="")
token = os.getenv("PP_JWT_TOKEN", "secret")
ename = "@82f7a77a-f03a-52aa-88fc-1b1e488ad498"
ONTOLOGY = "contacts"


@app.route("/")
def index():
    vio = VaultIO(token, ename)
    return [str(envelope_to_py(x)) for x in vio.get_envelopes_for_ontology(ONTOLOGY)]


@app.route("/add/<ename_to_add>/<alias>")
def add(ename_to_add: str, alias: str):
    vio = VaultIO(token, ename)
    rc = vio.store_envelopes(ONTOLOGY, {"ename": ename_to_add, "alias": alias})
    print(rc)
    return redirect("/")
