from nicegui import ui
with ui.column().classes(
    "w-full h-screen items-centre justify centre bg-slate-950"
):
    with ui.card().classes(
        "w-96 items-centre p-10"
    ):
        ui.label("Arashi-OS").classes(
            "text-4*1 font-bold"
        )

        ui.label("intialising Arashi-OS....").classes(
            "text-grey-400"
        )

        ui.spinner(size='lg')

ui.run()