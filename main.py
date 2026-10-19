from datetime import datetime
from nicegui import ui, app
ui.query('body').classes('m-0')
app.add_static_files('/assets', 'assets')

ui.add_head_html('''
<style>
html, body {margin:0; padding:0; width: 100%; height: 100%;}
</style>
''')

with ui.element('div').classes(
    "w-full h-screen flex items-center justify-center bg-slate-950"
) as boot_screen:
        with ui.card().classes("w-100 items-left"):
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
     "w-full h-screen m-0 p-0 text-white " \
     " flex flex-col").style(' background-image: url( "/assets/cherry_blossom.jpg");' \
     ' background-size: cover;' \
     ' background-position: center;' \
     ' background-repeat: no-repeat') as desktop_screen:
     with ui.element('div').classes("fixed bottom-0 left-0 flex items-centre justify-between px-4 bg-black/50 w-full h-14"):
          ui.button("Arashi-OS")
          clock_label= ui.label('00:00:00').classes("text-white text-lg")

def clock_update():
     time = datetime.now().strftime("%H:%M:%S")
     clock_label.set_text(time)

clock_update()
ui.timer(1, clock_update)

desktop_screen.set_visibility(False)

def finish_boot():
     boot_screen.set_visibility(False)
     desktop_screen.set_visibility(True)

ui.timer(1.5, finish_boot,once=True)


ui.run()
