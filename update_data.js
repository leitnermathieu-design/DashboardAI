const fs = require('fs');

const data = JSON.parse(fs.readFileSync('./src/data.json', 'utf8'));

const promptsMap = {
    "ChatGPT": [
        "Agis en tant qu'expert en marketing et donne-moi une stratégie pour lancer mon nouveau produit innovant.",
        "Rédige-moi une lettre de motivation percutante pour un poste de développeur React.",
        "Explique-moi la théorie de la relativité comme si j'avais 10 ans."
    ],
    "Claude": [
        "Analyse le texte suivant et synthétise les trois arguments principaux en bullet points.",
        "Écris un script Python optimisé pour scraper les données d'un tableau HTML.",
        "Agis comme mon tuteur de français et corrige mes fautes en expliquant mes erreurs."
    ],
    "Midjourney": [
        "A futuristic city with flying cars at sunset, cyberpunk aesthetic, highly detailed, 8k resolution, octane render --ar 16:9",
        "A cute golden retriever puppy wearing an astronaut suit on the moon, hyper-realistic photography, dramatic lighting --ar 4:5",
        "Minimalist logo design for a coffee shop featuring a geometric bean, flat design, vector style"
    ],
    "Gemini": [
        "Planifie un voyage de 5 jours à Tokyo avec des recommandations de restaurants locaux.",
        "Résume la vidéo YouTube dont voici le lien en mettant en évidence les moments clés.",
        "Aide-moi à brainstormer des idées créatives pour le nom de ma nouvelle chaîne YouTube."
    ],
    "Perplexity": [
        "Quelles sont les dernières découvertes scientifiques en matière de fusion nucléaire ? Cite tes sources.",
        "Compare les meilleurs frameworks JavaScript en 2024 avec leurs avantages et inconvénients.",
        "Quel est l'impact de l'intelligence artificielle sur le marché de l'emploi dans les 5 prochaines années ?"
    ],
    "DALL-E 3": [
        "Une peinture à l'huile d'un chat lisant un livre dans une bibliothèque magique avec de la lumière chaude.",
        "Illustration vectorielle flat design d'un groupe de personnes travaillant ensemble sur des ordinateurs portables.",
        "Une photographie macro d'une goutte d'eau sur une feuille verte avec un reflet de la forêt en arrière-plan."
    ],
    "Stable Diffusion": [
        "Portrait of a cyberpunk girl with glowing neon tattoos, cyberpunk city background, depth of field, sharp focus, 8k",
        "Landscape of a fantasy world with floating islands and waterfalls, digital art, trending on artstation",
        "A cozy cabin in the snowy woods at night with warm yellow light coming from the windows, highly detailed painting"
    ],
    "Sora": [
        "Un drone survole une ville médiévale fantastique pendant un festival avec des feux d'artifice dans le ciel nocturne.",
        "Une personne marchant dans les rues de Tokyo la nuit sous la pluie, filmé en vue subjective avec des reflets néon dans les flaques d'eau.",
        "Animation 3D d'un petit robot explorant une planète extraterrestre remplie de plantes bioluminescentes."
    ],
    "Suno": [
        "Une chanson pop entraînante des années 80 sur le fait de tomber amoureux d'une IA, avec des synthétiseurs rétro.",
        "Un morceau de jazz relaxant avec un solo de saxophone doux, idéal pour étudier ou se concentrer.",
        "Une piste lofi hip hop avec des beats chill et une mélodie de piano nostalgique."
    ],
    "Runway Gen-3": [
        "Travelling avant lent dans un couloir d'une station spatiale abandonnée, ambiance sombre et mystérieuse.",
        "Gros plan d'un oeil qui s'ouvre, avec des galaxies tourbillonnantes se reflétant dans l'iris.",
        "Un lion majestueux rugissant au ralenti dans la savane africaine pendant le coucher du soleil."
    ],
    "GitHub Copilot": [
        "// Create a function that fetches user data from an API and handles errors gracefully",
        "// Write a React component for a customizable button with hover effects and loading state",
        "// Write unit tests for this utility function using Jest"
    ],
    "Cursor": [
        "Explain this code block and suggest optimizations for better performance.",
        "Refactor this component to use React Hooks instead of class components.",
        "Find and fix the memory leak in this useEffect hook."
    ],
    "Character.ai": [
        "Agis comme Albert Einstein et explique-moi comment tu as développé ta théorie.",
        "Jouons à un jeu de rôle d'aventure fantastique où tu es le maître du donjon.",
        "Parle-moi comme si tu étais un détective privé cynique des années 1940."
    ],
    "Adobe Firefly": [
        "Génère une image de paysage de montagne enneigée au coucher du soleil (style Aquarelle).",
        "Crée une texture de mur de briques rouges vieillies et usées pour une utilisation en 3D.",
        "(Effet de texte) Applique un style de lierres et de fleurs grimpantes sur le mot 'NATURE'."
    ]
};

data.forEach(category => {
    category.apps.forEach(app => {
        // Find prompts or generate some random ones if not in map
        if (promptsMap[app.name]) {
            app.prompts = promptsMap[app.name];
        } else {
             // Default generic prompts based on category
             if (category.name === 'ASSISTANTS & CHATBOTS') {
                app.prompts = ["Aide-moi à résoudre un problème complexe.", "Peux-tu m'expliquer ce concept simplement ?"];
             } else if (category.name === 'IMAGES & DESIGN') {
                app.prompts = ["Un magnifique paysage futuriste, hautement détaillé.", "Portrait d'un personnage de fantasy, éclairage dramatique."];
             } else if (category.name === 'VIDÉO & ANIMATION') {
                app.prompts = ["Plan cinématique d'une ville cyberpunk sous la pluie.", "Un animal sauvage se déplaçant dans la jungle au ralenti."];
             } else if (category.name === 'AUDIO & MUSIQUE') {
                app.prompts = ["Une musique entraînante pour une vidéo promotionnelle.", "Des effets sonores d'ambiance pour une scène spatiale."];
             } else {
                app.prompts = ["Comment puis-je utiliser cet outil de manière plus efficace ?"];
             }
        }
    });
});

fs.writeFileSync('./src/data.json', JSON.stringify(data, null, 4));
console.log('data.json updated with prompts successfully!');
