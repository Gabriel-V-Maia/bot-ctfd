import requests
import json
import sys, os
import discord

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
from dataclasses import dataclass, field
from helpers import embeds

load_dotenv()

@dataclass
class Tracker:
    URL_API: str
    API_KEY: str
    NTFY_TOPIC: str
    ARQUIVO_ESTADO: str
    DISCORD_CLIENT: discord.Client
    
    def carregar_vistos(self):
        if os.path.exists(self.ARQUIVO_ESTADO):
            with open(self.ARQUIVO_ESTADO, "r") as f:
                return set(json.load(f))
        return set()

    def salvar_vistos(self, ids):
        with open(self.ARQUIVO_ESTADO, "w") as f:
            json.dump(list(ids), f)

    def buscar_desafios(self):
        headers = {"Authorization": f"Token {self.API_KEY}", "Content-Type": "application/json"}
        r = requests.get(self.URL_API, headers=headers)
        return r.json().get("data", [])

    async def checar_novos(self):
        vistos = self.carregar_vistos()
        desafios = self.buscar_desafios()
        novos = [d for d in desafios if str(d["id"]) not in vistos]
        for d in novos:
            mensagem = f"Novo desafio: {d['name']} - {d['category']}"
            requests.post(f"https://ntfy.sh/{self.NTFY_TOPIC}", data=mensagem.encode("utf-8"))
            await embeds.send_embed(self.DISCORD_CLIENT, "Novo desafio!", mensagem, discord.Color.red())
            vistos.add(str(d["id"]))
        self.salvar_vistos(vistos)

        
