from experta import Rule, Fact, KnowledgeEngine, AND

class maladieRespiratoire(KnowledgeEngine):
    # Variables pour les réponses
    maladies = ""
    description = ""
    traitement = ""
    photo = ""


    # Asthme
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='0'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='0'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='0'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Asthme(self):
        self.maladies = "Maladie : Asthme"
        self.description = "Description : L'asthme est une maladie respiratoire chronique qui se caractérise par des difficultés à respirer, une toux persistante et une respiration sifflante."
        self.traitement = "Traitement : Le traitement de l'asthme peut inclure l'utilisation de bronchodilatateurs, de corticostéroïdes inhalés et d'autres médicaments selon la gravité des symptômes. Consultez un professionnel de la santé pour un plan de traitement personnalisé."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\asthma.jpg"


    # Bronchite
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='0'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Bronchite(self):
        self.maladies = "Maladie : Bronchite"
        self.description = "Description : La bronchite est une inflammation des bronches, les tubes qui transportent l'air vers les poumons. Elle peut provoquer une toux persistante, des difficultés respiratoires et de la fatigue."
        self.traitement = "Traitement : Le traitement de la bronchite dépend de sa cause, qu'elle soit virale ou bactérienne. Il peut inclure des médicaments antiviraux, des antibiotiques, des bronchodilatateurs et des mesures pour soulager les symptômes. Consultez un professionnel de la santé pour un diagnostic et un traitement appropriés."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\bronchitis.jpg"


    # Pneumonie
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='1'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='1'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Pneumonie(self):
        self.maladies = "Maladie : Pneumonie"
        self.description = "Description : La pneumonie est une infection des sacs d'air dans les poumons. Les symptômes peuvent inclure une toux persistante, des difficultés respiratoires, de la fièvre et de la fatigue."
        self.traitement = "Traitement : Le traitement de la pneumonie dépend de la cause de l'infection. Il peut inclure des antibiotiques, des antiviraux, des médicaments pour soulager les symptômes et, dans certains cas, une hospitalisation. Consultez un professionnel de la santé pour un diagnostic précis."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\pneumonia.jpg"


    # Tuberculose
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='1'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='1'), Fact(Eternuements='0'), Fact(PerteOdorat='1'),
              Fact(PerteDuGout='1'), Fact(PertePoids='1'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Tuberculose(self):
        self.maladies = "Maladie : Tuberculose"
        self.description = "Description : La tuberculose est une infection bactérienne qui affecte les poumons. Elle peut provoquer une toux persistante, des difficultés respiratoires, une perte de poids et d'autres symptômes variés."
        self.traitement = "Traitement : Le traitement de la tuberculose implique généralement l'utilisation d'antibiotiques sur une période prolongée. Un suivi médical régulier est essentiel pour surveiller la réponse au traitement et prévenir la propagation de l'infection."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\tuberculosis.jpg"


    # Insuffisance Respiratoire
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='1'), Fact(Frissons='1'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='1'), Fact(Eternuements='0'), Fact(PerteOdorat='1'),
              Fact(PerteDuGout='1'), Fact(PertePoids='1'), Fact(Pâleur='1'), Fact(Vertiges='1')))
    def InsuffisanceRespiratoire(self):
        self.maladies = "Maladie : Insuffisance Respiratoire"
        self.description = "Description : L'insuffisance respiratoire se produit lorsque les poumons ne fonctionnent pas correctement, entraînant des difficultés respiratoires, de la fatigue, une perte de poids et d'autres symptômes."
        self.traitement = "Traitement : Le traitement de l'insuffisance respiratoire dépend de sa cause sous-jacente. Il peut inclure l'oxygénothérapie, des médicaments bronchodilatateurs, la gestion des maladies sous-jacentes et, dans certains cas, une assistance respiratoire."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\respiratory_failure.jpg"


    # Bronchite Chronique
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='1'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='1'), Fact(Frissons='1'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='1'), Fact(Eternuements='0'), Fact(PerteOdorat='1'),
              Fact(PerteDuGout='1'), Fact(PertePoids='1'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def BronchiteChronique(self):
        self.maladies = "Maladie : Bronchite Chronique"
        self.description = "Description : La bronchite chronique est une inflammation persistante des bronches. Elle peut provoquer une toux persistante, des difficultés respiratoires, de la fatigue et d'autres symptômes respiratoires."
        self.traitement = "Traitement : Le traitement de la bronchite chronique vise à soulager les symptômes et à améliorer la fonction pulmonaire. Il peut inclure l'utilisation de bronchodilatateurs, de corticostéroïdes inhalés et des mesures pour réduire l'exposition aux irritants pulmonaires."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\chronic_bronchitis.jpg"


    # Fibrose Pulmonaire
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='1'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def FibrosePulmonaire(self):
        self.maladies = "Maladie : Fibrose Pulmonaire"
        self.description = "Description : La fibrose pulmonaire est une maladie caractérisée par la formation de tissu cicatriciel dans les poumons, ce qui rend la respiration difficile."
        self.traitement = "Traitement : Le traitement de la fibrose pulmonaire vise à ralentir la progression de la maladie et à soulager les symptômes. Il peut inclure l'utilisation de médicaments anti-fibrotiques, la réhabilitation pulmonaire et, dans certains cas, une transplantation pulmonaire."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\pulmonary_fibrosis.jpg"

    # Maladie Pulmonaire Obstructive Chronique (MPOC)
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='1'), Fact(Pâleur='1'), Fact(Vertiges='0')))
    def MPOC(self):
        self.maladies = "Maladie : Maladie Pulmonaire Obstructive Chronique (MPOC)"
        self.description = "Description : La MPOC est un terme générique regroupant des affections pulmonaires telles que la bronchite chronique et l'emphysème."
        self.traitement = "Traitement : Le traitement de la MPOC vise à soulager les symptômes et à améliorer la fonction pulmonaire. Il peut inclure l'utilisation de bronchodilatateurs, de corticostéroïdes inhalés et des programmes de réhabilitation pulmonaire. Dans les cas graves, une oxygénothérapie ou une intervention chirurgicale peuvent être nécessaires."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\copd.jpg"


    # Pneumothorax
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='0'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'), Fact(PerteOdorat='0'),
              Fact(PerteDuGout='0'), Fact(PertePoids='0'), Fact(Pâleur='1'), Fact(Vertiges='0')))
    def Pneumothorax(self):
        self.maladies = "Maladie : Pneumothorax"
        self.description = "Description : Le pneumothorax est une affection où de l'air s'accumule dans l'espace autour des poumons, provoquant un effondrement partiel ou complet d'un poumon."
        self.traitement = "Trzitement : Le traitement du pneumothorax dépend de la gravité de l'affection. Dans les cas légers, l'observation peut suffire. Pour les cas plus graves, une aspiration de l'air ou une intervention chirurgicale peut être nécessaire pour rétablir la pression normale dans la poitrine."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\pneumothorax.jpg"

    # Sinusite
    @Rule(AND(Fact(TouxPersistante='0'), Fact(Essoufflement='0'), Fact(DouleurThoracique='0'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='0'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='1'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='1'), Fact(MauxDeTete='1'), Fact(Eternuements='1'), Fact(PerteOdorat='1'),
              Fact(PerteDuGout='0'), Fact(PertePoids='0'), Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Sinusite(self):
        self.maladies = "Maladie : Sinusite"
        self.description = "Description : La sinusite est une inflammation des sinus, généralement causée par une infection. Les symptômes incluent de la fièvre, une congestion nasale, des maux de tête et des éternuements fréquents."
        self.traitement = "Traitement : Le traitement de la sinusite dépend de la cause sous-jacente. Il peut inclure des décongestionnants, des antihistaminiques, des corticostéroïdes nasaux et des analgésiques. Dans les cas bactériens, des antibiotiques peuvent également être prescrits."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\sinusitis.jpg"

    # Infection Pulmonaire
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'),
              Fact(PerteOdorat='0'), Fact(PerteDuGout='0'), Fact(PertePoids='1'),
              Fact(Pâleur='0'), Fact(Vertiges='0')))
    def InfectionPulmonaire(self):
        self.maladies = "Maladie : Infection Pulmonaire"
        self.description = "Description : L'infection pulmonaire est une infection des voies respiratoires inférieures, souvent causée par des bactéries ou des virus."
        self.traitement = "Traitement : Le traitement des infections pulmonaires dépend du type d'agent pathogène. Les infections virales sont généralement traitées par des médicaments antiviraux, tandis que les infections bactériennes nécessitent des antibiotiques. Un repos adéquat et une hydratation sont également recommandés."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\infectionpulmonaire.jpg"

    # Toux chez Enfant
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='0'), Fact(DouleurThoracique='0'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='0'), Fact(Fievre='1'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'),
              Fact(PerteOdorat='0'), Fact(PerteDuGout='0'), Fact(PertePoids='0'),
              Fact(Pâleur='0'), Fact(Vertiges='0')))
    def TouxChezEnfant(self):
        self.maladies = "Maladie : Toux chez l'enfant"
        self.description = "Description : La toux chez l'enfant peut être causée par divers facteurs, y compris les infections virales ou bactériennes."
        self.traitement = "Traitement : Le traitement de la toux chez l'enfant dépend de la cause sous-jacente. Il peut inclure des médicaments antitussifs, des hydratants, et des mesures pour soulager les symptômes. Consultez un pédiatre pour des conseils adaptés à l'âge de l'enfant."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\touxenfant.jpg"

    # Atélectasie
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'),
              Fact(PerteOdorat='0'), Fact(PerteDuGout='0'), Fact(PertePoids='0'),
              Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Atelectasie(self):
        self.maladies = "Maladie : Atélectasie"
        self.description = "Description : L'atélectasie est une affection pulmonaire caractérisée par le collapsus ou la fermeture des petites voies aériennes dans les poumons. Cela peut entraîner une diminution de l'oxygénation des tissus."
        self.traitement = "Traitement : Le traitement de l'atélectasie dépend de la cause sous-jacente. Il peut inclure la physiothérapie respiratoire, l'utilisation de dispositifs de pression positive, et le traitement de la cause contributive."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\altelectasie.jpg"

    # Plèvre
    @Rule(AND(Fact(TouxPersistante='0'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='0'), Fact(FatigueExcessive='1'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='1'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'),
              Fact(PerteOdorat='0'), Fact(PerteDuGout='0'), Fact(PertePoids='0'),
              Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Plèvre(self):
        self.maladies = "Maladie : Plèvre"
        self.description = "Description : La plèvre est l'inflammation des membranes entourant les poumons. Elle peut causer une douleur thoracique."
        self.traitement = "Traitement : Le traitement de la plèvre vise à soulager la douleur et à traiter la cause sous-jacente. Il peut inclure des médicaments anti-inflammatoires, des analgésiques, et parfois des procédures pour drainer l'excès de liquide de l'espace pleural."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\plevre.jpg"

    # Silicose
    @Rule(AND(Fact(TouxPersistante='1'), Fact(Essoufflement='1'), Fact(DouleurThoracique='1'),
              Fact(SifflementsRespiratoires='1'), Fact(FatigueExcessive='1'), Fact(Fievre='0'),
              Fact(RonflementFort='0'), Fact(ChangementsVoix='0'), Fact(CongestionNasale='0'),
              Fact(CrachatsAnormaux='0'), Fact(DouleursArticulaires='0'), Fact(Frissons='0'),
              Fact(MauxDeGorge='0'), Fact(MauxDeTete='0'), Fact(Eternuements='0'),
              Fact(PerteOdorat='0'), Fact(PerteDuGout='0'), Fact(PertePoids='0'),
              Fact(Pâleur='0'), Fact(Vertiges='0')))
    def Silicose(self):
        self.maladies = "Maladie : Silicose"
        self.description = "Description : La silicose est une maladie pulmonaire causée par l'inhalation de particules de silice."
        self.traitement = "Traitement : Il n'existe pas de traitement spécifique pour la silicose. Le traitement vise à soulager les symptômes et peut inclure l'arrêt."
        self.photo = r"C:\Users\Ghofrane\PycharmProjects\IA Project\photo\silicose.jpg"
