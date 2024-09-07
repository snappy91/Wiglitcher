# Metadata page

import flet as ft

from .mediawiki import *


class Metadata(ft.View):
    """Wikimedia data page"""

    def __init__(self, page):
        super().__init__()
        self.route = "/"
        self.page = page
        self.wiki_data = self.page.client_storage.get("wiki_data")
        self.wiki_index = self.page.client_storage.get("wiki_index")
        self.controls = [ 

            ft.ListTile(
                leading=ft.Icon(ft.icons.ALBUM),
                title=ft.Text("WikiGlitcher"),
                subtitle=ft.Text(
                    "GLAMhack 2024 ~ zHB Luzern"
                ),
            ),

            ft.Column(self.column(self)) 
        ]

    def column(self, e):
        if not self.wiki_data:
            print("Loading fresh data ...")
            self.wiki_data = get_random_images(10)
            #self.wiki_data = [ get_todays_image() ]
            self.page.client_storage.set('wiki_data', self.wiki_data)
            self.page.client_storage.set('wiki_index', 0)

        idx = self.page.client_storage.get('wiki_index')
        self.page.client_storage.set('wiki_index', idx + 1)
        if idx == len(self.wiki_data):
            idx = 0
        return [
            ft.Image(
                src=self.wiki_data[idx]['thumbnail_url'],
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN
            ),

            ft.Text(self.wiki_data[idx]['description_text']),
            ft.Text(f"Artist: " + self.wiki_data[idx]['artist_name']),
            ft.Text(f"License: " + self.wiki_data[idx]['license_name']),

            ft.Row(
                [
                    ft.TextButton("Hot", on_click=lambda e: self.page.go("/hotshot")), 
                    ft.TextButton("Not", on_click=lambda _: self.page.go("/detect"))
                ],
                #alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
