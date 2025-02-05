import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Custom Title", width=600, height=300)

with dpg.window(
    label="Example Window",
    width=600,
    height=300,
    no_move=True,
    no_resize=True,
    no_collapse=True,
    no_close=True,
    no_title_bar=True,
):
    # Add some padding at the top
    dpg.add_spacer(height=20)

    # Center align text
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=200)
        dpg.add_text("Hello, world", color=(255, 255, 0))

    dpg.add_spacer(height=20)

    # Create a group for input elements with consistent width
    with dpg.group(width=400):
        dpg.add_input_text(label="string", default_value="Quick brown fox", width=300)
        dpg.add_spacer(height=10)
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1, width=300)
        dpg.add_spacer(height=20)

        # Center the button
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=150)
            dpg.add_button(label="Save", width=100)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
