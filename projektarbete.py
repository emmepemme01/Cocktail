import flet
import requests
# allt som är 1 är recepten och allt som ör 2 är info
#key s är recept, key i är info

class SearchField1(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
    def show_recepie(self,recepie_result_json ):
        self.controls = [Recepie(recepie_result_json)]
        self.update()

class Recepie(flet.Container):
    def __init__(self, recepie_result_json):
        super().__init__()
        self.expand = True

        if "drinks" in recepie_result_json and recepie_result_json["drinks"]:
            drink = recepie_result_json["drinks"][0]
            drink_name = drink.get("strDrink", "okänd drink")

            ingredients = []
            for i in range(1, 15):
                ingredient = drink.get(f"strIngredient{i}")
                measure = drink.get(f"strMeasure{i}")
                if ingredient:
                    ingredients.append(f"{measure or ''}{ingredient}")
                    self.content = flet.Column([
                        flet.Text(drink_name),
                        flet.Column([flet.Text(ing) for ing in ingredients])
                        ])
        else:
            self.content = flet.Text("No recepies found")


class SearchField2(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True

def main(page: flet.Page):
    recepie_box = flet.TextField(label="What drink are you looking to make?")
    recepie_view = SearchField1()

    def search1(e):
        s_value = {"s": recepie_box.value}
        recepie_result = requests.get("https://thecocktaildb.com/api/json/v1/1/search.php?", params=s_value)
        recepie_result_json = recepie_result.json()

        recepie_view.show_recepie(recepie_result_json)

    def search2(e):
        i_value = {
            "key": "i",
            "i": fact_box.value
        }
        facts_result = requests.get("https://thecocktaildb.com/api/json/v1/1/search.php?", params=i_value)
        facts_result_json = facts_result.json()


    search_button1 = flet.ElevatedButton("Search", on_click=search1)
    fact_box = flet.TextField(label="Facts about a chosen drink")
    search_button2 = flet.TextButton("Search")

    search_button1.on_submit = SearchField1

    recepie_visivle = page.add(flet.Row([recepie_box, search_button1]))

    page.add(flet.Row(
        controls=[
            fact_box,
            search_button2
        ]
    ))
    if recepie_visivle = True
        pass
    page.add(recepie_view)


flet.app(target=main)

#on_submit för att söka med enter