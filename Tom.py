
import speech_recognition as sr 
import pyttsx3 
import random
import webbrowser
import time                                                                         
import os

soru = input("Merhaba Sarp bugün ne konuşmak istersin ?")

if soru == "Nasılsın ?" or soru == "Bugün nasılsın ?" or soru == "Bugün Nasılsın ?" or soru == "nasılsın ?" or soru == "bugün nasılsın ?":
    print("İyiyim")
    time.sleep(1)
    a = input("Sen bugün nasılsın ?")
    if a == "Ben de iyiyim" or a == "İyiyim" or a == "iyiyim" or a == "iyi" or a == "İyi" or a == "Ben de" or a == "ben de" or a == "Güzel" or a == "güzel":
        print("Oooooo güzeeeellll")
    elif a == "Kötüyüm" or a == "Kötü" or a == "kötü" or "kötüyüm":
        print("Neden ? Nasıl yardımcı olabilirim?")
    else:
        print("Anlamadım , tekrardan dener misin ?")




if soru == "Halimizle hatrımızla ilgili" or soru == "Günümüzün nasıl geçtiğiyle ilgili":
    b = input("Pekala, o zaman ben iyiyim, senin günün nasıl geçti, nasılsın iyi misin ?")
    if b == "Ben de iyiyim"or b == "İyiyim" or b == "iyiyim" or b == "iyi" or b == "İyi" or b == "Ben de" or b == "ben de" or b == "Güzel" or b == "güzel":
        print("O zaman çok iyi")
    elif b == "Kötüyüm":
        print("Neden ? Nasıl yardımcı olabilirim?")
    else:
        print("Anlamadım , tekrardan dener misin ?")




if soru == "Bilmem" or soru == "Bilmem ki" or soru == "Bilmiyorum" or soru == "Bilmiyorum ki" or soru == "bilmem" or soru == "bilmem ki" or soru == "bilmiyorum" or soru == "bilmiyorum ki":
    c = random.choice(["piano","satranç"])
    if c == "piano":
        d = input("Peki o zaman piano ile ilgili bir şey konuşmaya ne dersin ?")
        if d == "Tamam" or d == "Olur" or d == "Ok" or d == "Evet" or d == "tamam" or d == "olur" or d == "ok" or d == "evet" or d == "OK":
            g = input("O zaman pianonun markası ne biliyor musun ?")
        if d == "Yok" or d == "yok" or d == "olmaz" or d == "Olmaz" or "Hayır" or "hayır":
            f = input("Peki o zaman satranç ile ilgili konuşmaya ne dersin ?")
            if f == "Tamam" or f == "Olur" or f == "Ok" or f == "Evet" or f == "tamam" or f == "olur" or f == "ok" or f == "evet" or f == "OK":
                h = input("O zaman bana satrançta ilk hamle olarak beyazlarla en çok oynanan hamleyi söyle")
    if c == "satranç":
        time.sleep(0,5)
        e = input("Peki o zaman satranç ile ilgili konuşmaya ne dersin ?")
        if e == "Tamam" or e == "Olur" or e == "Ok" or e == "Evet" or e == "tamam" or e == "olur" or e == "ok" or e == "evet" or e == "OK":
            i = input("O zaman bana satrançta ilk hamle olarak beyazlarla en çok oynanan hamleyi söyle")
        if e == "Yok" or e == "yok" or e == "olmaz" or e == "Olmaz" or e == "Hayır" or e == "hayır":
            d = input("Peki o zaman piano ile ilgili bir şey konuşmaya ne dersin ?")
        if d == "Tamam" or d == "Olur" or d == "Ok" or d == "Evet" or d == "tamam" or d == "olur" or d == "ok" or d == "evet" or d == "OK":
            j = input("O zaman pianonun markası ne biliyor musun ?")

else:
    print("Konuşma bitti.")




    





