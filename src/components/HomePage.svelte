<script lang="ts">
  import { Grid, Zap, Layers, Sparkles, ArrowRight, Shield, Globe, Cpu } from 'lucide-svelte';

  export let navigate: (path: string) => void;

  const features = [
    {
      icon: Layers,
      title: 'Unified Ecosystem',
      description: 'Access all your favorite AI tools and creative platforms from a single, beautifully organized hub.',
      color: 'from-blue-500 to-cyan-400'
    },
    {
      icon: Zap,
      title: 'Seamless Workflows',
      description: 'Connect platforms together and automate your creative process with powerful predefined workflows.',
      color: 'from-purple-500 to-pink-500'
    },
    {
      icon: Shield,
      title: 'Privacy First',
      description: 'Your data, your rules. Enjoy a secure environment where your digital footprint is protected.',
      color: 'from-emerald-500 to-teal-400'
    }
  ];
</script>

<div class="flex flex-col animate-in fade-in duration-700">
  <!-- Hero Section -->
  <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden">
    <!-- Abstract background elements -->
    <div class="absolute inset-0 z-0">
      <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-purple-600/20 rounded-full blur-[120px] mix-blend-screen"></div>
      <div class="absolute bottom-1/4 right-1/4 w-[600px] h-[600px] bg-blue-600/20 rounded-full blur-[150px] mix-blend-screen"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-pink-500/10 rounded-full blur-[100px]"></div>
      
      <!-- Grid pattern -->
      <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNTQgNjBIMTBWMGg0NHY2MHptLTQwLTJIMTJWNGg0MHY1NHoiIGZpbGw9InJnYmEoMjU1LCAyNTUsIDI1NSwgMC4wNSkiIGZpbGwtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==')] opacity-20"></div>
    </div>

    <div class="relative z-10 max-w-5xl mx-auto px-6 text-center">
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full mb-8 border border-white/10 bg-white/5 backdrop-blur-md text-sm font-medium animate-in slide-in-from-bottom-8 duration-700 delay-100">
        <Sparkles size={16} class="text-pink-400" />
        <span class="text-gray-300">The Next Generation App Experience</span>
      </div>
      
      <h1 class="text-6xl md:text-8xl font-black mb-8 tracking-tighter leading-tight animate-in slide-in-from-bottom-8 duration-700 delay-200">
        Your Gateway to <br />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400">Infinite Creation</span>
      </h1>
      
      <p class="text-xl md:text-2xl text-gray-400 mb-12 max-w-3xl mx-auto font-light leading-relaxed animate-in slide-in-from-bottom-8 duration-700 delay-300">
        App Central transcends traditional boundaries, orchestrating the best AI tools and platforms into one seamless, elegant symphony of productivity.
      </p>
      
      <div class="flex flex-col sm:flex-row gap-6 justify-center items-center animate-in slide-in-from-bottom-8 duration-700 delay-400">
        <button 
          on:click={() => navigate('/apps')} 
          class="group relative px-8 py-4 bg-white text-black rounded-2xl font-bold text-lg transition-all hover:scale-105 hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex items-center gap-3 overflow-hidden"
        >
          <span class="relative z-10">Discover Apps</span>
          <ArrowRight size={20} class="relative z-10 group-hover:translate-x-1 transition-transform" />
        </button>
        
        <button 
          on:click={() => navigate('/workflows')} 
          class="px-8 py-4 bg-white/5 border border-white/10 text-white rounded-2xl font-semibold text-lg transition-all hover:bg-white/10 hover:border-white/20 backdrop-blur-md flex items-center gap-3"
        >
          <Cpu size={20} class="text-gray-400" />
          <span>Explore Workflows</span>
        </button>
      </div>
    </div>
  </section>

  <!-- Value Proposition / Storytelling -->
  <section class="py-32 px-6 relative border-t border-white/5 bg-gradient-to-b from-black to-zinc-950">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-24">
        <h2 class="text-4xl md:text-6xl font-bold mb-6 tracking-tight">Crafted for the Visionaries.</h2>
        <p class="text-xl text-gray-400 max-w-3xl mx-auto">
          We built App Central because scattered tools break creative flow. Now, you can transition gracefully from idea generation to execution without ever losing momentum.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        {#each features as feature, i}
          <div class="group p-8 rounded-3xl bg-white/[0.02] border border-white/5 hover:bg-white/[0.04] transition-all hover:-translate-y-2 hover:border-white/10 backdrop-blur-sm relative overflow-hidden">
            <div class={`absolute top-0 right-0 w-32 h-32 bg-gradient-to-br ${feature.color} opacity-20 blur-3xl rounded-full group-hover:opacity-40 transition-opacity`}></div>
            
            <div class={`w-14 h-14 rounded-2xl mb-6 flex items-center justify-center bg-gradient-to-br ${feature.color} bg-opacity-10 backdrop-blur-md border border-white/10`}>
              <svelte:component this={feature.icon} size={28} class="text-white" />
            </div>
            
            <h3 class="text-2xl font-bold mb-4 text-gray-100">{feature.title}</h3>
            <p class="text-gray-400 leading-relaxed group-hover:text-gray-300 transition-colors">
              {feature.description}
            </p>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Showcase Section -->
  <section class="py-32 px-6 overflow-hidden bg-black border-y border-white/5">
    <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-16">
      <div class="flex-1 space-y-8 z-10 w-full lg:w-1/2">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-purple-500/30 bg-purple-500/10 text-purple-300 text-sm font-semibold">
          <Globe size={16} /> Transform Your Process
        </div>
        <h2 class="text-4xl md:text-5xl font-bold leading-tight">
          Everything works <br /> together, <span class="italic text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500">beautifully.</span>
        </h2>
        <p class="text-xl text-gray-400">
          Gone are the days of juggling dozens of tabs. App Central's intuitive directory and powerful search puts the entire universe of next-gen software right at your fingertips.
        </p>
        <div class="pt-4">
          <button on:click={() => navigate('/apps')} class="text-white font-semibold flex items-center gap-2 hover:gap-4 transition-all">
            See the showcase <ArrowRight size={20} class="text-pink-400" />
          </button>
        </div>
      </div>
      
      <!-- Visual Element -->
      <div class="flex-1 relative w-full lg:w-1/2 h-[400px]">
        <div class="absolute inset-0 bg-gradient-to-tr from-purple-900/40 to-blue-900/40 rounded-3xl blur-[80px]"></div>
        <div class="absolute inset-0 bg-white/5 backdrop-blur-md rounded-3xl border border-white/10 p-6 shadow-2xl flex flex-col gap-4 transform rotate-2 hover:rotate-0 transition-transform duration-700">
          <!-- Mockup UI -->
          <div class="flex gap-2 items-center mb-2">
            <div class="w-3 h-3 rounded-full bg-red-400/80"></div>
            <div class="w-3 h-3 rounded-full bg-yellow-400/80"></div>
            <div class="w-3 h-3 rounded-full bg-green-400/80"></div>
          </div>
          <div class="h-10 w-full bg-white/5 border border-white/10 rounded-xl flex items-center px-4">
            <div class="w-4 h-4 rounded-full bg-gray-500/50 mr-3"></div>
            <div class="h-2 w-32 bg-gray-600/50 rounded-full"></div>
          </div>
          <div class="flex-1 bg-black/40 rounded-xl border border-white/5 p-4 flex gap-4">
            <div class="w-1/3 flex flex-col gap-3">
              <div class="h-24 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-lg border border-white/5 p-3 flex flex-col justify-end">
                <div class="h-2 w-16 bg-white/40 rounded-full mb-2"></div>
                <div class="h-1 w-24 bg-white/20 rounded-full"></div>
              </div>
              <div class="h-24 bg-gradient-to-br from-pink-500/20 to-red-500/20 rounded-lg border border-white/5 p-3 flex flex-col justify-end">
                <div class="h-2 w-12 bg-white/40 rounded-full mb-2"></div>
                <div class="h-1 w-20 bg-white/20 rounded-full"></div>
              </div>
            </div>
            <div class="w-2/3 bg-white/5 rounded-lg border border-white/5 p-4 flex flex-col gap-3">
              <div class="w-full h-32 bg-white/5 rounded-md mb-2"></div>
              <div class="w-3/4 h-2 bg-white/20 rounded-full"></div>
              <div class="w-1/2 h-2 bg-white/20 rounded-full"></div>
              <div class="w-5/6 h-2 bg-white/20 rounded-full"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <!-- CTA Section -->
  <section class="py-32 px-6 bg-black relative">
    <div class="absolute inset-0 bg-gradient-to-t from-blue-900/20 to-transparent"></div>
    <div class="max-w-4xl mx-auto text-center relative z-10">
      <h2 class="text-5xl font-black mb-8">Ready to Elevate Your Workflow?</h2>
      <p class="text-xl text-gray-400 mb-12">Join thousands of creators who have already unified their digital workspace with App Central.</p>
      <button on:click={() => navigate('/apps')} class="px-10 py-5 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full font-bold text-lg hover:shadow-[0_0_30px_rgba(139,92,246,0.5)] transition-all hover:-translate-y-1">
        Enter App Central
      </button>
    </div>
  </section>
  
  <footer class="py-12 border-t border-white/10 text-center text-gray-500 text-sm">
    <p>© 2026 App Central / Mathieu Leitner Design. All rights reserved.</p>
    <p class="mt-2 text-gray-600">Built for the future of creativity.</p>
  </footer>
</div>

<style>
  /* Custom animations and utilities can go here if needed */
</style>
