<script lang="ts">
  import { Star, TrendingUp, Sparkles, ArrowRight, Flame, Crown, Clock, Zap } from 'lucide-svelte';

  export let navigate: (path: string) => void;

  // Mock data for the Explore page, using real apps from the database
  const featuredApp = {
    name: "Midjourney",
    tagline: "La référence pour le photoréalisme",
    description: "Le générateur d'images par IA de référence. Midjourney repousse les limites du photoréalisme, de l'art numérique et du design d'interface fluide.",
    tags: ["Art", "Design", "Editor's Choice"],
    image: "https://picsum.photos/seed/midjourney/800/500", // Background hero
    logo: "https://favicon.im/midjourney.com",
    link: "https://www.midjourney.com",
    color: "from-indigo-600 to-cyan-500"
  };

  const collections = [
    {
      title: "Boîte à Outils Créative",
      subtitle: "Générez des images étonnantes.",
      gradient: "from-orange-500 to-amber-300",
      icon: Flame,
      appCount: 8
    },
    {
      title: "Assistants de Code",
      subtitle: "Devenez un dev décuplé.",
      gradient: "from-pink-500 to-rose-400",
      icon: Sparkles,
      appCount: 12
    },
    {
      title: "Audio & Création",
      subtitle: "La musique à portée de clavier.",
      gradient: "from-blue-600 to-indigo-400",
      icon: Zap,
      appCount: 5
    }
  ];

  const trendingApps = [
    { name: "ChatGPT", category: "Assistants", rank: 1, logo: "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/openai.svg", link: "https://chatgpt.com" },
    { name: "Claude", category: "Assistants", rank: 2, logo: "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/claude.svg", link: "https://claude.ai" },
    { name: "Suno", category: "Audio", rank: 3, logo: "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/suno.svg", link: "https://suno.com" },
    { name: "Sora", category: "Vidéo", rank: 4, logo: "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/openai.svg", link: "https://openai.com/sora" },
  ];
</script>

<div class="animate-in fade-in duration-700 pb-20">
  
  <!-- Content Container -->
  <div class="max-w-7xl mx-auto px-8 pt-8 space-y-24">
    
    <!-- Spotlight Hero (App of the Week) -->
    <section>
      <div class="flex items-center gap-3 mb-6">
        <Crown size={24} class="text-yellow-400" />
        <h2 class="text-2xl font-bold tracking-tight">App of the Week</h2>
      </div>
      
      <a href={featuredApp.link} target="_blank" rel="noopener noreferrer" class="relative block w-full rounded-[2.5rem] overflow-hidden group cursor-pointer border border-white/10 hover:border-white/20 transition-all duration-500 hover:shadow-[0_0_60px_rgba(79,70,229,0.2)]">
        <!-- Background Image with Gradient Overlay -->
        <div class="absolute inset-0 z-0">
          <div class={`absolute inset-0 bg-gradient-to-r ${featuredApp.color} mix-blend-multiply opacity-60 z-10 transition-opacity group-hover:opacity-40`}></div>
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/60 to-transparent z-10"></div>
          <img src={featuredApp.image} alt={featuredApp.name} class="w-full h-full object-cover scale-105 group-hover:scale-100 transition-transform duration-1000" />
        </div>
        
        <!-- Content -->
        <div class="relative z-20 p-10 md:p-16 flex flex-col justify-end h-[600px] md:h-[500px]">
          <div class="flex gap-3 mb-6 flex-wrap">
            {#each featuredApp.tags as tag}
              <span class="px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider bg-white/10 backdrop-blur-md border border-white/20 text-white">
                {tag}
              </span>
            {/each}
          </div>
          
          <h1 class="text-5xl md:text-7xl font-black mb-4 tracking-tight drop-shadow-lg flex items-center gap-4">
            <img src={featuredApp.logo} alt={featuredApp.name} class="w-16 h-16 rounded-xl shadow-lg border border-white/20 object-contain bg-white/10 p-2" />
            {featuredApp.name}
          </h1>
          <h3 class="text-2xl md:text-3xl text-gray-200 font-semibold mb-6">{featuredApp.tagline}</h3>
          <p class="text-lg text-gray-300 md:max-w-2xl leading-relaxed mb-8">
            {featuredApp.description}
          </p>
          
          <div class="flex items-center gap-4">
            <button class="px-8 py-4 bg-white text-black rounded-2xl font-bold text-lg transition-transform hover:scale-105 shadow-xl">
              Ouvrir {featuredApp.name}
            </button>
            <div class="px-6 py-4 bg-white/10 text-white rounded-2xl font-semibold backdrop-blur-md border border-white/20 hover:bg-white/20 transition-colors">
              Voir sur app central
            </div>
          </div>
        </div>
      </a>
    </section>

    <!-- Curated Collections -->
    <section>
      <div class="flex items-center justify-between mb-8">
        <div class="flex items-center gap-3">
          <Star size={24} class="text-pink-400" />
          <h2 class="text-3xl font-bold tracking-tight">Curated Collections</h2>
        </div>
        <a href="/apps" class="text-gray-400 hover:text-white flex items-center gap-1 font-medium transition-colors">
          View all <ArrowRight size={16} />
        </a>
      </div>

      <div class="grid md:grid-cols-3 gap-6">
        {#each collections as collection}
          <div class="group relative rounded-3xl overflow-hidden cursor-pointer h-72 border border-white/10 hover:border-white/30 transition-all duration-500 hover:-translate-y-2">
            <!-- Dynamic Gradient Background -->
            <div class={`absolute inset-0 bg-gradient-to-br ${collection.gradient} opacity-80 group-hover:scale-110 transition-transform duration-700`}></div>
            <div class="absolute inset-0 bg-black/20 group-hover:bg-black/0 transition-colors duration-500"></div>
            
            <!-- Grid pattern overlay -->
            <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')]"></div>

            <div class="relative p-8 h-full flex flex-col">
              <div class="w-12 h-12 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center mb-auto border border-white/30 shadow-lg">
                <svelte:component this={collection.icon} size={24} class="text-white" />
              </div>
              
              <div>
                <p class="text-white/80 font-medium mb-1">{collection.appCount} Apps</p>
                <h3 class="text-2xl font-bold text-white mb-2 leading-tight">
                  {collection.title}
                </h3>
                <p class="text-white/70 text-sm group-hover:text-white transition-colors delay-100">
                  {collection.subtitle}
                </p>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </section>

    <!-- Trending & Popular section -->
    <section>
      <div class="flex items-center gap-3 mb-8">
        <TrendingUp size={24} class="text-emerald-400" />
        <h2 class="text-3xl font-bold tracking-tight">Trending Now</h2>
      </div>

      <div class="bg-white/[0.02] border border-white/5 rounded-3xl p-6 md:p-10 backdrop-blur-sm">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6">
          {#each trendingApps as app}
            <a href={app.link} target="_blank" rel="noopener noreferrer" class="flex items-center gap-6 p-4 rounded-2xl hover:bg-white/5 transition-colors cursor-pointer group">
              <!-- Rank -->
              <div class="w-8 text-center text-3xl font-black text-gray-600 group-hover:text-gray-400 transition-colors">
                {app.rank}
              </div>
              
              <!-- App Logo -->
              <div class="logo w-16 h-16 rounded-2xl overflow-hidden border border-white/10 group-hover:border-white/30 shadow-lg transform group-hover:scale-105 transition-all bg-white/5 p-2 flex items-center justify-center">
                <img src={app.logo} alt={app.name} class="w-full h-full object-contain" />
              </div>
              
              <!-- App Info -->
              <div class="flex-1">
                <h4 class="text-lg font-bold text-white mb-1 group-hover:text-pink-300 transition-colors">{app.name}</h4>
                <p class="text-sm text-gray-500 font-medium">{app.category}</p>
              </div>

              <!-- Action -->
              <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white opacity-0 -translate-x-4 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300">
                <ArrowRight size={18} />
              </div>
            </a>
          {/each}
        </div>
      </div>
    </section>
    
    <!-- Fresh / New Arrivals Mini Banner -->
    <section class="relative overflow-hidden rounded-[2rem] border border-blue-500/30 bg-blue-900/10 cursor-pointer group">
      <div class="absolute inset-0 bg-gradient-to-r from-blue-600/20 to-transparent opacity-50"></div>
      <div class="absolute right-0 top-0 bottom-0 w-1/2 bg-[url('https://picsum.photos/seed/abstract/800/400')] bg-cover mix-blend-overlay opacity-30 group-hover:opacity-50 transition-opacity duration-1000"></div>
      
      <div class="relative p-10 md:p-16 flex items-center justify-between">
        <div class="max-w-xl">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-blue-400/30 bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-widest mb-6">
            <Clock size={14} /> Just Added
          </div>
          <h2 class="text-3xl md:text-5xl font-black mb-4">Discover the Latest Tools</h2>
          <p class="text-lg text-blue-200">Our ecosystem is growing every day. See what's freshly baked and join the beta programs before anyone else.</p>
        </div>
        <div class="hidden md:block">
          <div class="w-16 h-16 rounded-full bg-white flex items-center justify-center shadow-[0_0_40px_rgba(59,130,246,0.6)] group-hover:scale-110 transition-transform">
            <ArrowRight size={24} class="text-blue-600" />
          </div>
        </div>
      </div>
    </section>

  </div>
</div>

<style>
  .logo {
    background-color: rgb(122, 122, 122);
  }
</style>