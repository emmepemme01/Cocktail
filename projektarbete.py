import flet
import requests

def main(page: flet.Page):

    search_box1 = flet.TextField(label="What drink are you looking to make?")
    search_button1 = flet.TextButton("Search")
    search_box2 = flet.TextField(label="Facts about a chosen drink:")
    search_button2 = flet.TextButton("Search")

    page.add(flet.Row(
        controls=[
            search_box1,
            search_button1,
         ]
    ))
    page.add(flet.Row(
        controls=[
            search_box2,
            search_button2
        ]
    ))


flet.app(main)