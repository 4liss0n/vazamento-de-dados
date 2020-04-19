vazamento = ["SpongeBob@gmail.com", "PatrickStar@gmail.com", "LulaMolusco@gmail.com", "Sandy@gmail.com", "Plankton@gmail.com", "SrCirigueijo@gmail.com", "CatDog@gmail.com", "MablePynes@gmail.com", "DipperPynes@gmail.com", "BillCypher@gmail.com", "Timmy@gmail.com", "Cosmo@gmail.com", "Wanda@gmail.com", "Bylli@gmail.com", "Mandy@gmail.com", "PuroOsso@gmail.com", "FlapJack@gmail.com", "bolha@gmail.com", "Capitão@gmail.com", "JonathanJoestar@gmail.com", "Dio@gmail.com", "Florzinha@gmail.com", "Lindinha@gmail.com", "Docinho@gmail.com", "Rigby@gmail.com", "Mordecai@gmail.com", "Benson@gmail.com", "Saltitao@gmail.com", "Musculoso@gmail.com", "FantasMao@gmail.com"]
senhas = ["Garry@123", "AquiÉoPatrick", "EuSouUmPolvo", "AdoroNozes", "KarenS2", "$dinheiro$", "CatCat", "familhaemoletons", "segredosdegravityfalls", "oPortãoEntreOsMundosEstaAberto", "CosmoWandaePoff", "LapisVerde", "@poff123", "oAmorMudaAsPessoas", "OdeioOBilly", "MorteaTodos", "aventuras123", "@familia123", "BalasDoces", "ErinaLOVE", "aMascaraeMinha", "desculpa", "mas", "esta", "acabando", "minha", "criatividade", "sao", "muitas", "senhas"]

dados = input("oque voce acha que vazou? ")
 
for x in range (0, len(vazamento)):
    if dados == vazamento[x]:
        print("vazado!")
        print(vazamento[x])
        print(senhas[x])
        
        
