import sys
import nltk
 # Funzione per leggere i file 
def getraw(file):
    f = open(file, mode="r", encoding="utf-8")
    raw = f.read()
    return raw
 # Funzione con sent tokenzer per il testo
def numerosent(sent_tokenizer, raw):
    sent =sent_tokenizer.tokenize(raw)
    return sent
 # Funzione calcolo token
def calctoken(sent):
    corpus = []
    for s in sent:
        tokens = nltk.word_tokenize(s)
        corpus += tokens
    
    return corpus
 # Funzione calcolo carrteri
def calchar(corpus):
    numc =0
    for token in corpus:
        numc+=len(token)
        
    return numc
# Funzione calcolo ttr
def ttr (corpus, dimx=5000):
    token5000 = corpus[0:dimx]
    lungvocabolario = len(set(token5000))
    TTR = (lungvocabolario*1.0)/(dimx*1.0)
    return TTR
# Funzione calcolo classi di frquenza
def FreqInc(tokens):
    for i in range(0, len(tokens), 500):
        listaToken500 = tokens[0:i+500]
        vocabolario500 = list(set(listaToken500))
        V1 =[]
        V5 =[]
        V10 =[]
        print("Range", i, "-", len(listaToken500))
        for tok in vocabolario500:
            conteggio = listaToken500.count(tok)
            if conteggio == 1:
                V1.append(tok)
            if conteggio == 5:
                V5.append(tok)
            if conteggio == 10:
                V10.append(tok)
        print("Classe V1: -", len(V1))
        print("Classe V5: -", len(V5))
        print("Classe V10: -", len(V10))
        print("\n")
 # Funzione calcolo Pos
def numeropos(corpuspos,posx):
    x =0
    for(token,pos) in corpuspos:
     if pos in posx:
        x =x+1
    return x

 # Funzione principale 
def main (file1,file2):
    print("***********************************************************")
    sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    raw1 = getraw(file1)
    raw2 = getraw(file2)
    sent1 = numerosent(sent_tokenizer,raw1)
    sent2 = numerosent(sent_tokenizer,raw2)

    # Numero delle frasi
    numsent1 =len(sent1)
    numsent2 =len(sent2)
    print("NUMERO DELLE FRASI \n")
    print ("Il un numero di frasi nel" ,file1 ,"è", numsent1)
    print ("Il un numero di frasi nel" ,file2 ,"è", numsent2)
    if(numsent1 > numsent2):
        print("Il",file1,"ha il numero di frasi è maggiore",file2,"\n")
    elif(numsent1 < numsent2):
         print("Il",file2,"ha il numero di frasi è minore",file1,"\n")
    else:
        print("I due file hanno lo stesso nuemro di frasi \n")

    # Numero dei tokens
    corpus1 = calctoken(sent1)
    corpus2 = calctoken(sent2)
    lencorpus1 = len(corpus1)
    lencorpus2 = len(corpus2)
    print("NUMERO DEI TOKEN \n")
    print ("Il numero di Token nel" ,file1 ,"è",lencorpus1)
    print ("Il numero di Token nel" ,file2 ,"è",lencorpus2)
    if(lencorpus1 > lencorpus2):
        print("Il",file1,"ha più Token di",file2,"\n")
    elif(lencorpus1 < lencorpus2):
         print("Il",file2,"ha più Token di",file1,"\n")
    else:
        print("I due file hanno lo stesso nuemro di Token \n")
    #la lunghezza media delle frasi in termini di token
    lenmediafrasi1 = (lencorpus1 *1.0)/(numsent1*1.0)   
    lenmediafrasi2 = (lencorpus2 *1.0)/(numsent2*1.0)
    print("LUNGHEZZA MEDIA DELLE FRASI IN TERMINI DI TOKEN \n")
    print ("La lunghezza media delle frasi nel" ,file1 ,"è", lenmediafrasi1)
    print ("La lunghezza media delle frasi nel" ,file2 ,"è", lenmediafrasi2)
    if(lenmediafrasi1 > lenmediafrasi2):
        print("Il",file1,"ha la lunghezza media delle frasi maggiore di",file2,"\n")
    elif(lenmediafrasi1 < lenmediafrasi2):
         print("Il",file1,"ha la lunghezza media delle frasi minore di",file2,"\n")
    else:
        print("I due file hanno lo stessa lunghezza media delle frasi \n")
    #numero medio di caratteri
    numchar1 = calchar(corpus1) 
    numchar2 = calchar(corpus2)
    #la lunghezza media delle frasi in termini di caratteri
    lungmediaparole1 = (numchar1*1.0)/(lencorpus1*1.0) 
    lungmediaparole2 = (numchar2*1.0)/(lencorpus2*1.0)
    print("LUNGHEZZA MEDIA DELLE FRASI IN TERMINI DI CARATTERE\n")
    print("La lunghezza media delle frasi in termini di caratteri del",file1 ,"è ",lungmediaparole1)
    print("La lunghezza media delle frasi in termini di caratteri del",file2 ,"è ",lungmediaparole2)
    if(lungmediaparole1 > lungmediaparole2):
        print("Il",file1,"ha la lunghezza media delle frasi in termini di carratere maggiore di",file2,"\n")
    elif(lungmediaparole1 < lungmediaparole2):
         print("Il",file1,"ha la lunghezza media delle frasi in termini di carratere minore di",file2,"\n")
    else:
        print("I due file hanno lo stessa lunghezza media delle frasi in termini di carratere \n")
# la grandezza del vocabolario e la ricchezza lessicale calcolata attraverso la Type Token Ratio (TTR),in entrambi i casi calcolati nei primi 5000 token;
    print("GRANDEZZA VOCABOLARIO \n")
    voc1 = list(set(corpus1))
    voc2 = list(set(corpus2))
    lenvoc1 = len(voc1)  
    lenvoc2 = len(voc2) 
    print("La grandezza del vocabolario del",file1,"è",lenvoc1)
    print("La grandezza del vocabolario del",file2,"è",lenvoc2,)
    if(lenvoc1 > lenvoc2):
        print("Il",file1,"ha la grandezza del vocabolario maggiore di",file2,"\n")
    elif(lenvoc1 < lenvoc2):
         print("Il",file1,"ha la la grandezza del vocabolario maggiore minore di",file2,"\n")
    else:
        print("I due file hanno lo stessa grandezza del vocabolario \n")

    # TTR = C/V
    print("TYPE TOKEN RATIO CACOLATA NEI PRIMI 5000 TOKEN \n")
    ttr1 = ttr(corpus1)
    ttr2 = ttr(corpus2)
    print("La TTR (Type Token Ratio) nel",file1,"è",ttr1)
    print("La TTR (Type Token Ratio) nel",file2,"è",ttr2,)
    if(ttr1 > ttr2):
        print("Il",file1,"ha la TTR maggiore",file2,"\n")
    elif(ttr1 < ttr2):
         print("Il",file1,"ha la TTR minore",file2,"\n")
    else:
        print("I due file hanno la stessa nuemro TTR \n")
    #Classi di frequenza
    print("ClASSI DI FREQUENZA |V1|, |V5| e |V10| AL AUMENTARE DI 500 TOKEN","\n")
    print("La distribuzione delle classi di frequenza |V1|, |V5| e |V10| all'aumentare del Corpus1 perporzioni incrementali di 500 token""\n")    #sentire miche come stamparlo 
    FreqInc(corpus1)
    print("La distribuzione delle classi di frequenza |V1|, |V5| e |V10| all'aumentare del Corpus2 perporzioni incrementali di 500 token""\n")
    FreqInc(corpus2)
    #nltk per i tag pos
    corpuspos1 = nltk.pos_tag(corpus1)
    corpuspos2 = nltk.pos_tag(corpus2)
    #lista che mi serve 
    sostantivipos = ["NN", "NNS", "NNP", "NNPS"]
    verbipos = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ","MD"]
    avverbipos = ["RB", "RBR", "RBS","WRB"]
    aggettivipos = ["JJ", "JJR", "JJS"]
    punteggiaturapos = [".", ","] #Non so se aggiungere altri segni di punt o lasciare come nella formula?
    #eseguo la funzione e prendo la lisa che mi serve  
    numsostantivi1 = numeropos(corpuspos1,sostantivipos)
    numeroverbi1 = numeropos(corpuspos1,verbipos)
    numeroavverbi1 = numeropos(corpuspos1,avverbipos)
    nuemroaggetivi1 = numeropos(corpuspos1,aggettivipos)
    numsostantivi2 = numeropos(corpuspos2,sostantivipos)
    numeroverbi2 = numeropos(corpuspos2,verbipos)
    numeroavverbi2 = numeropos(corpuspos2,avverbipos)
    nuemroaggetivi2 = numeropos(corpuspos2,aggettivipos)
    numpunteggiatura1 = numeropos(corpuspos1,punteggiaturapos)
    numpunteggiatura2 = numeropos(corpuspos2,punteggiaturapos)
    #Media di sostantivi, verbi,avverbi,aggetivi,per frase nel file1
    mediasostantivi1 = (numsostantivi1*1.0)/(numsent1*1.0)
    mediasostantivi2 = (numsostantivi2*1.0)/(numsent2*1.0)
    mediaverbi1 = (numeroverbi1*1.0)/(numsent1*1.0)
    mediaverbi2 = (numeroverbi2*1.0)/(numsent2*1.0)
    print("NUMERO MEDIO DI SOSTANTIVI E VERBI","\n")
    print("Media dei sostantivi del", file1,"è", mediasostantivi1)
    print("Media dei sostantivi del", file2,"è", mediasostantivi2)
    if(mediasostantivi1 > mediasostantivi1):
        print("Il",file1,"ha la media sostantivi maggiore",file2,"\n")
    elif(mediasostantivi1 < mediasostantivi2):
         print("Il",file1,"ha la media dei sostantivi minore",file2,"\n")
    else:
        print("I due file hanno la stessa media \n")
    print("Media dei verbi del", file1,"è", mediaverbi1)
    print("Media dei verbi del", file2,"è", mediaverbi2,"\n")
    if(mediaverbi1 > mediaverbi2):
        print("Il",file1,"ha la media verbi maggiore",file2,"\n")
    elif( mediaverbi1 < mediaverbi2):
         print("Il",file1,"ha la media dei verbi minore",file2,"\n")
    else:
        print("I due file hanno la stessa media \n")
    #il numero totale di parole nel testo ad esclusione dei segni di punteggiatura marcati
    print("DENSITA LESSICALE","\n")
    densitalessicale1 = (numsostantivi1+ numeroverbi1+ numeroavverbi1+ nuemroaggetivi1)*1.0/( lencorpus1- numpunteggiatura1)*1.0
    densitalessicale2 = (numsostantivi2+ numeroverbi2+ numeroavverbi2+ nuemroaggetivi2)*1.0/( lencorpus2- numpunteggiatura2)*1.0
    print("La densita lessicale del testo1",file1,"è",densitalessicale1)
    print("La densita lessicale del testo2",file2,"è",densitalessicale2)
    if(densitalessicale1 > densitalessicale2):
        print("Il",file1,"ha la densita lessicale maggiore",file2,)
    elif( densitalessicale1 < densitalessicale2):
         print("Il",file1,"ha la densita lessicale minore",file2,)
    else:
        print("I due file hanno la stessa densita lessicale")
    
    print("***********************************************************")
    
main(sys.argv[1], sys.argv[2])
