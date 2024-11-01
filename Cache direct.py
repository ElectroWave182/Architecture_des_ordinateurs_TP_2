from math import log, log2, ceil

global base
base = 10


class Cache:

    # Paramètres
    tailleCache = 1024
    tailleBloc = 32
    n = int (log2 (tailleCache ** 0.5))

    # Constantes
    nbDeplacements = tailleBloc
    nbLignes = 2 ** n
    nbEtiquettes = 2 ** (tailleCache // nbLignes - 1)
    numDeplacement = 2 ** ceil (log2 (nbDeplacements))
    numLigne = nbLignes * numDeplacement
    numEtiquette = nbEtiquettes * numLigne
    
    # Contenu du cache
    nbChiffres = ceil (log (nbEtiquettes, 10))
    defaut = "0" * nbChiffres
    donnees = [defaut] * nbLignes


    # Fonctions opératives

    def lecture (self, etiquette, ligne, deplacement):

        info = self.donnees[ligne]
        valide = bool (info[0]) and etiquette == info[1 :]

        if not valide:
            self.ecriture (etiquette, ligne)
            
        print ("Bloc n° " + etiquette + ligne)
        print ("Octet n° " + deplacement)


    def ecriture (self, etiquette, ligne):

        valide = 0 <= etiquette < self.nbEtiquettes

        if valide:
            self.donnees[ligne] = "1" + etiquette
            
        else:
            self.donnees[ligne] = self.defaut


    def start (self, entree):

        # Gestion de l'entrée
        adresse, mode = entree.split (':')
        adresse = int (adresse)

        etiquette = adresse // self.numLigne
        ligne = adresse // self.numDeplacement % self.numLigne
        deplacement = adresse % self.numDeplacement
        
        # Gestion du mode
        match mode:
            
            case "W":
                self.ecriture (etiquette, ligne)

            case "R":
                self.lecture (etiquette, ligne, deplacement)


# Utilisation

def tests ():

    c1 = Cache ()
    c1.start (input ())
    c1.start (input ())


tests ()
