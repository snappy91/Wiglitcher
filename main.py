import datetime
import requests, json
import flet as ft

from pages.hotshot import Hotshot
from pages.metadata import Metadata
from pages.detect import Detect
from pages.improve import Improve


def main(page: ft.Page):
    page.title = "⋆ ◎ ✾ WIGLITCHER ✾ ◎ ⋆"
    page.bgcolor = ft.colors.TRANSPARENT
    page.adaptive = True

    def route_change(route):
        page.views.clear()

        page.views.append(Metadata())

        if page.route == "/hotshot":
            page.views.append(Hotshot())
        if page.route == "/detect":
            page.views.append(Detect())
        if page.route == "/improve":
            page.views.append(Improve())
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main) #, view=ft.AppView.WEB_BROWSER)
