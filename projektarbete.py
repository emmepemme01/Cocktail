import flet
import requests

# allt som är 1 är recepten och allt som är 2 är info
#key 's är recept, key 'i är info

class SearchField1(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
    def show_recepie(self,recepie_result_json ):
        self.controls = [Recepie(recepie_result_json)]
        self.visible = True
        self.update()


class Recepie(flet.Container):
    def __init__(self, recepie_result_json):
        super().__init__()
        self.expand = True

        if "drinks" in recepie_result_json and recepie_result_json["drinks"]:
            drink = recepie_result_json["drinks"][0]
            drink_name = drink.get("strDrink", "okänd drink")
            instructions_en = flet.Text(
                drink.get("strInstructions", "No instructions available"),
                width=300,
                bgcolor="#f1f1f1",
                color="black"
            )
            instructions_de = flet.Text(
                drink.get("strInstructionsDE", "Keine Anweisungen verfügbar"),
                width=300,
                bgcolor="#f1f1f1",
                color="black"
            )
            instructions_es = flet.Text(
                drink.get("strInstructionsES", "No hay instrucciones disponibles"),
                width=300,
                bgcolor="#f1f1f1",
                color="black"
            )


            ingredients = []
            for i in range(1, 15):
                ingredient = drink.get(f"strIngredient{i}")
                measure = drink.get(f"strMeasure{i}")
                if ingredient:
                    ingredients.append(f"{measure or ''}{ingredient}")


                self.content = flet.Column([flet.Row([
                    flet.Text(drink_name, size=35, weight="W_500", color="black"),
                    flet.Column([flet.Text(ing, bgcolor="#f1f1f1", color="black")for ing in ingredients])],
                    alignment=flet.MainAxisAlignment.CENTER),
                    flet.Column([flet.Text("English: ", weight="bold", color="black" ), instructions_en,
                                flet.Text("German: ", weight="bold", color="black"), instructions_de,
                                 flet.Text("Spanish: ", weight="bold", color="black"), instructions_es,
                                 flet.Text("-" + (drink.get("strAlcoholic")), size=20, weight="bold", color="black")],
                                alignment=flet.MainAxisAlignment.CENTER)],
                                    alignment=flet.MainAxisAlignment.CENTER,
                                    horizontal_alignment=flet.CrossAxisAlignment.CENTER)
        else:
            self.content = flet.Text("No recepies found")


class SearchField2(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
    def show_fact(self, fact_result_json):
        self.controls = [Facts(fact_result_json)]
        self.visible = True
        self.update()

class Facts(flet.Container):
    def __init__(self, fact_result_json):
        super().__init__()
        self.expand = True

        if "ingredients" in fact_result_json and fact_result_json["ingredients"]:
            fact = fact_result_json["ingredients"][0]
            fact_name = fact.get("strIngredient", "No information found")
            description = fact.get("strDescription", "No description available")
            percentage = fact.get("strABV", "Unknown percentage")

            self.content = (flet.Column([
                    flet.Text(fact_name, size=35, weight="W_500", color="black"),
                    flet.Text(description, width=650, bgcolor="#f1f1f1", color="black"),
                    flet.Row([
                        flet.Text("Percentage", size=20, color="black"),
                        flet.Text(f"{percentage}%", size=18, color="black")],
                    alignment=flet.MainAxisAlignment.CENTER,
                    )

            ], alignment=flet.MainAxisAlignment.CENTER,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER))
        else:
            self.content = flet.Text("No information available.")

def main(page: flet.Page):
    def search1(e):
        s_value = {"s": recepie_box.value}
        recepie_result = requests.get("https://thecocktaildb.com/api/json/v1/1/search.php?",
                                      params=s_value,)
        recepie_result_json = recepie_result.json()

        recepie_view.show_recepie(recepie_result_json)
        facts_view.visible = False

        recepie_box.value = ""
        page.update()

    def search2(e):
        i_value = {
            "i": fact_box.value
        }
        facts_result = requests.get("https://thecocktaildb.com/api/json/v1/1/search.php?", params=i_value)
        facts_result_json = facts_result.json()

        facts_view.show_fact(facts_result_json)
        recepie_view.visible = False

        fact_box.value = ""
        page.update()


    recepie_box = flet.TextField(label="What drink are you looking to make?", bgcolor="#919395")
    recepie_view = SearchField1()
    search_button1 = flet.Button("Search", color="#e2def3", on_click=search1)
    recepie_box.on_submit = search1


    fact_box = flet.TextField(label="Facts about beverage", bgcolor="#919395")
    facts_view = SearchField2()
    search_button2 = flet.Button("Search", color="#e2def3", on_click=search2)
    fact_box.on_submit = search2

    content = flet.Column([
        flet.Row([recepie_box, search_button1], alignment=flet.MainAxisAlignment.CENTER),
        flet.Row([fact_box, search_button2], alignment=flet.MainAxisAlignment.CENTER),
        recepie_view,
        facts_view,

    ], alignment=flet.MainAxisAlignment.START, expand=True, scroll="auto")
    page.add(flet.Stack(
    controls=[
        flet.Image(
            src="summer_cocktails.jpg", width=1500, height=1100,
            expand=True,
            fit=flet.ImageFit.COVER,
        ),
        content],
    expand=True))

flet.app(target=main)