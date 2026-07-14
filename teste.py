from services.apostas_service import registrar_aposta
from main.aposta import Aposta



aposta = Aposta(
    id_jogo=1,
    valor_aposta=50,
    multiplicar_aposta=2.0
)


resultado = registrar_aposta(aposta, "mhmm")
print(resultado)