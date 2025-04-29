def vyhodnot_odpovedi(spravne_odpovedi, odpovedi_uzivatele):
    # Spočítáme počet správně zodpovězených otázek
    spravne_odpovedi_count = sum(1 for spravna, uzivatel in zip(spravne_odpovedi, odpovedi_uzivatele) if spravna == uzivatel)
    
    # Celkový počet otázek
    celkovy_pocet = len(spravne_odpovedi)
    
    # Úspěšnost v procentech
    uspesnost = (spravne_odpovedi_count / celkovy_pocet) * 100
    
    # Výstup s zaokrouhlením úspěšnosti na jedno desetinné místo
    print(f"Uživatel odpověděl správně na {spravne_odpovedi_count} z {celkovy_pocet} otázek. Úspěšnost: {uspesnost:.1f}%.")
    
# Příklad použití:
spravne_odpovedi = ["Praha", "B", "C", "D", "A"]
odpovedi_uzivatele = ["Praha", "B", "C", "A", "A"]
