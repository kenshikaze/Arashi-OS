from nicegui import ui
ui.query('body').classes('m-0')

with ui.element('div').classes(
    "w-full h-screen flex items-center justify-center bg-slate-950"
):
    ui.image
    with ui.card().classes(
        "w-100 items-center p-10"
    ):
        ui.label("Arashi-OS").classes(
            "text-4xl font-bold"
        )

        ui.label("intialising Arashi-OS....").classes(
            "text-grey-400"
        )

        ui.spinner(size='lg')


ui.run()