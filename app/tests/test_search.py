from fastapi.testclient import TestClient
from ..main import app
client = TestClient(app)


def test_cv_not_found():
    response = client.get("/search_cv?q=javax", json={"q": "javax"})
    assert response.status_code == 200
    assert response.json() == []
    print(response.json())


def test_cv_java_profile():
    response = client.get("/search_cv?q=java")
    assert response.status_code == 200
    assert {
        "_index": "cv_search",
        "_type": "cv",
        "_id": "d21e6a80-223d-548f-b5ec-b836c8226e37",
        "_score": 0.40230206,
        "_source": {
            "info": "Développeur junior chez Fleetizen\n\nÉtudiant en master STL (Science et Technologie du Logiciel)\n\n\n\n\n\nDéveloppeur junior chez Fleetizen\n\nÉtudiant en master STL (Science et Technologie du Logiciel)\n\n\n\n\n\nAlessandro RINAUDO\n\n\n\nAlessandro RINAUDO\n\n\n\n\n\n\n\n \n\n      DIPLOMAS Y HOBBIES\n\n\n\nFormaciones : Diplomados, Congresos, xxxxxxxxxx xxxxxx xxxxxxxxx xxxxxxxxxxxxxxxxx\n\nHobbies: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n \n\n      DIPLOMAS Y HOBBIES\n\n\n\nFormaciones : Diplomados, Congresos, xxxxxxxxxx xxxxxx xxxxxxxxx xxxxxxxxxxxxxxxxx\n\nHobbies: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n\n\n\n\n\n\n\n\n\n75015\n\nParis, France               \n\n75015\n\nParis, France               \n\n06. 45 67 10 82\n\n06. 45 67 10 82\n\nalessandro.rinaudo@gmail.com \n\n\n\nalessandro.rinaudo@gmail.com \n\n\n\n\n\n\n\n\n\nLANGUES\n\nLANGUES\n\n\n\nEXPERIENCES PROFESSIONNELLES\n\nEXPERIENCES PROFESSIONNELLES\n\n\n\nItalien:    Langue maternelle\n\nFrançais:  C1\n\nAnglais:   B2\n\nItalien:    Langue maternelle\n\nFrançais:  C1\n\nAnglais:   B2\n\n\n\n\n\n2020-2021\n\nPuteaux, France\n\n\n\n\n\n\n\n\n\n2020-2021\n\nPuteaux, France\n\n\n\n\n\n\n\n\n\n\n\nDéveloppeur junior en alternance chez Fleetizen\n\n\n\n\n\nDéveloppeur junior en alternance chez Fleetizen\n\n\n\n\n\n\n\n\n\nFORMATION\t\n\nFORMATION\t\n\n\n\nRÉSEAUX SOCIAUX\n\nRÉSEAUX SOCIAUX\n\n\n\n\n\nhttps://www.linkedin.com/in/alessandro-rinaudo-403a001b3/\n\n\n\nhttps://www.linkedin.com/in/alessandro-rinaudo-403a001b3/\n\n\n\nhttps://github.com/AlessandroRinaudo\n\n\n\nhttps://github.com/AlessandroRinaudo\n\n\n\nhttp://alessandroserver.com \n\nhttp://alessandroserver.com \n\n\n\nhttps://gitlab.alessandroserver.com/Alessandro \n\n\n\nhttps://gitlab.alessandroserver.com/Alessandro \n\n2021-2022\n\nParis, France\n\n\n\n\n\n\n\n\n\n\n\n2020-2021\n\nParis, France\n\n\n\n\n\n\n\n\n\n\n\n2017-2020\n\nParis, France\n\n2021-2022\n\nParis, France\n\n\n\n\n\n\n\n\n\n\n\n2020-2021\n\nParis, France\n\n\n\n\n\n\n\n\n\n\n\n2017-2020\n\nParis, France\n\nMASTER 2: Science et téchnologie du Logiciel – Sorbonne Université Campus Jussieu \n\nConnaissance visée:  Apprentissage de méthodes et d'outils rigoureux pour la conception et le développement de logiciels complexes ainsi que pour la modélisation et l'analyse de problèmes algorithmiques.\n\nBAC+4: Analyste Développeur – CFA INSTA 75002 Paris \nConnaissance visée: Programmation SaaS, MEAN stack, Backend algorithmique, Culture DevOps. \n\nLICENCE: Informatique - Université Descartes, Paris V               Connaissance visée: programmation orientée objet, programmation fonctionnelle, programmation procédurale, algorithmique , scripting , sécurité. informatique. \n\n\n\n\n\nMASTER 2: Science et téchnologie du Logiciel – Sorbonne Université Campus Jussieu \n\nConnaissance visée:  Apprentissage de méthodes et d'outils rigoureux pour la conception et le développement de logiciels complexes ainsi que pour la modélisation et l'analyse de problèmes algorithmiques.\n\nBAC+4: Analyste Développeur – CFA INSTA 75002 Paris \nConnaissance visée: Programmation SaaS, MEAN stack, Backend algorithmique, Culture DevOps. \n\nLICENCE: Informatique - Université Descartes, Paris V               Connaissance visée: programmation orientée objet, programmation fonctionnelle, programmation procédurale, algorithmique , scripting , sécurité. informatique. \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n2020-2021\n\nParis, France\n\n\n\n2020-2021\n\nParis, France\n\n\n\n\n\n \n\n\n\n\n\n2017-2020\n\nParis, France\n\n2017-2020\n\nParis, France\n\n\n\n\n\n\n\nCENTRES D’INTERÊT:\n\nCENTRES D’INTERÊT:\n\nCOMPETENCES\n\nCOMPETENCES\n\n\n\n\n\nVidéo making : réalisation de différents courts métrages et participation à plusieurs concours de cinéma \n\n\n\nEngagement associatif :  membre actif de l’association de bénevola https://ilcuoregrandediflavio.it \n\n\n\nVidéo making : réalisation de différents courts métrages et participation à plusieurs concours de cinéma \n\n\n\nEngagement associatif :  membre actif de l’association de bénevola https://ilcuoregrandediflavio.it \n\n\n\n\n\nFront-end : React Js, Angular Html, Css, JS ,Bootsrap, \n\nBack-end logique : Node JS Java, Php \n\nBack-end data : SQL\n\nScripting : Bash                     \t\t\t\n\nOutils de développement : VisualStudio Code, PhpStorm\n\nOutils Collaboratifs et CI/CD : GitHub, GitLab \n\nOutils de conteneurisation : Docker\n\n\n\n\n\nFront-end : React Js, Angular Html, Css, JS ,Bootsrap, \n\nBack-end logique : Node JS Java, Php \n\nBack-end data : SQL\n\nScripting : Bash                     \t\t\t\n\nOutils de développement : VisualStudio Code, PhpStorm\n\nOutils Collaboratifs et CI/CD : GitHub, GitLab \n\nOutils de conteneurisation : Docker\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCommunication\n\nIncourage les collegues\n\n\n\nCommunication\n\nIncourage les collegues\n\n\n\nQUALITÉS PERSONNELLES\n\nQUALITÉS PERSONNELLES\n\nBateau de Thibault : réalisation d’un backoffice pour les revendeurs des produits de mer avec authentification JWT.\n\nTechover Marketplace : réalisation d’un Marketplace de formations professionnelles en lignes.\n\nDesannales: réalisation d’une application web permettant aux étudiants de s’échanger des documents universitaires afin de mieux se préparer pour les examens.\n\nPersonal web server : mise en place d’un web server personnelle avec plusieurs micro-services et applications self-hosted en utilisant docker ou crées directement par moi-même.\n\n\n\n\n\nBateau de Thibault : réalisation d’un backoffice pour les revendeurs des produits de mer avec authentification JWT.\n\nTechover Marketplace : réalisation d’un Marketplace de formations professionnelles en lignes.\n\nDesannales: réalisation d’une application web permettant aux étudiants de s’échanger des documents universitaires afin de mieux se préparer pour les examens.\n\nPersonal web server : mise en place d’un web server personnelle avec plusieurs micro-services et applications self-hosted en utilisant docker ou crées directement par moi-même.\n\n\n\n\n\nPROJETS RÉALISÉS\n\nPROJETS RÉALISÉS\n\nSYNTHESE PROFESSIONNELLE\n\n\n\nSYNTHESE PROFESSIONNELLE",
            "emailAdress": "alessandro.rinaudo@gmail.com",
            "phoneNumber": "",
            "variousURL": [
                "https://www.linkedin.com/in/alessandro-rinaudo-403a001b3/",
                "https://www.linkedin.com/in/alessandro-rinaudo-403a001b3/",
                "https://github.com/AlessandroRinaudo",
                "https://github.com/AlessandroRinaudo",
                "http://alessandroserver.com",
                "http://alessandroserver.com",
                "https://gitlab.alessandroserver.com/Alessandro",
                "https://gitlab.alessandroserver.com/Alessandro",
                "https://ilcuoregrandediflavio.it",
                "https://ilcuoregrandediflavio.it"
            ]
        }
    } in response.json()
    print(response.json())


def test_cv_correct_info_only():
    response = client.get("/search_cv?q=java&contactInfoOnly=true")
    assert response.status_code == 200
    assert {
        "_index": "cv_search",
        "_type": "cv",
        "_id": "d21e6a80-223d-548f-b5ec-b836c8226e37",
        "_score": 0.40230206,
        "_source": {
            "phoneNumber": "",
            "variousURL": [
                "https://www.linkedin.com/in/alessandro-rinaudo-403a001b3/",
                "https://www.linkedin.com/in/alessandro-rinaudo-403a001b3/",
                "https://github.com/AlessandroRinaudo",
                "https://github.com/AlessandroRinaudo",
                "http://alessandroserver.com",
                "http://alessandroserver.com",
                "https://gitlab.alessandroserver.com/Alessandro",
                "https://gitlab.alessandroserver.com/Alessandro",
                "https://ilcuoregrandediflavio.it",
                "https://ilcuoregrandediflavio.it"
            ],
            "emailAdress": "alessandro.rinaudo@gmail.com"
        }
    } in response.json()
    print(response.json())
