from nicegui import ui, app
ui.query('body').classes('m-0')
app.add_static_files('/assets', 'assets')

with ui.element('div').classes(
    "w-full h-screen flex items-center justify-center bg-slate-950"
) as boot_screen:
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

with ui.element('div').classes(
     "w-full h-screen text-white" \
     "background-image: url('/assets/cherry_blossom.jpg)" \
     " flex flex-col").style( 'background-size: cover background-position: center background-repeat: no-repeat')as desktop_screen:
     pass

desktop_screen.set_visibility(False)

def finish_boot():
     boot_screen.set_visibility(False)
     desktop_screen.set_visibility(True)

ui.timer(1.5, finish_boot,once=True)


ui.run()
