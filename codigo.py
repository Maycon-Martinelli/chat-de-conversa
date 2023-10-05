# DEVCHAT
# Botão de inicar chat
# Popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensahem que você entrou no chat;
    # o campo e o botão de enviar mensagem;
# a cada mensagem que você envia: (aparece para todo mundo)
    # Nome: Texto da mensagem;
 
import flet as ft

def main(pagina):
    texto = ft.Text("DEVCHAT")

    nome_usuario = ft.TextField()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao DEVCHAT"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar")],
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)


    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)