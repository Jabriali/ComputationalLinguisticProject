import sys
import math
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
# Funzione calcolo Pos
def numpos(corpuspos, posx):
    plist = []
    for(token, pos) in corpuspos:
        if pos in posx:
            plist.append(token)
    return plist
# Funzione calcolo bigrammi
def bigra(bigrammi, posx1, posx2):
    blist = []
    for b in bigrammi:
        if b[0][1] in posx1:
            if b[1][1] in posx2:
                blist.append(b)
    return blist
# Funzione calcolo pos frequenti
def posfrequenti(corpus, postocheck):
    p = numpos(corpus, postocheck)
    freqdist = nltk.FreqDist(p)
    frequent10 = freqdist.most_common(20)
    return frequent10
# Funzione ordinamento bigrammi
def postokbigrammi(bigrammi):
    tsx = []
    tdx = []
    for b in bigrammi:
        tsx.append(b[0])
        tdx.append(b[1])
    
    sxpos = nltk.pos_tag(tsx)
    dxpos = nltk.pos_tag(tdx)

    for i in range(0, len(bigrammi)):
        bigrammi[i] = (sxpos[i], dxpos[i])

    return bigrammi
# Funzione catenza markov1
def markov1(sent):
    sentlen = []
    for s in sent:
        tsent = nltk.word_tokenize(s)
        if len(tsent) >=8 and len(tsent) <= 15:
            sentlen.append(s)
    
    corpus = calctoken(sent)
    voc = list(set(corpus))
    freqdist = nltk.FreqDist(corpus)
    bigrammi1 = nltk.bigrams(corpus)
    bigrammifreqdist = nltk.FreqDist(bigrammi1)
    #Qui ho cambiato la struttura ed ho usato la strutttra dizionario come mi ha chiesto il prof.Orletto
    probsent = {
        8 : ("", 0),
        9 : ("", 0),
        10 : ("", 0),
        11 : ("", 0),
        12 : ("", 0),
        13 : ("", 0),
        14 : ("", 0),
        15 : ("", 0),
    }
    
    for s in sentlen:
        tsen = list(nltk.word_tokenize(s))
        bsen = list(nltk.bigrams(tsen))
        prob = (freqdist[tsen[0]] + 1) / (len(corpus) + len(voc))
        for b in bsen:
            freqbigramma = bigrammifreqdist[b] + 1
            freqtoken1 = freqdist[b[0]] + len(voc)
            condprob = freqbigramma * 1.0 / freqtoken1 * 1.0
            prob = prob * condprob
        if prob > probsent[len(tsen)][1]:
            probsent[len(tsen)] = (s, prob)
    return probsent
# Funzione per le entita 
def entitynominate(corpus):
    pos = nltk.pos_tag(corpus)
    entnominate = nltk.ne_chunk(pos)
    pers = []
    luoghi = []
    for nodo in entnominate:
        NE = ''
        if hasattr(nodo, 'label'):
            if nodo.label() in ["PERSON", "GPE"]:
                for tiponodo in nodo.leaves():
                    NE = NE + ' ' + tiponodo[0]
                if nodo.label() == "PERSON":
                    pers.append(NE)
                else:
                    luoghi.append(NE)
                                
    return pers, luoghi
 # Funzione principale 
def main (file1,file2):
    print("***********************************************************")
    sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    raw1 = getraw(file1)
    raw2 = getraw(file2)
    # Numero delle frasi
    sent1 = numerosent(sent_tokenizer,raw1)
    sent2 = numerosent(sent_tokenizer,raw2)
    # Numero dei tokens
    corpus1 = calctoken(sent1)
    corpus2 = calctoken(sent2)
    # eseguo il post tag
    corpuspos1 =nltk.pos_tag(corpus1)
    corpuspos2 =nltk.pos_tag(corpus2)
    sostantivipos =["NN", "NNS", "NNP", "NNPS"]
    verbipos =["VB", "VBD", "VBG", "VBN", "VBP", "VBZ","MD"]
    avverbipos =["RB", "RBR", "RBS","WRB"]
    aggettivipos =["JJ", "JJR", "JJS"]
    punteggiaturapos =[".", ","]
    #Estrazione dei 10 post piu frequenti nel primo testo e li metto nella mia lista 
    POSlist = []
    for p in corpuspos1:
        POSlist.append(p[1])
    freqdistpos1 = nltk.FreqDist(POSlist)
    frequent10pos1 = freqdistpos1.most_common(10)
    #Estrazione dei 10 post piu frequenti nel secondo testo  e li metto nella mia lista
    POSlist = []
    for p in corpuspos2:
        POSlist.append(p[1])
    freqdistpos2 = nltk.FreqDist(POSlist)
    frequent10pos2 = freqdistpos2.most_common(10)
     # stampare le frequenze pos
    print("LE 10 POS (PART-OF-SPEECH) PIÙ FREQUENTI \n")
    print("La lista dei 10 PoS più frequenti nel primo testo ",file1)
    for e in frequent10pos1:
        print("POS",e[0],"con frquenza", e[1])
    
    print("\t")    
    print("La lista dei 10 PoS più frequenti nel secondo testo ",file2)
    for e in frequent10pos2:
        print("POS",e[0],"con frquenza", e[1])
    
    print("\t") 
    print("I 20 SOSTANTIVI E I 20 VERBI PIÙ FREQUENTI \n")
    print("La lista dei sostantivi nel primo testo ",file1)
    frequent10sos1 = posfrequenti(corpuspos1, sostantivipos)
    #Estrazione dei 20 sostantivi piu frequenti nel primo testo e li stampo
    for t in frequent10sos1: 
        print("Il sostantivo","[",t[0],"]","con frequenza", t[1],)
    
    print("\t")
    print("La lista dei sostantivi nel secondo testo",file2)
    frequent10sos2 = posfrequenti(corpuspos2, sostantivipos)
    #Estrazione dei 20 sostantivi piu frequenti nel secondo testo e li stampo
    for t in frequent10sos2: 
         print("Il sostantivo","[",t[0],"]","con frequenza", t[1])
    
    print("\t")
    print("La lista dei verbi nel primo testo ",file1)
    frequent10verb1 = posfrequenti(corpuspos1, verbipos)
    #Estrazione dei 20 verbi piu frequenti nel primo testo e li stampo
    for t in frequent10verb1: 
        print("Il verbo","[",t[0],"]","con frequenza", t[1])
    
    print("\t")
    print("La lista dei verbi nel secondo testo ",file2)
    frequent10verb2 = posfrequenti(corpuspos2, verbipos)
    #Estrazione dei 20 verbi piu frequenti nel secondo testo e li stampo
    for t in frequent10verb2: 
        print("Il verbo","[",t[0],"]","con frequenza", t[1])
    
    print("\t")
    print("I 20 BIGRAMMI COPOSTI DA UN SOSTANTIVO SEGUITO DA UN VERBO PIÙ FREQUENTI")
    print("\t") 
    bigrammi1 = list(nltk.bigrams(corpus1))
    bigrammitagged1 = postokbigrammi(bigrammi1)
    #i 20 bigrammi composti da un Sostantivo seguito da un Verbo più frequenti e chiamo la funzione bigra;
    blist1 = bigra(bigrammitagged1, sostantivipos, verbipos)
    mostfrequentb1 = nltk.FreqDist(blist1).most_common(20)
    print("La lista dei 20 bigrammi composti da un sostantivo seguito da un verbo più frequenti primo testo",file1)
    #Estrazione dei 20 bigramm composti da sostantivi seguiti da verboi piu frequenti nel primo testo e li stampo
    for (b, f) in mostfrequentb1:
        print("Il bigramma","(",b[0][0],",",b[1][0],")","con frequenza", f)
    
    print("\t")
    bigrammi2 = list(nltk.bigrams(corpus2))
    bigrammitagged2 = postokbigrammi(bigrammi2)
    #i 20 bigrammi composti da un Sostantivo seguito da un Verbo più frequenti e chiamo la funzione bigra;
    blist2 = bigra(bigrammitagged2, sostantivipos, verbipos)
    mostfrequentb2 = nltk.FreqDist(blist2).most_common(20)
    print("La lista dei 20 bigrammi composti da un sostantivo seguito da un verbo più frequenti secondo testo",file2)
    #Estrazione dei 20 bigramm composti da sostantivi seguiti da verboi piu frequenti nel secondo testo e li stampo
    for (b, f) in mostfrequentb2:
       print("Il bigramma","(",b[0][0], ",",b[1][0],")", "con frequenza", f)

    print("\t")
    print("I 20 BIGRAMMI COPOSTI DA UN AGGETIVO SEGUITO DA UN SOSTANTIVO PIÙ FREQUENTI\n")
    bigrammi1 = list(nltk.bigrams(corpus1))
    bigrammitagged1 = postokbigrammi(bigrammi1)
    #i 20 bigrammi composti da un aggetivo seguito da un sotantivo più frequenti e chiamo la funzione bigra;
    blist1 = bigra(bigrammitagged1, aggettivipos, sostantivipos)
    mostfrequentb1 = nltk.FreqDist(blist1).most_common(20)
    print("La lista dei 20 bigrammi composti da un aggetivo seguito da un sostantivo più frequenti primo testo",file1)
    #Estrazione dei 20 bigramm composti da aggetivo seguiti da un sostantivo piu frequenti nel primo testo e li stampo
    for (b, f) in mostfrequentb1:
        print("Il bigramma","(",b[0][0], ",",b[1][0],")","con frequenza", f)
    
    print("\t")
    bigrammi2 = list(nltk.bigrams(corpus2))
    bigrammitagged2 = postokbigrammi(bigrammi2)
    #i 20 bigrammi composti da un aggetivo seguito da un sotantivo più frequenti e chiamo la funzione bigra;
    blist2 = bigra(bigrammitagged2, aggettivipos, sostantivipos)
    mostfrequentb2 = nltk.FreqDist(blist2).most_common(20)
    print("La lista dei 20 bigrammi composti da un aggetivo seguito da un sostantivo più frequenti secondo testo",file2)
    #Estrazione dei 20 bigramm composti da aggetivo seguiti da un sostantivo piu frequenti nel secondo testo e li stampo
    for (b, f) in mostfrequentb2:
       print("Il bigramma","(",b[0][0], ",",b[1][0],")","con frequenza", f)
    
    print("\t")
    print("I 20 BIGRAMMI CON FREQUENZA MAGGIORE DI 3 CON PROBABILITÀ CONGIUNTA MAX, CONDIZIONATA MAX E LMI\n")
    #probabilità congiunta massima, indicando anche la relativa probabilità
    #creo la lista 
    bigrammifmin1 = []
    #eseguo funzione bigrams
    bigrammi1 = list(nltk.bigrams(corpus1))
    #eseguo funzione freqDist
    bigrammifdist1 = nltk.FreqDist(bigrammi1)
    #faccio il ciclo for e faccio un controllo con il if e prendo quelli maggiori di 3 
    for b in bigrammi1:
        if bigrammifdist1[b] > 3:
            bigrammifmin1.append(b)

    corpusdist1 = nltk.FreqDist(corpus1)
    bigrammidistf1 = nltk.FreqDist(bigrammifmin1)
    #creo altre 3 liste  
    bigrammipcong = []
    bigrammipcond = []
    bigrammiLMI = []
    #faccio un altro ciclo for e uso le formule per la probabilita congiunta, condizionata e LMI
    for b in bigrammidistf1:
        pcong = bigrammidistf1[b] * 1.0/ len(corpus1) * 1.0
        pcond = bigrammidistf1[b] * 1.0 / corpusdist1[b[0]] * 1.0
        MI = math.log2((bigrammidistf1[b] * len(corpus1)) / (corpusdist1[b[0]]  * corpusdist1[b[1]]))
        LMI = bigrammidistf1[b] * MI
        bigrammipcong.append((b, pcong))
        bigrammipcond.append((b, pcond))
        bigrammiLMI.append((b, LMI))
    #ordino la lista di tuple in base al secondo elemento
    bigrammipcong.sort(key = lambda x: x[1], reverse=True)
    bigrammipcond.sort(key = lambda x: x[1], reverse=True)
    bigrammiLMI.sort(key = lambda x: x[1], reverse=True)
    #estrago le prime venti tuple
    bigrammipcong = bigrammipcong[0:20]
    print("Lista dei 20 bigrammi con probabilità congiunta massima nel primo testo",file1)
     #stampo la lista probcongiunta 
    for b in bigrammipcong:
        print("Il bigramma",b[0],"con probabilità",b[1])
    
    print("\t")
    #estrago le prime venti tuple
    bigrammipcond = bigrammipcond[0:20]
    print("Lista dei 20 bigrammi con probabilità condizionata massima nel primo testo",file1)
    #stampo la lista probcondizionata 
    for b in bigrammipcond:
        print("Il bigramma",b[0],"con probabilità",b[1])
    
    print("\t")
    #estrago le prime venti tuple
    bigrammiLMI = bigrammiLMI[0:20]
    print("Lista dei 20 bigrammi con forza associativa (LMI) massima, primo testo",file1)
     #stampo la lista LMI
    for b in bigrammiLMI:
        print("Il bigramma",b[0],"con LMI",b[1])
    
    print("\t")
    #Esguil gli stessi pasaggi per il secndo testo 
    bigrammifmin2 = []
    bigrammi2 = list(nltk.bigrams(corpus2))
    bigrammifdist2 = nltk.FreqDist(bigrammi2)
    for b in bigrammi2:
        if bigrammifdist2[b] > 3:
            bigrammifmin2.append(b)

    corpusdist2 = nltk.FreqDist(corpus2)
    bigrammidistf2 = nltk.FreqDist(bigrammifmin2)
    bigrammipcong = []
    bigrammipcond = []
    bigrammiLMI = []
    for b in bigrammidistf2:
        pcong = bigrammidistf2[b] * 1.0/ len(corpus2) * 1.0
        pcond = bigrammidistf2[b] * 1.0 / corpusdist2[b[0]] * 1.0
        MI = math.log2((bigrammidistf2[b] * len(corpus2)) / (corpusdist2[b[0]]  * corpusdist2[b[1]]))
        LMI = bigrammidistf2[b] * MI
        bigrammipcong.append((b, pcong))
        bigrammipcond.append((b, pcond))
        bigrammiLMI.append((b, LMI))

    bigrammipcong.sort(key = lambda x: x[1], reverse=True)
    bigrammipcond.sort(key = lambda x: x[1], reverse=True)
    bigrammiLMI.sort(key = lambda x: x[1], reverse=True)
    bigrammipcong = bigrammipcong[0:20]
    print("Lista dei 20 bigrammi con probabilità congiunta massima nel secondo testo",file2)
    for b in bigrammipcong:
        print("Il bigramma",b[0],"con probabilità",b[1])
    
    print("\t")
    bigrammipcond = bigrammipcond[0:20]
    print("Lista dei 20 bigrammi con probabilità condizionata massima nel secondo testo",file2)
    for b in bigrammipcond:
        print("Il bigramma",b[0],"con probabilità",b[1])
    
    print("\t")
    bigrammiLMI = bigrammiLMI[0:20]
    print("Lista dei 20 bigrammi con forza associativa (LMI) massima, secondo testo",file2)
    for b in bigrammiLMI:
        print("Il bigramma",b[0],"con LMI",b[1])
    
    print("\t")
    print("LUNGHEZZA DI FRASE DA 8 A 15 TOKEN CON PROBABILITÀ PIÙ ALTA CALCOLATA ATTRAVERSO UN MODELLO DI MARKOV DI ORDINE 1 USANDO LO ADD-ONE SMOOTHING")
    print("\t")
    #uso la funzione per il calcolo di markov 1 sulle frasi primo file
    probsent1 = markov1(sent1)
    #uso il range e caccio la tupla del dizionario  
    #uso il ciclo for per la stampa 
    for i in range(8, 16):
        print("La frase di lunghezza", i, "con probabilità massima del primo testo",file1)
        print("[",probsent1[i][0],"]" ,"con probabilità", probsent1[i][1])
       
    #uso la funzione per il calcolo di markov 1 sulle frasi secondo file  
    probsent2 = markov1(sent2)
    #uso il range e caccio la tupla del dizionario 
    print("\t")
    #uso il ciclo for per la stampa   
    for i in range(8, 16):
        print("La frase di lunghezza", i, "con probabilità massima del secondo testo",file2)
        print("[",probsent2[i][0],"]" ,"con probabilità", probsent2[i][1])
    
    print("\t")
    print("I 15 NOMI PROPRI DI PERSONA E DI LUOGI PIÙ FREQUENTI")
    print("\t")
    #uso la funzione entit sul corpus1
    pers1, luoghi1 = entitynominate(corpus1)
    #estargo i 15 nomi piu frequanti e luoghi 
    persdist1 = nltk.FreqDist(pers1).most_common(15)
    luoghidist1 = nltk.FreqDist(luoghi1).most_common(15)
    print("I nomi di persone piu frquanti nel primo testo",file1)
    #eseguo un ciclo for per entrambi 
    for p in persdist1:
        print("Il nome","[",p[0],"]","con frequenza", p[1])
    
    print("\t")
    for p in luoghidist1:
        print("Il luogo","[",p[0],"]","con frequenza", p[1])
    
    print("\t")
    #uso la funzione entit sul corpus2
    pers2, luoghi2 = entitynominate(corpus2)
    #estargo i 15 nomi piu frequanti e luoghi 
    persdist1 = nltk.FreqDist(pers2).most_common(15)
    luoghidist1 = nltk.FreqDist(luoghi2).most_common(15)
    print("I nomi di persone piu frquanti nel secondo testo",file2)     
    #eseguo un ciclo for per entrambi  
    for p in persdist1:
        print("Il nome","[",p[0],"]","con frequenza", p[1])
    
    print("\t")
    for p in luoghidist1:
        print("Il luogo","[",p[0],"]", "con frequenza", p[1])

    
    print("***********************************************************")
main(sys.argv[1], sys.argv[2])