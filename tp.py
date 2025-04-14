[11] class Bibliotheque:
def _init_(self):
    self.livres_disponibles ={}
    self.utilisateurs = {}
#Ajoute un livre à la bibliothèque.
def ajouter_livre(self, titre, auteur, disponibilite=True):
    self.livres_disponibles[titre] = {'auteur': auteur, 'disponible'; disponibilite}
# Recherche des livres dans la bibliotheque en fonction du critere spécifié."
def rechercher_livre(self, critere, type_recherche='titre'):
    resultats = []
    for titre, info in self.livres_disponibles.items():
        if type_recherche == 'titre' and critere.lower() in titre.lower():
            resultats.append((titre, info['auteur']))
        elif type_recherche == 'auteur' and critere.lower() in info['auteur'].lower():
            resultats.append((titre, info['auteur']))elif type_recherche == 'critere':
        if critere.lower() in titre.lower() or critere.lower() in info['auteur'].lower():
            resultats.append((titre, info['auteur']))
return resultats            
# Permet à un utilisateur d'emprunter un livre."··
def emprunter_livre(self, titre, utilisateur):
    if titre in self.livres_disponibles and self.livres_disponibles[titre]['disponible']:
        self.livres_disponibles[titre]['disponible'] = False
        if utilisateur in self.utilisateurs:
            self.utilisateurs[utilisateur].append(titre)
        else:
            self.utilisateurs[utilisateur] = [titre]
        return True
    else:
        return False
# Permet à un utilisateur de retourner un livre emprunté.""·
def retourner_livre(self, titre, utilisateur):
    if utilisateur in self.utilisateurs and titre in self.utilisateurs[utilisateur]:
        self.livres_disponibles[titre]['disponible']= True
        self.utilisateurs[utilisateur].remove(titre)
        return True
    else:
        return False
# Crée un compte utilisateur avec le nom spécifié. "··
def creer_utilisateur(self, nom_utilisateur):
    if nom_utilisateur not in self.utilisateurs:
        self.utilisateurs[nom_utilisateur] = []
        return True
    else:
        return False