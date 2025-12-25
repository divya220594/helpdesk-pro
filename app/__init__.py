from flask import Flask, render_template, request, redirect, url_for
from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change-this-secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        return render_template("home.html")
    
    with app.app_context():
            from app import models
            db.create_all()
    
    from app.models import Ticket

    @app.route("/tickets/new", methods=["GET", "POST"])
    def new_ticket():
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            priority = request.form["priority"]

            ticket = Ticket(title=title, description=description, priority=priority)
            db.session.add(ticket)
            db.session.commit()

            return redirect(url_for("home"))

        return render_template("new_ticket.html")

    @app.route("/tickets")
    def tickets():
        all_tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
        return render_template("tickets.html", tickets=all_tickets)

    @app.route("/tickets/<int:ticket_id>")
    def ticket_detail(ticket_id):
            ticket = Ticket.query.get_or_404(ticket_id)
            return render_template("ticket_detail.html", ticket=ticket)

    return app
