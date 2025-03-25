import flet
import requests
# allt som är 1 är recepten och allt som ör 2 är info
#key s är recept, key i är info

class SearchField1(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        if self.visible == True:
            SearchField2.visible = False
    def show_recepie(self, ):
        self.controls = []


class SearchField2(flet.ListView):
    def __init__(self):
        super().__init__()
        self.expand = True
        if self.visible == True:
            SearchField1.visible = False

def main(page: flet.Page):

    def search1(e):
        s_value = {
            "s": recepie_box.value
        }
        recepie_result = requests.get("www.thecocktaildb.com/api/json/v1/1/search.php?", params=s_value)
        recepie_result_json = recepie_result.json()


    def search2(e):
        i_value = {
            "key": "i",
            "i": fact_box.value
        }
        facts_result = requests.get("www.thecocktaildb.com/api/json/v1/1/search.php?", params=i_value)
        facts_result_json = facts_result.json()

    recepie_box = flet.TextField(label="What drink are you looking to make?")
    search_button1 = flet.TextButton("Search")
    fact_box = flet.TextField(label="Facts about a chosen drink")
    search_button2 = flet.TextButton("Search")

    search_button1.on_submit = SearchField1
    search_button1.on_click =

    page.add(flet.Row(
        controls=[
            recepie_box,
            search_button1,
         ]
    ))
    page.add(flet.Row(
        controls=[
            fact_box,
            search_button2
        ]
    ))
    page.add(SearchField1)

flet.app(main)

#on_submit för att söka med enter