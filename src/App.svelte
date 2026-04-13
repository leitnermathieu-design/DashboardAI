<script lang="ts">
  import { Search, Bell, Grid } from 'lucide-svelte';
  import AppCard from './components/AppCard.svelte';
  import CategorySection from './components/CategorySection.svelte';

  import categories from './data.json';
</script>

<div class="min-h-screen bg-black text-white font-sans selection:bg-white/20">
  <!-- Navbar -->
  <nav class="flex items-center justify-between px-8 py-4 border-b border-white/10 bg-black/50 backdrop-blur-md sticky top-0 z-50">
    <div class="flex items-center gap-2">
      <div class="w-8 h-8 bg-white/10 rounded-lg flex items-center justify-center">
        <Grid size={20} class="text-white" />
      </div>
      <span class="font-bold tracking-tight text-lg uppercase">App Central</span>
    </div>

    <div class="hidden md:flex items-center gap-8 text-sm font-medium text-gray-400">
      <a href="/" class="text-white hover:text-white transition-colors">Home</a>
      <a href="/apps" class="hover:text-white transition-colors">Apps</a>
      <a href="/explore" class="hover:text-white transition-colors">Explore</a>
      <a href="/support" class="hover:text-white transition-colors">Support</a>
    </div>

    <div class="flex items-center gap-4">
      <button class="p-2 hover:bg-white/10 rounded-full transition-colors relative">
        <Bell size={20} />
        <span class="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-black"></span>
      </button>
      <div class="flex items-center gap-3 pl-4 border-l border-white/10">
        <span class="text-sm font-medium hidden sm:block">Sarah J.</span>
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-500 to-pink-500 border border-white/20 overflow-hidden">
          <img src="https://picsum.photos/seed/sarah/100/100" alt="Profile" class="w-full h-full object-cover" referrerPolicy="no-referrer" />
        </div>
      </div>
    </div>
  </nav>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-8 py-12">
    <!-- Search Bar -->
    <div class="max-w-2xl mx-auto mb-24">
      <div class="relative group">
        <div class="absolute inset-y-0 left-6 flex items-center pointer-events-none text-gray-500 group-focus-within:text-white transition-colors">
          <Search size={22} strokeWidth={1.5} />
        </div>
        <input 
          type="text" 
          placeholder="Search all apps, tools, or categories..." 
          class="w-full bg-[#1a1a1a] border border-white/5 rounded-full py-5 pl-16 pr-8 focus:outline-none focus:ring-2 focus:ring-white/10 focus:bg-[#222] transition-all text-lg placeholder:text-gray-500 shadow-2xl"
        />
      </div>
    </div>

    <!-- Categories -->
    <div class="space-y-24">
      {#each categories as category}
        <CategorySection title={category.name}>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
            {#each category.apps as app}
              <AppCard {...app} />
            {/each}
          </div>
        </CategorySection>
      {/each}
    </div>
  </main>
</div>

<style>
  :global(body) {
    background-color: black;
    margin: 0;
  }
</style>
