dictionary = {"Belarus": ["Brest, Gomel, Grodno, Minsk, Vitebsk, Mogilev, Beloozersk, Novopolotsk"]
            , "Spain": ["Barcelona, madrid, alicante, salou, valencia, denia, Malaga, girona, las palmas, sevilla,"
                        " toledo, granada, Tarragona calafell santa cruz bilbao segovia, Salamanca, Murcia, Cordoba" 
                        "Cadiz, Zaragoza, Pamplopa"]
            , "Italy": ["Rome, Milan, Naples, Turin, Palermo, Genoa, Bologna, Florence"
                        "Bari, Catania, Venice, Verona"
                        "Messina, Padua, Trieste, Taranto, Brescia, Prato, Parma, Modena"
                        "Reggio Calabria, Reggio, Emilia Perugia, Livorno, Ravenna, Cagliari Foggia"
                        "Rimini, Ferrara, Salerno, Sassari, Latina, Monza, Syracuse, Pescara"
                        "Giugliano in Campagna, Bergamo, Forlì, Trento, Vicenza"]}

def human_answer():
    answer = str(input("Do you want to continue"))
    return (answer)
while True:
    country = str(input("Enter the country "))
    if country == "Belarus":
        print(*dictionary["Belarus"])

        if human_answer() == "no":
            break
    elif country == "Spain":
        print(*dictionary["Spain"])
        if human_answer() == "no":
            break
    elif country == "Italy":
        print(*dictionary["Italy"])
        if human_answer() == "no":
            break
