import flet as ft
"""
def main(page: ft.Page):
    page.title = "카운터"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_btn_click(e):
        #btn_change.content = '눌렸습니다'
        text_hello.value = '반갑습니다'
        page.update()

    text_hello = ft.Text('안녕하세요')
    btn_change = ft.Button('눌러 주세요', on_click=on_btn_click)
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
                text_hello,
                btn_change,
            ]
        )
    )
    
if __name__ == "__main__":
    ft.run(main)
"""


def main(page: ft.Page):
    page.title= "Neat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    """
    def on_btn_click(e):
        #btn_change.content = "Pressed"
        #e.control.content = "Dick"
        text_counter.value = "Good to see you"
        page.update()


    text_counter = ft.Text("Hello")
    btn_change = ft.Button("Press me!", on_click=on_btn_click)
    """


    text_counter = ft.Text(value = '0', size=100, width=200, text_align=ft.TextAlign.CENTER)
    def on_minus_click(e):
        text_counter.value=str(int(text_counter.value)-1)
    
    def on_plus_click(e):
        text_counter.value=str(int(text_counter.value)+1)
    
    
    page.add(
        ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
            ft.IconButton(ft.Icons.REMOVE, on_click = on_minus_click),
            text_counter,
            ft.IconButton(ft.Icons.ADD, on_click = on_plus_click)
            ]
            )
        )
    

if __name__ == "__main__":
    ft.run(main)