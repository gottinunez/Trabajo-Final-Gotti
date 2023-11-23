from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from proyectoFinal.db import get_db

bp = Blueprint('album', __name__)

@bp.route('/album')
def index():
    db = get_db()
    album = db.execute(
        """SELECT title AS Album, ar.name AS Artista, sum(Milliseconds) AS Duración
        FROM albums a 
        JOIN artists ar ON ar.ArtistId = a.ArtistId
        JOIN tracks t ON t.AlbumId = a.AlbumId
        GROUP BY Album
        ORDER BY Artista ASC"""   
    ).fetchall()
    return render_template('Album/index.html', album=album)

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    canciones = db.execute(
        """SELECT t.name AS Cancion, Milliseconds AS Duracion, title AS Album
            FROM tracks t JOIN albums a ON t.AlbumId = a.AlbumId
            WHERE a.AlbumId = ?
            ORDER BY Cancion ASC"""  ,
        (id,)
    ).fetchall()

    return render_template('Album/detalle.html', canciones=canciones)