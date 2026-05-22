from flask import Flask, render_template
from app.routes.ai_routes import register_ai_routes
from app.routes.scheduler_routes import register_scheduler_routes

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

register_ai_routes(app)
register_scheduler_routes(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
