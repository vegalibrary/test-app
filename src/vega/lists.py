import flet as ft


class ListView(ft.Column):
    def __init__(self, items=[]):
        super().__init__(
            controls=items, spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.items = items


class ListItem(ft.Container):
    def __init__(
        self,
        title,
        subtitle=None,
        leading_icon=None,
        trailing_icon=None,
        on_click=None,
        ink=True,
        leading_icon_clickable=False,
        trailing_icon_clickable=True,
        border_radius=0,
        icon_radius=12,
    ):
        # Initialize the Container with default properties
        super().__init__(
            padding=ft.Padding(left=12, top=12, bottom=12, right=8),
            border_radius=border_radius,
            ink=ink,
            on_click=on_click,
            border=ft.Border(
                bottom=ft.BorderSide(
                    color=ft.Colors.with_opacity(0.1, ft.Colors.OUTLINE),
                    width=1,
                ),
            ),
        )

        # Set attributes
        self.title = title
        self.subtitle = subtitle
        self.leading_icon = leading_icon
        self.trailing_icon = trailing_icon
        self.leading_icon_clickable = leading_icon_clickable
        self.trailing_icon_clickable = trailing_icon_clickable
        self.icon_radius = icon_radius

        # Build the content of the container
        self.content = ft.Row(
            controls=[
                self._build_leading_icon(),
                ft.Column(
                    spacing=10,
                    expand=True,
                    controls=[
                        ft.Text(value=self.title, size=14, weight=ft.FontWeight.W_500),
                        (
                            ft.Text(
                                value=self.subtitle,
                                size=14,
                                color=ft.Colors.OUTLINE,
                                visible=self.subtitle is not None,
                            )
                            if self.subtitle
                            else None
                        ),
                    ],
                ),
                self._build_trailing_icon(),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def _build_leading_icon(self):
        # Create leading icon if provided
        if self.leading_icon is not None:
            if isinstance(self.leading_icon, ft.Control):
                wrapped_icon = (
                    ft.Container(
                        content=self.leading_icon,
                        border_radius=self.icon_radius,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    )
                    if isinstance(self.leading_icon, ft.Image)
                    else self.leading_icon
                )
                if self.leading_icon_clickable:
                    return ft.IconButton(
                        content=wrapped_icon,
                        style=ft.ButtonStyle(
                            padding=0,
                            shape=ft.RoundedRectangleBorder(radius=self.icon_radius),
                        ),
                    )
                return wrapped_icon

            if self.leading_icon_clickable:
                return ft.IconButton(
                    icon=self.leading_icon,
                    icon_color=ft.Colors.ON_SURFACE_VARIANT,
                    style=ft.ButtonStyle(
                        padding=0,
                        shape=ft.RoundedRectangleBorder(radius=self.icon_radius),
                    ),
                )
            return ft.Icon(name=self.leading_icon, color=ft.Colors.ON_SURFACE_VARIANT)
        return None

    def _build_trailing_icon(self):
        # Create trailing icon if provided
        if self.trailing_icon is not None:
            if isinstance(self.trailing_icon, ft.Control):
                return self.trailing_icon
            if self.trailing_icon_clickable:
                return ft.IconButton(
                    icon=self.trailing_icon,
                    icon_color=ft.Colors.ON_SURFACE_VARIANT,
                    style=ft.ButtonStyle(
                        padding=0,
                        shape=ft.RoundedRectangleBorder(radius=self.icon_radius),
                    ),
                )
            return ft.Icon(name=self.trailing_icon, color=ft.Colors.ON_SURFACE_VARIANT)
        return None
