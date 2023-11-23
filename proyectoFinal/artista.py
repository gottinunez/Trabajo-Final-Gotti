from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from proyectoFinal.db import get_db

bp = Blueprint('artista', __name__)

@bp.route('/artista')
def index():
    db = get_db()
    artistas = db.execute(
        """SELECT ar.name AS Nombre, count(al.AlbumId) AS Albums
         FROM artists ar JOIN albums al ON ar.ArtistId = al.ArtistId
		 GROUP BY Nombre
         ORDER BY Nombre ASC"""
    ).fetchall()
    return render_template('Artista/index.html', artistas=artistas)

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    artista = db.execute(
        """SELECT name AS Nombre, ArtistId
            FROM artists
		    WHERE ArtistId = ?"""   ,
        (id,)
    ).fetchone()

    albums = db.execute(
        """SELECT title AS Album, sum(Milliseconds) AS Duración, g.name AS Genero, count(t.TrackID) AS Cantidad
            FROM albums a JOIN artists ar ON ar.ArtistId = a.ArtistId
            JOIN tracks t ON t.AlbumId = a.AlbumId
            JOIN genres g ON t.GenreId = g.GenreId
            WHERE ar.ArtistId = ?
            GROUP BY Album
            ORDER BY Album ASC"""  ,
        (id,)
    ).fetchall()

    return render_template('Artista/detalle.html', artista=artista, album=album)