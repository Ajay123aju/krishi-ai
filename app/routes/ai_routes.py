from flask import request, render_template
from app.services.ai_service import get_ai_response

def register_ai_routes(app):

    @app.route("/ask", methods=["POST"])
    def ask():
        question = request.form.get("question")

        if not question:
            return render_template(
                "index.html",
                response="Please enter a question",
                question=""
            )

        answer = get_ai_response(question)

        return render_template(
            "index.html",
            response=answer,
            question=question
        )