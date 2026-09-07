from flask import render_template


def register_error_handlers(app):
    @app.errorhandler(403)
    def forbidden(error):
        app.logger.warning("403 Forbidden: %s", error)
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        from app.extensions import db
        db.session.rollback()
        app.logger.error("Server exception: %s", error, exc_info=True)
        return render_template("errors/500.html"), 500