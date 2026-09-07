from app.models import Recipe


def test_owner_can_open_edit_page(client, recipe, login):
    login("alice@example.com")
    assert client.get(f"/recipes/{recipe.id}/edit").status_code == 200


def test_other_user_cannot_edit_recipe(client, recipe, other_user, login):
    login("bob@example.com")  # User B
    assert client.get(f"/recipes/{recipe.id}/edit").status_code == 403

    response = client.post(
        f"/recipes/{recipe.id}/edit",
        data={
            "title": "Hacked title",
            "short_description": "Trying to overwrite someone else's recipe.",
            "instructions": "Nope.",
            "category": "Dinner",
            "preparation_time": 5,
            "servings": 1,
        },
    )
    assert response.status_code == 403
    assert Recipe.query.get(recipe.id).title == "Pasta Carbonara"  # unchanged


def test_other_user_cannot_delete_recipe(client, recipe, other_user, login):
    login("bob@example.com")  # User B
    response = client.post(f"/recipes/{recipe.id}/delete")
    assert response.status_code == 403
    assert Recipe.query.get(recipe.id) is not None


def test_owner_can_delete_recipe(client, recipe, login):
    login("alice@example.com")
    recipe_id = recipe.id
    response = client.post(f"/recipes/{recipe_id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert Recipe.query.get(recipe_id) is None