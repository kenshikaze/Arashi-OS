from datetime import datetime
from nicegui import ui, app
ui.query('body').classes('m-0')
app.add_static_files('/assets', 'assets')

ui.add_head_html('''
<style>
html, body {margin:0; padding:0; width: 100%; height: 100%;}
</style>
<script src="/assets/clock.js">
</script>
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
     with ui.card().classes('fixed bottom-16 left-4 w-72 max-h-[70vh] overflow-y-auto bg-slate-900 text-white')as panel:
          ui.label('Arashi-OS').classes('text-xl font-bold')
          ui.label('''This is my first project and i ain't that much practiced now, so i have only built the loading screen and this desktop screen.\n
          The rest of the OS is still not developed :(
            \n
          Rest of the things are coming later,for now i am shipping what i have built:D''')
          ui.label("Thanks for Checking it out!!")
          ui.separator()
          ui.label('Made by Kaze_97').classes('italic text-gray-400 text-sm')

          panel.set_visibility(False)

     with ui.element('div').classes("fixed bottom-0 left-0 flex items-centre justify-between px-4 bg-black/80 w-full h-14") as taskbar:
          with ui.button(on_click=lambda:panel.set_visibility(not panel.visible)).props('flat round').classes("w-12 h-12 p-0"):
               ui.image('/assets/logo.jpeg').classes('w-8 h-8')
          clock_label= ui.label('--:--:--').props('id=local-clock').classes("text-white text-lg")


#def clock_update():{REMOVED AS IT USE SINGLE TIMEZONE OF PYTHIN SERVER}
#     time = datetime.now().strftime("%H:%M:%S")
#    clock_label.set_text(time)
#ui.timer(1, clock_update)

desktop_screen.set_visibility(False)

def finish_boot():
     boot_screen.set_visibility(False)
     desktop_screen.set_visibility(True)

ui.timer(1.5, finish_boot,once=True)


ui.run()