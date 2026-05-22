from datetime import datetime, timedelta

def get_crop_schedule(crop_type, planting_date_str):
    try:
        planting_date = datetime.strptime(planting_date_str, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD."}
        
    crop = crop_type.strip().lower()
    
    # Simple rule engine
    if crop == "tomato":
        irrigation = [
            "Every 2 days (early stage)",
            "Every 3 days (mid stage)"
        ]
        fertilizer = [
            "Week 2: Nitrogen boost",
            "Week 5: Balanced NPK",
            "Week 8: Potassium support"
        ]
        harvest = [
            "90–110 days after planting",
            f"Expected: {(planting_date + timedelta(days=100)).strftime('%B %Y')}"
        ]
    elif crop == "wheat":
        irrigation = [
            "Day 21: Crown root initiation",
            "Day 60: Booting stage",
            "Day 80: Flowering stage"
        ]
        fertilizer = [
            "Day 1: Nitrogen at planting",
            "Day 30: Tillering phase",
            "Day 60: Booting phase"
        ]
        harvest = [
            "120–130 days after planting",
            f"Expected: {(planting_date + timedelta(days=125)).strftime('%B %Y')}"
        ]
    elif crop == "rice":
        irrigation = [
            "Maintain continuous flooding (2-5 cm deep)",
            "Drain 2 weeks before harvest"
        ]
        fertilizer = [
            "Day 20: Nitrogen at tillering",
            "Day 50: Panicle initiation"
        ]
        harvest = [
            "130-140 days after planting",
            f"Expected: {(planting_date + timedelta(days=135)).strftime('%B %Y')}"
        ]
    elif crop == "corn":
        irrigation = [
            "Day 1-40: Regular watering",
            "Day 50-60: Critical during tasseling and silking"
        ]
        fertilizer = [
            "Day 1: Nitrogen at planting",
            "Day 30: Knee-high stage"
        ]
        harvest = [
            "90-100 days after planting",
            f"Expected: {(planting_date + timedelta(days=95)).strftime('%B %Y')}"
        ]
    else:
        irrigation = [
            "Standard regular watering",
            "Monitor soil moisture daily"
        ]
        fertilizer = [
            "Day 1: Balanced NPK at planting",
            "Mid-growth: Additional nutrient support"
        ]
        harvest = [
            "Approx. 90 days after planting",
            f"Expected: {(planting_date + timedelta(days=90)).strftime('%B %Y')}"
        ]

    return {
        "crop": crop.capitalize(),
        "planting_date": planting_date.strftime("%Y-%m-%d"),
        "irrigation": irrigation,
        "fertilizer": fertilizer,
        "harvest_estimate": harvest
    }
