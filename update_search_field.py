import json

# Specific extra keywords for certain apps (the top ones)
extra_keywords_dict = {
    "ChatGPT": "intelligence artificielle, llm, openai, gpt-4, gpt-3, assistant virtuel, rédaction, programmation, code, questions, conversation",
    "Claude": "anthropic, sonnet, opus, haiku, analyse de texte, éthique, résumé, pdf, documents, programmation",
    "Gemini": "google, bard, pro, ultra, multimodal, recherche, intégration google workspace, vision, images",
    "Grok": "x, twitter, elon musk, temps réel, actualités, non-censuré, xai",
    "Perplexity": "moteur de recherche, sources, citations, réponses sourcées, recherche académique",
    "Poe": "quora, bots personnalisés, multi-modèles, création d'assistants",
    "Mistral": "startup française, mistral ai, open source, europe, mixtral, modèles locaux",
    "Character.ai": "roleplay, jeu de rôle, personnages historiques, avatars, divertissement",
    "Pi": "empathie, soutien émotionnel, conversation naturelle, inflexion ai",
    "HuggingChat": "hugging face, communauté, open source, modèles libres",
    "DeepSeek": "performances mathématiques, code, chine, open source, apprentissage",
    "You.com": "recherche sémantique, agents web, confidentialité",
    "Arc Search": "navigateur, ios, création de pages web, résumé d'articles",
    "Microsoft Copilot": "bing chat, windows, office 365, dall-e, entreprise, word, excel",
    "Kimi": "lune, contexte ultra long, documents volumineux, chine",
    "DuckDuckGo AI": "recherche privée, anonymat, sans pistage",
    "Midjourney": "génération d'images, discord, art numérique, photoréalisme, v6",
    "DALL-E 3": "chatgpt, génération d'images, intégration fluide, openai",
    "Stable Diffusion": "stability ai, open source, contrôle poussé, controlnet, local",
    "Adobe Firefly": "photoshop, illustrator, retouche, génération légale, droits d'auteur",
    "Canva Magic Design": "réseaux sociaux, présentations, marketing, design facile",
    "Leonardo.ai": "assets de jeu, 3d, contrôle de la génération, concept art",
    "Recraft": "art vectoriel, icônes, illustrations, design graphique",
    "Magnific AI": "upscaling, amélioration de la résolution, hd, détails",
    "Krea.ai": "génération en temps réel, croquis, ipad, design instantané",
    "Looka": "branding, identité de marque, création de logos, charte graphique",
    "Photoroom": "suppression fond, détourage, e-commerce, packshot",
    "Sora": "vidéo générative, réalisme époustouflant, openai",
    "Runway Gen-3": "montage vidéo, effets spéciaux, génération text-to-video",
    "Kling AI": "génération de vidéo chinoise, physique réaliste, haute fidélité",
    "HeyGen": "avatars réalistes, traduction, clonage de voix, marketing vidéo",
    "Synthesia": "avatar d'entreprise, formation, elearning, voix off",
    "Suno": "génération de chansons, musique complète, paroles, hit",
    "Udio": "musique haute fidélité, production professionnelle, pistes",
    "ElevenLabs": "clonage vocal, text-to-speech, voix off, narration, podcast",
    "Cursor": "vs code, ide, développement, programmation assistée, ai coding",
    "GitHub Copilot": "développeur, complétion de code, microsoft, git",
    "V0.dev": "vercel, ui, react, tailwind, génération d'interfaces, front-end",
    "Bolt.new": "stack complete, web, itération rapide, développement"
}

# Category synonyms to add to ALL apps in those categories
category_synonyms = {
    "ASSISTANTS & CHATBOTS": ["assistant virtuel", "chatbot", "conversation", "aide", "qa", "questions", "réponses", "chat", "ia", "intelligence artificielle"],
    "IMAGES & DESIGN": ["génération images", "photo", "dessin", "graphisme", "visuel", "art numérique", "peinture", "ui", "ux", "esthétique", "création"],
    "VIDÉO & ANIMATION": ["montage vidéo", "film", "clip", "effets spéciaux", "vfx", "motion", "mouvement", "audiovisuel", "youtube", "tiktok", "animation"],
    "AUDIO & MUSIQUE": ["son", "voix", "chanson", "piste", "audio", "enregistrement", "parlé", "mp3", "wav", "podcast", "rythme", "mélodie"],
    "DÉVELOPPEMENT & CODE": ["programmation", "développeur", "dev", "script", "logiciel", "web", "html", "css", "js", "python", "github", "applications"],
    "RÉDACTION & MARKETING": ["texte", "écriture", "blog", "seo", "campagne", "publicité", "copie", "mots", "articles", "copywriting", "social", "réseaux"],
    "PRODUCTIVITÉ": ["organisation", "efficacité", "gain de temps", "tâches", "gestion", "planning", "automation", "outil", "agenda", "calendrier", "travail"],
    "RECHERCHE & ÉDUCATION": ["école", "étudiant", "science", "académique", "savoir", "apprentissage", "tuteur", "cours", "études", "université", "documents"],
    "NO-CODE & WEB": ["sans code", "site internet", "app builder", "création web", "nocode", "hébergement", "landing page", "saas", "plateforme"],
    "DIVERS": ["outils pratiques", "utilitaires", "fun", "autre", "divers", "loisir"]
}

# Tag and word substring matching to inject synonyms globally
tag_synonyms_rules = {
    "3d": ["trois dimensions", "modélisation", "rendu", "spatial", "volume", "mesh", "blend"],
    "api": ["développeur", "intégration", "endpoint", "programmation", "backend"],
    "aca": ["école", "université", "étudiant", "professeur", "recherche", "thèse", "académique"],
    "accessibilit": ["handicap", "inclusif", "aide", "lecture", "facile"],
    "ads": ["publicité", "marketing", "promotion", "campagne", "sponsor", "facebook ads", "google ads"],
    "agent": ["bot", "assistant autonome", "robot", "tâche automatisée"],
    "analyse": ["statistiques", "données", "rapports", "insights", "compréhension"],
    "app": ["application", "mobile", "smartphone", "ios", "android", "tablette"],
    "art": ["création", "dessin", "peinture", "illustration", "visuel", "artiste"],
    "asset": ["ressources", "fichiers", "éléments", "jeu", "banque"],
    "assist": ["aide", "virtuel", "chatbot", "compagnon", "soutien", "assistant"],
    "audio": ["son", "bruitage", "écoute", "musique", "voix", "micro"],
    "auto": ["automatisation", "gain de temps", "processus", "workflow", "zapier"],
    "avatar": ["personnage", "profil", "humain virtuel", "visage"],
    "bien": ["santé", "mental", "psychologie", "zen", "détente", "calme"],
    "blog": ["article", "rédaction", "post", "site perso", "wordpress", "contenu"],
    "brand": ["marque", "logo", "identité", "charte graphique", "entreprise"],
    "business": ["entreprise", "pme", "startup", "pro", "commerce", "b2b", "vente", "société"],
    "bot": ["robot", "chat", "conversation", "ia", "assistant"],
    "cloud": ["en ligne", "saas", "serveur", "hébergement", "internet"],
    "code": ["programmation", "développement", "logiciel", "script", "html", "css", "javascript", "python"],
    "collaborat": ["équipe", "partage", "ensemble", "multi-utilisateurs", "projet"],
    "communaut": ["forum", "discord", "groupe", "utilisateurs", "social"],
    "context": ["mémoire", "long", "tokens", "compréhension", "taille document"],
    "copy": ["rédaction", "vente", "marketing", "texte", "slogan", "persuasion"],
    "corporate": ["entreprise", "société", "groupe", "rh", "employés"],
    "data": ["données", "chiffres", "base de données", "analyse", "statistiques", "big data"],
    "design": ["interface", "ui", "ux", "esthétique", "graphisme", "création", "maquette"],
    "dev": ["code", "programmation", "logiciel", "ingénieur", "développement", "github"],
    "ecommerce": ["boutique", "vente en ligne", "produits", "shopify", "achats", "panier"],
    "edu": ["apprentissage", "école", "formation", "professeur", "tutoriel", "pédagogie"],
    "learn": ["apprentissage", "école", "formation", "professeur", "tutoriel", "pédagogie"],
    "email": ["mail", "courriel", "newsletter", "messagerie", "gmail", "outlook"],
    "english": ["anglais", "langue", "traduction", "texte"],
    "europe": ["rgpd", "français", "souveraineté", "eu", "local"],
    "fast": ["rapide", "vitesse", "immédiat", "temps réel"],
    "rapid": ["rapide", "vitesse", "immédiat", "temps réel"],
    "fun": ["divertissement", "blague", "jeu", "loisir", "humour"],
    "game": ["jeu", "vidéo", "joueur", "gaming", "unreal", "unity", "divertissement", "assets"],
    "graphic": ["image", "dessin", "illustration", "visuel", "vecteur"],
    "legal": ["droit", "avocat", "lois", "juridique", "contrat"],
    "libre": ["open source", "gratuit", "github", "communauté", "public"],
    "market": ["vente", "publicité", "promotion", "croissance", "seo", "réseaux sociaux"],
    "math": ["calcul", "science", "algèbre", "numérique", "équations"],
    "media": ["presse", "réseaux", "actualités", "contenu", "journalisme"],
    "meet": ["réunion", "visio", "zoom", "google meet", "teams", "transcription", "agenda"],
    "music": ["musique", "son", "chanson", "piste", "audio", "rythme", "mélodie"],
    "musique": ["musique", "son", "chanson", "piste", "audio", "rythme", "mélodie"],
    "nocode": ["sans code", "création facile", "visuel", "application web", "site"],
    "open": ["libre", "source", "gratuit", "github", "ouvert"],
    "photo": ["image", "appareil", "retouche", "détourage", "pixel", "objectif"],
    "plan": ["organisation", "calendrier", "agenda", "tâches", "gestion"],
    "podcast": ["audio", "émission", "voix", "radio", "spotify"],
    "pro": ["entreprise", "expert", "avancé", "travail", "b2b", "qualité", "professionnel"],
    "productivit": ["efficacité", "gain de temps", "organisation", "tâches"],
    "recherche": ["moteur", "google", "trouver", "sources", "réponses", "web", "investigation"],
    "research": ["moteur", "google", "trouver", "sources", "réponses", "web", "science", "académique"],
    "seo": ["référencement", "google", "mots-clés", "trafic", "web", "positionnement"],
    "social": ["réseaux", "instagram", "tiktok", "facebook", "twitter", "linkedin", "community management"],
    "speech": ["voix", "parole", "lecture", "texte vers voix", "tts"],
    "stt": ["transcription", "dictée", "voix vers texte", "sous-titres", "audio vers texte"],
    "tts": ["synthèse vocale", "voix", "lecture", "robot vocal", "texte vers voix"],
    "tech": ["technologie", "informatique", "innovation", "startup"],
    "texte": ["rédaction", "mots", "lettres", "phrase", "article"],
    "video": ["film", "clip", "montage", "youtube", "tiktok", "vlog", "caméra"],
    "vidéo": ["film", "clip", "montage", "youtube", "tiktok", "vlog", "caméra"],
    "voice": ["voix", "parole", "audio", "chant", "clone", "synthèse"],
    "web": ["site", "internet", "navigateur", "en ligne", "html", "création web"],
    "work": ["travail", "emploi", "entreprise", "tâches", "équipe"],
    "writ": ["écriture", "rédaction", "auteur", "livre", "blog", "copywriting"]
}

def generate_search_terms(app, cat_name):
    name = app.get("name", "")
    desc = app.get("desc", "")
    tags = app.get("tags", [])
    
    # 1. Start with the core info
    keywords_set = set([name.lower(), cat_name.lower()])
    
    for t in tags:
        keywords_set.add(t.lower())
    
    # 2. Add extra keywords if defined specifically for this app
    if name in extra_keywords_dict:
        for k in extra_keywords_dict[name].split(","):
            keywords_set.add(k.strip().lower())
            
    # 3. Add Category synonyms
    if cat_name in category_synonyms:
        for syn in category_synonyms[cat_name]:
            keywords_set.add(syn.lower())
            
    # 4. Add Tag-based smart synonyms
    for t in tags:
        t_low = t.lower()
        for rule_key, synonyms in tag_synonyms_rules.items():
            if rule_key in t_low:
                for syn in synonyms:
                    keywords_set.add(syn.lower())
                    
    # Format words neatly, ensuring original casing for some, or just lowercase is fine
    # For a neat display, let's keep them title case or just standard lowercase
    final_keywords = sorted(list(keywords_set))
    
    app["searchKeywords"] = f"{desc}. Mots-clés: {', '.join(final_keywords)}"
    return app

def main():
    with open("src/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for category in data:
        cat_name = category.get("name", "")
        for app in category.get("apps", []):
            generate_search_terms(app, cat_name)

    with open("src/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()
