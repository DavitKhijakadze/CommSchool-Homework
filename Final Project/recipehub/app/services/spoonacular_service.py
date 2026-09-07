import requests
from flask import current_app

SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"


def get_recipe_nutrition(recipe):
    """Return a dict with calories/protein/fat/carbs, or None if unavailable."""
    api_key = current_app.config.get("SPOONACULAR_API_KEY")
    if not api_key:
        current_app.logger.warning(
            "Spoonacular API key is not configured; skipping nutrition lookup for: %s", recipe.title
        )
        return None

    params = {
        "apiKey": api_key,
        "query": recipe.title,
        "number": 1,
        "addRecipeNutrition": True,
    }

    try:
        response = requests.get(
            SEARCH_URL, params=params, timeout=current_app.config.get("SPOONACULAR_TIMEOUT", 5)
        )
        if response.status_code != 200:
            current_app.logger.error(
                "Spoonacular API request failed for recipe: %s (status %s)",
                recipe.title, response.status_code,
            )
            return None

        results = response.json().get("results") or []
        if not results:
            current_app.logger.info("Spoonacular returned no results for recipe: %s", recipe.title)
            return None

        nutrients = results[0].get("nutrition", {}).get("nutrients", [])
        wanted = {"Calories", "Protein", "Fat", "Carbohydrates"}
        nutrition = {
            n["name"]: f"{round(n['amount'], 1)} {n['unit']}"
            for n in nutrients
            if n.get("name") in wanted
        }
        return nutrition or None

    except requests.RequestException as exc:
        current_app.logger.error(
            "Spoonacular API request failed for recipe: %s (%s)", recipe.title, exc
        )
        return None
    except (ValueError, KeyError, TypeError) as exc:
        current_app.logger.error(
            "Spoonacular API returned invalid data for recipe: %s (%s)", recipe.title, exc
        )
        return None