import flet as ft
import string
import random

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0 
    page.window.title_bar_hidden= False
    page.window.width=400
    page.window.min_width=400
    page.window.max_width=400
    page.window.height=700
    page.window.min_height=700
    page.window.max_height=700
    


    page.theme = ft.Theme(        
        color_scheme= ft.ColorScheme(
            primary="#192233",
            on_primary="#ffffff",
            on_background="#0d121c",
        )       
    )
    options= {}
    generate_button = ft.Ref[ft.Container]()
    txt_password = ft.Ref[ft.Text]()
    characters_count=ft.Ref[ft.Slider]()
    btn_clipboard=ft.Ref[ft.IconButton]()

    def copy_to_clipboard(e):
        pwd = txt_password.current.value
        if pwd:
            page.set_clipboard(pwd)
            btn_clipboard.current.selected= True
            btn_clipboard.current.update()

    def generate_password(e):
        pwd = ""
        if options.get("uppercase"):
            pwd+= string.ascii_uppercase

        if options.get("lowercase"):
            pwd+= string.ascii_lowercase

        if options.get("digits"):
            pwd+= string.digits

        if options.get("uppercase"):
            pwd+= string.ascii_uppercase

        if options.get("punctuation"):
            pwd+= string.punctuation

        count=int(characters_count.current.value)
        password=random.choices(pwd, k=count)
        txt_password.current.value= "".join(password)
        txt_password.current.update()
        btn_clipboard.current.selected= False
        btn_clipboard.current.update()
        

    def toggle_option(e):
        nonlocal options
        options[e.control.data] = e.control.value
        if any(options.values()):
            generate_button.current.disabled= False
            generate_button.current.opacity = 1
        else:
            generate_button.current.disabled= True
            generate_button.current.opacity= 0.3

        generate_button.current.update()

        

    layout = ft.Container(        
        padding=ft.Padding(top=60,right=10, left=10, bottom=10),
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1.0, -1.0),
            end=ft.Alignment(-1.0, 1.0),
            colors=[ft.Colors.PRIMARY, ft.Colors.BLACK]
        ),
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text(
                    value="GERADOR DE SENHAS",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    text_align= ft.TextAlign.CENTER,
                ), 
                ft.Divider(height=30, thickness=0.6),
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),  
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    padding=ft.Padding(
                        left=7,
                        top=7,
                        right=7,
                        bottom=7
                    ),                                   
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,                        
                        controls=[
                            ft.Text(
                                ref=txt_password,
                                selectable=True,
                                size=20,
                                height=40,
                            ),
                            ft.IconButton(
                                ref=btn_clipboard,
                                icon=ft.Icons.COPY,
                                icon_color=ft.Colors.WHITE38,
                                selected_icon=ft.Icons.CHECK,
                                selected_icon_color=ft.Colors.INDIGO,
                                selected=False,
                                on_click=copy_to_clipboard
                            )
                        ]
                    )
                ),
                ft.Text(
                    value="QUANT CARACTERES",
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),  
                    border_radius=ft.BorderRadius(10, 10, 10, 10),                    
                    content=ft.Slider(
                        ref=characters_count,
                        value=8,
                        min=6,
                        max=20,
                        divisions=14,
                        label="{value}"
                    )                
                ),
                ft.Text(
                    value="PREFERÊNCIAS",                    
                    weight=ft.FontWeight.BOLD,
                    text_align= ft.TextAlign.CENTER,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value="Letras Maiúsculas",
                        size=20,                        
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.Colors.INDIGO,
                        data="uppercase",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value="Letras Minúsculas",
                        size=20,                        
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.Colors.INDIGO,
                        data="lowercase",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value="Incluir números",
                        size=20,                        
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.Colors.INDIGO,
                        data="digits",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.ListTile(
                    title=ft.Text(
                        value="Incluir Símbolos",
                        size=20,                        
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.Colors.INDIGO,
                        data="punctuation",
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),
                ft.Container(
                    ref=generate_button,
                    gradient=ft.LinearGradient(
                        colors=[ft.Colors.INDIGO_900, ft.Colors.INDIGO_500]
                    ),
                    alignment=ft.Alignment(0.0, 0.0),
                    padding=ft.Padding(top=10, left=10, right=10, bottom=10),
                    border_radius=ft.BorderRadius(10, 10, 10, 10), 
                    content=ft.Text(
                        value="GERAR SENHA",
                        weight=ft.FontWeight.BOLD,

                    ),
                    on_click=generate_password,
                    disabled=True,
                    opacity=0.3,
                    animate_opacity=ft.Animation(duration=700, curve=ft.AnimationCurve.DECELERATE),

                )
            ]
        )
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)