
def test_home_page_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"RecipeHub" in response.data


def test_about_page_is_public(client):
    assert client.get("/about").status_code == 200


def test_recipe_detail_page(client, recipe):
    response = client.get(f"/recipes/{recipe.id}")
    assert response.status_code == 200
    assert b"Pasta Carbonara" in response.data


def test_unknown_page_returns_custom_404(client):
    response = client.get("/this-does-not-exist")
    assert response.status_code == 404
    assert b"404" in response.data


def test_anonymous_user_redirected_from_add_recipe(client):
    response = client.get("/recipes/add")
    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]