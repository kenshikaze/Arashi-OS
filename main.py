from nicegui import ui
ui.query('body').classes('m-0')

from nicegui import app
app.add_static_files('/assets', 'assets')

with ui.element('div').classes(
    "w-full h-screen flex items-center justify-center bg-slate-950"
):
        with ui.card().classes(
    "w-100 items-left"
        ):
            ui.image('/assets/storm_background.jpg'
            ).classes("w-full h-40 rounded-lg mb-4")
            ui.label("Arashi-OS").classes(
            "text-4xl font-bold"
            )
            with ui.row().classes("w-full justify-between"
            ):
                ui.label("intialising Arashi-OS....").classes(
                "text-gray-400"
                )
                ui.spinner(size='lg')

ui.run()