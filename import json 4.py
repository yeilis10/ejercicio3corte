import json

# Aquí está el JSON proporcionado
data = [
    {
        "fase": "Cuartos de final",
        "Resultados": [
            {
                "visitante": "Manchester City",
                "local": "Atlético de Madrid",
                "Resultado": "1-0",
                "tarjetas": {
                    "rojas": {
                        "total": "1",
                        "jugadores": [
                            {"equipo": "Atlético de Madrid", "jugador": "Savic", "minuto": "57"}
                        ]
                    },
                    "amarillas": {
                        "total": "3",
                        "jugadores": [
                            {"equipo": "Atlético de Madrid", "jugador": "Koke", "minuto": "25"},
                            {"equipo": "Atlético de Madrid", "jugador": "Carrasco", "minuto": "63"},
                            {"equipo": "Manchester City", "jugador": "Rodri", "minuto": "49"}
                        ]
                    }
                }
            },
            {
                "visitante": "Liverpool",
                "local": "Benfica",
                "Resultado": "3-1",
                "tarjetas": {
                    "rojas": {"total": "0", "jugadores": []},
                    "amarillas": {
                        "total": "4",
                        "jugadores": [
                            {"equipo": "Benfica", "jugador": "Grimaldo", "minuto": "30"},
                            {"equipo": "Benfica", "jugador": "Weigl", "minuto": "56"},
                            {"equipo": "Liverpool", "jugador": "Fabinho", "minuto": "42"},
                            {"equipo": "Liverpool", "jugador": "Konaté", "minuto": "66"}
                        ]
                    }
                }
            },
            {
                "visitante": "Chelsea",
                "local": "Real Madrid",
                "Resultado": "1-3",
                "tarjetas": {
                    "rojas": {"total": "0", "jugadores": []},
                    "amarillas": {
                        "total": "2",
                        "jugadores": [
                            {"equipo": "Chelsea", "jugador": "Jorginho", "minuto": "39"},
                            {"equipo": "Real Madrid", "jugador": "Casemiro", "minuto": "58"}
                        ]
                    }
                }
            },
            {
                "visitante": "Bayern Munich",
                "local": "Villarreal",
                "Resultado": "1-1",
                "tarjetas": {
                    "rojas": {"total": "0", "jugadores": []},
                    "amarillas": {
                        "total": "5",
                        "jugadores": [
                            {"equipo": "Villarreal", "jugador": "Pau Torres", "minuto": "20"},
                            {"equipo": "Villarreal", "jugador": "Albiol", "minuto": "48"},
                            {"equipo": "Bayern Munich", "jugador": "Kimmich", "minuto": "33"},
                            {"equipo": "Bayern Munich", "jugador": "Müller", "minuto": "60"},
                            {"equipo": "Villarreal", "jugador": "Trigueros", "minuto": "73"}
                        ]
                    }
                }
            }
        ]
    }
]

# Función para extraer el resultado, las tarjetas y el equipo ganador
def extract_tarjetas_y_ganador(data):
    for fase in data:
        print(f"Fase: {fase['fase']}")
        for resultado in fase["Resultados"]:
            visitante = resultado["visitante"]
            local = resultado["local"]
            resultado_partido = resultado["Resultado"]
            tarjetas_rojas = resultado["tarjetas"]["rojas"]
            tarjetas_amarillas = resultado["tarjetas"]["amarillas"]
            
            # Mostrar el resultado del partido y el total de tarjetas
            print(f"\nPartido: {local} vs {visitante}")
            print(f"Resultado final: {resultado_partido}")
            print(f"Total tarjetas rojas: {tarjetas_rojas['total']}")
            print(f"Total tarjetas amarillas: {tarjetas_amarillas['total']}")

            # Mostrar quién recibió tarjetas rojas
            if tarjetas_rojas["jugadores"]:
                for jugador in tarjetas_rojas["jugadores"]:
                    print(f"  - {jugador['jugador']} ({jugador['equipo']}) recibió roja en el minuto {jugador['minuto']}")
            else:
                print("  No hubo tarjetas rojas")

            # Mostrar quién recibió tarjetas amarillas
            if tarjetas_amarillas["jugadores"]:
                for jugador in tarjetas_amarillas["jugadores"]:
                    print(f"  - {jugador['jugador']} ({jugador['equipo']}) recibió amarilla en el minuto {jugador['minuto']}")
            else:
                print("  No hubo tarjetas amarillas")

            # Determinar al ganador
            if resultado_partido[0] > resultado_partido[2]:
                ganador = local
            else:
                ganador = visitante

            # Mostrar el equipo ganador
            print(f"Equipo ganador: {ganador}")

# Llamar a la función para extraer los datos del JSON
extract_tarjetas_y_ganador(data)
