<script lang="ts">
  import { fade, fly } from 'svelte/transition';
  import { Search, Copy, Check } from 'lucide-svelte';
  import categories from '../data.json';

  export let navigate: (path: string) => void;

  let searchTerm = '';
  let copiedPrompt: string | null = null;
  
  // Flatten apps and their prompts
  $: allPrompts = categories.flatMap(category => 
    category.apps.flatMap(app => 
      app.prompts ? app.prompts.map((prompt: string) => ({
        app: app.name,
        category: category.name,
        logo: app.logo,
        text: prompt
      })) : []
    )
  );

  $: filteredPrompts = allPrompts.filter(p => 
    p.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
    p.app.toLowerCase().includes(searchTerm.toLowerCase())
  );

  function copyPrompt(text: string) {
    navigator.clipboard.writeText(text);
    copiedPrompt = text;
    setTimeout(() => {
      if (copiedPrompt === text) copiedPrompt = null;
    }, 2000);
  }
</script>

<div in:fade={{ duration: 300 }} class="max-w-7xl mx-auto px-4 sm:px-8 py-8 sm:py-12 w-full">
  <div class="mb-10 text-center">
    <h1 class="text-4xl sm:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500 mb-4 tracking-tight">
      Bibliothèque de Prompts
    </h1>
    <p class="text-gray-400 text-lg sm:text-xl max-w-2xl mx-auto text-balance">
      Découvrez des prompts optimisés pour vos applications d'IA préférées.
    </p>
  </div>

  <!-- Search -->
  <div class="relative max-w-2xl mx-auto mb-12">
    <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-gray-500">
      <Search size={22} />
    </div>
    <input 
      type="text" 
      bind:value={searchTerm}
      placeholder="Rechercher un prompt, une application..." 
      class="w-full pl-12 pr-4 py-4 rounded-2xl bg-white/5 border border-white/10 text-white focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:bg-white/10 transition-all text-lg backdrop-blur-md placeholder:text-gray-500"
    >
  </div>

  <!-- Prompts Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each filteredPrompts as prompt, idx (idx)}
      <div 
        in:fly={{ y: 20, duration: 400, delay: Math.min(idx * 50, 500) }}
        class="bg-[#1a1a1a] border border-white/5 rounded-2xl p-6 hover:bg-[#252525] hover:border-white/10 transition-all group flex flex-col h-full relative overflow-hidden"
      >
        <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-blue-500/5 to-purple-500/5 rounded-full blur-2xl -mr-16 -mt-16 transition-opacity group-hover:opacity-100 opacity-50"></div>
        
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 bg-black/30 rounded-xl max-h-[44px]">
             <img src={prompt.logo} alt={prompt.app} class="w-6 h-6 object-contain" />
          </div>
          <div>
            <h3 class="font-semibold text-white/90">{prompt.app}</h3>
            <span class="text-xs text-blue-400/80 font-medium tracking-wide uppercase">{prompt.category}</span>
          </div>
        </div>
        
        <p class="text-gray-300 text-sm leading-relaxed flex-grow mb-6 whitespace-pre-wrap">{prompt.text}</p>
        
        <button 
          on:click={() => copyPrompt(prompt.text)}
          class="mt-auto flex items-center justify-center gap-2 w-full py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/5 transition-colors text-sm font-medium cursor-pointer"
        >
          {#if copiedPrompt === prompt.text}
            <Check size={16} class="text-green-400" />
            <span class="text-green-400">Copié !</span>
          {:else}
            <Copy size={16} class="text-gray-400 group-hover:text-white transition-colors" />
            <span class="text-gray-400 group-hover:text-white transition-colors">Copier le prompt</span>
          {/if}
        </button>
      </div>
    {/each}
  </div>

  {#if filteredPrompts.length === 0}
    <div class="text-center text-gray-500 py-24">
      <p class="text-xl">Aucun prompt ne correspond à "{searchTerm}"</p>
    </div>
  {/if}
</div>

<style>
</style>
