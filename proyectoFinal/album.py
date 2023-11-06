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
    return render_template('album/index.html', albums=albums)