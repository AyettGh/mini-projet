from surveillance_api.models import Formula


def calculate_max_hours(row):
    formula_instance = Formula.objects.first(formula="(courses + td + tp * 0.75)*coef",coef="0.3")
    formula = formula_instance.formula if formula_instance else "courses + td + tp"
    try:
        # Map Excel column names to formula variable names
        context = {
            "courses": row.get("Cours", 0),
            "td": row.get("TD", 0),
            "tp": row.get("TP", 0),
            "coef": row.get("coef", 0)
        }
        max_hours = eval(formula, context)
        return max_hours
    except Exception as e:
        print(f"Error evaluating formula: {e}")
        return 0