while True:
    try:
        stundenlohn = float(input("Geben Sie Ihren Stundenlohn ein: "))
        if stundenlohn <= 0:
            print("Fehler: Stundenlohn muss positiv sein. Versuchen Sie es erneut.")
            continue
        break
    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben.")
    


taglohn = stundenlohn * 8
monatslohn = taglohn * 20  
jahreslohn = monatslohn * 12  


print("Tägliches Einkommen: " + str(taglohn) + " €")
print("Monatliches Einkommen: " + str(monatslohn) + " €")
print("Jährliches Einkommen: " + str(jahreslohn) + " €")
        
