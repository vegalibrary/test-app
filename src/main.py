import flet as ft
from vega.lists import ListView, ListItem


def main(page: ft.Page):
    # Page configuration
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.SURFACE
    page.padding = 0
    page.window.min_width = 360

    # App bar
    appbar_title = ft.Text(value="Chat", size=22, weight=ft.FontWeight.BOLD)
    page.appbar = ft.AppBar(title=appbar_title, center_title=True)

    # Divider
    page.add(ft.Divider(height=1, opacity=0.13))

    # Navigation bar
    def change_appbar_title(e):
        selected_label = page.navigation_bar.destinations[
            page.navigation_bar.selected_index
        ].label
        page.appbar.title.value = selected_label
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                label="Chats",
                icon=ft.Icons.CHAT_OUTLINED,
                selected_icon=ft.Icons.CHAT_ROUNDED,
            ),
            ft.NavigationBarDestination(
                label="Updates",
                icon=ft.Icons.RADIO_BUTTON_UNCHECKED,
                selected_icon=ft.Icons.RADIO_BUTTON_CHECKED,
            ),
            ft.NavigationBarDestination(
                label="Communities",
                icon=ft.Icons.GROUPS_OUTLINED,
                selected_icon=ft.Icons.GROUPS_ROUNDED,
            ),
            ft.NavigationBarDestination(
                label="Calls",
                icon=ft.Icons.PHONE_OUTLINED,
                selected_icon=ft.Icons.PHONE_ROUNDED,
            ),
        ],
        on_change=change_appbar_title,
    )

    # List Items
    custom_image = ft.Image(
        src="src/assets/icon.png", width=40, height=40, fit=ft.ImageFit.CONTAIN
    )

    def handle_click(e):
        clicked_title = e.control.content.controls[1].controls[0].value
        print(f"Clicked: {clicked_title}")

    # List items data
    list_items_data = [
        ("Wireless Headphones", "Bluetooth Noise Cancelling"),
        ("Smart Watch", "Health Tracking"),
        ("Samsung S20 Ultra", "Health Tracking"),
    ]

    pb = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Item 1"),
            ft.PopupMenuItem(icon=ft.Icons.POWER_INPUT, text="Check power"),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                        ft.Text("Item with a custom content"),
                    ]
                ),
                on_click=lambda _: print("Button with a custom content clicked!"),
            ),
        ],
        icon_color=ft.Colors.ON_SURFACE_VARIANT,
    )

    # Generate list items dynamically
    list_items = [
        ListItem(
            title=title,
            subtitle=subtitle,
            leading_icon=custom_image,
            trailing_icon=pb,
            icon_radius=30,
            on_click=handle_click,
        )
        for title, subtitle in list_items_data
    ]

    # ListView content
    content = ListView(items=list_items)

    # Add content to the page
    page.add(content)


# Run the Flet app
ft.app(main)
