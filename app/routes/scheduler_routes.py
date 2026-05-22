from flask import request, render_template
from app.services.scheduler_service import get_crop_schedule

def register_scheduler_routes(app):
    @app.route("/schedule", methods=["POST"])
    def schedule():
        crop_type = request.form.get("crop_type")
        planting_date = request.form.get("planting_date")
        
        if not crop_type or not planting_date:
            return render_template(
                "index.html",
                schedule_error="Please provide both crop type and planting date."
            )
            
        schedule_data = get_crop_schedule(crop_type, planting_date)
        
        return render_template(
            "index.html",
            schedule_data=schedule_data,
            crop_type=crop_type,
            planting_date=planting_date
        )
