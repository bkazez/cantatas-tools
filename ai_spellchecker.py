#!/opt/homebrew/bin/python3.9

# import the OpenAI Python library for calling the OpenAI API
from pprint import pprint
import openai

MODEL = "gpt-4" # "gpt-4"
openai.api_key_path = "openai_api_key.txt"

system = """You hold advanced degrees in French, German, Italian, and Latin literature from Princeton. You will be given baroque text, copied from Google Sheets. Output any lines with spelling mistakes and your recommended correction. Use this exact format:
Cao mio ben -> Caro mio ben"""




user = """
Quando avran fine omai
Padre, germani, addio!
Ecco, Idamante, ahimè!
Radunate i Troiani, ite
Non ho colpa
Ecco il misero resto de' Troiani
Scingete le catene
Godiam la pace, trionfi Amore
Prence, signor, tutta la Grecia oltraggi
Tutte nel cor vi sento
Pietà! Numi, pietà!
Pantomime
Eccoci salvi alfìn
Oh voi, di Marte e di Nettuno
Vedrommi intorno l'ombra dolente
Cieli! che veggo?
Spiagge romite, e voi scoscese rupi
Spietatissimi Dei!
Il padre adorato
Marcia [=1.]
Ballo delle donne Cretesi
Nettuno s'onori, quel nome risuoni
Tutto m'è noto
Se il tuo duol
Non più. Tutto ascoltai
Non temer, amato bene
Se mai pomposo apparse
Se il padre perdei
Qual mi conturba i sensi
Fuor del mar [=1.]
Frettolosa e giuliva Elettra vien
Fuor del mar [=2.]
Chi mai del mio provò piacer più dolce?
Idol mio, se ritroso
Odo da lunge armonioso suono
Sidonie sponde!
Placido è il mar, andiamo
Vattene prence
Pria di partir, oh Dio!
Deh cessi il scompiglio
Più
Qual nuovo terrore!
Eccoti in me, barbaro Nume!
Io solo errai
Corriamo, fuggiamo
Solitudini amiche
Zeffìretti lusinghieri
Ei stesso vien ... oh Dei!
Principessa, a' tuoi sguardi
Odo? o sol quel che brama finge l'udito
S'io non moro a questi accenti
Spiegarti non poss'io
Cieli! che vedo?
Andrò ramingo e solo
Sire, alla reggia tua immensa turba
Sventurata Sidon!
Se colà ne' fati è scritto
Volgi intorno lo sguardo, oh sire
Oh voto tremendo!
Marcia [=2.]
Accogli, oh re del mar
Stupenda vittoria!
Qual risuona qui intorno
Sire, il prence
Padre, mio caro padre
Barbaro, iniquo fato
gombra
Deh vibra un colpo
alto voler
Ma che più tardi?
Ilia, t'accheta...
Idomeneo cessi esser re
A Idomeneo perdona
Oh ciel pietoso!
Popoli, a voi l'ultima legge
Scenda Amor, scenda Imeneo
Chaconne
Larghetto
La Chaconne, qui reprend
Largo
Oh voi, di Marte e di Nettuno
Cieli! che veggo? – ah qual dolore
Cieli! che veggo? – Potesi almeno
Siam soli. Odimi Arbace
Se mai pomposo apparse
Frettolosa e giuliva Elettra vien / Sire, da Arbace / Chi mai del mio provò
No, la morte
Padre, mio caro padre
Ha vinto Amore ...
Ha vinto Amore ...
Numi! Oh smania!
D'Oreste, d'Aiace
Torna la pace
Annonce
Popoli, a voi l'ultima legge
Torna la pace
"""

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user},

    ],
    temperature=0.9,
)

print(response['choices'][0]['message']['content'])



