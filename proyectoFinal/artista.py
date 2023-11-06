from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from proyectoFinal.db import get_db

bp = Blueprint('artista', __name__)

@bp.route('/artista')
def index():
    db = get_db()
    cancion = db.execute(
        """SELECT t.name AS Cancion, a.name AS Artista FROM tracks t
           JOIN albums al ON t.AlbumId = al.AlbumId
           JOIN artists a ON al.ArtistId = a.ArtistId"""
    ).fetchall()
    return render_template('artista/index.html', cancion=cancion)