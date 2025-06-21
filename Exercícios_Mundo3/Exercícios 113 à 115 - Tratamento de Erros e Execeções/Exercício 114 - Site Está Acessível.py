#Crie um código em Python que teste se o site Pudim (pudim.com.br) está acessível pelo computador usado.

from requests import get
import emoji

def ver_conexao(url):
    try:
        teste= get(url)
    except:
        print(f"=" * 30 + f"\n\033[31mO site de endereço '{url}' está indisponível no momento.\033[m")
    else:
        print(f"=" * 30 + f"\n\033[32mO site de endereço '{url}' está disponível e pode ser acessado.\033[m")
    finally:
        print(f"=" * 30 + f"\n\033[34mVolte Sempre!{emoji.emojize(':smiling_face_with_smiling_eyes:')}\033[m")

site= ver_conexao("https://pudim.com.br")
