<script lang="ts">
  import { onMount } from 'svelte';
  import { Bell, Grid, Menu, X } from 'lucide-svelte';
  import { fly, fade } from 'svelte/transition';
  import AppCard from './components/AppCard.svelte';
  import CategorySection from './components/CategorySection.svelte';
  import SearchBar from './components/SearchBar.svelte';
  import Workflows from './components/Workflows.svelte';
  import HomePage from './components/HomePage.svelte';
  import ExplorePage from './components/ExplorePage.svelte';
  import SupportPage from './components/SupportPage.svelte';
  import ProfilePage from './components/ProfilePage.svelte';
  import PromptsPage from './components/PromptsPage.svelte';
  import categories from './data.json';

  let searchTerm = '';
  let isMobileMenuOpen = false;

  $: filteredCategories = categories.map(category => {
    return {
      ...category,
      apps: category.apps.filter(app => 
        (app.name && app.name.toLowerCase().includes(searchTerm.toLowerCase())) ||
        (app.desc && app.desc.toLowerCase().includes(searchTerm.toLowerCase())) ||
        (category.name && category.name.toLowerCase().includes(searchTerm.toLowerCase()))
      )
    };
  }).filter(category => category.apps.length > 0);

  let currentPath = '/';

  onMount(() => {
    currentPath = window.location.pathname;
    window.addEventListener('popstate', () => {
      currentPath = window.location.pathname;
    });
  });

  function navigate(path: string) {
    window.history.pushState({}, '', path);
    currentPath = path;
    isMobileMenuOpen = false;
  }
</script>

<div class="min-h-screen bg-black text-white font-sans selection:bg-white/20 flex flex-col relative">
  <!-- Navbar -->
  <nav class="flex items-center justify-between px-4 sm:px-8 py-4 border-b border-white/10 bg-black/50 backdrop-blur-md sticky top-0 z-50">
    <div class="flex items-center gap-2 sm:gap-3">
      <button class="md:hidden p-1.5 -ml-1.5 text-gray-400 hover:text-white transition-colors cursor-pointer" on:click={() => isMobileMenuOpen = true}>
        <Menu size={24} />
      </button>

      <a href="/" on:click|preventDefault={() => navigate('/')} class="flex items-center gap-2 cursor-pointer absolute left-1/2 -translate-x-1/2 md:static md:translate-x-0 z-10">
        <div class="w-8 h-8 bg-white/10 rounded-lg flex items-center justify-center shrink-0">
          <Grid size={20} class="text-white" />
        </div>
        <span class="font-bold tracking-tight text-base md:text-lg uppercase max-[350px]:hidden">App Central</span>
      </a>
    </div>

    <!-- Desktop Navigation -->
    <div class="hidden md:flex items-center gap-8 text-sm font-medium text-gray-400">
      <a href="/" on:click|preventDefault={() => navigate('/')} class="{currentPath === '/' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Home</a>
      <a href="/workflows" on:click|preventDefault={() => navigate('/workflows')} class="{currentPath === '/workflows' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Workflows</a>
      <a href="/apps" on:click|preventDefault={() => navigate('/apps')} class="{currentPath === '/apps' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Apps</a>
      <a href="/prompts" on:click|preventDefault={() => navigate('/prompts')} class="{currentPath === '/prompts' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Prompts</a>
      <a href="/explore" on:click|preventDefault={() => navigate('/explore')} class="{currentPath === '/explore' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Explore</a>
      <a href="/support" on:click|preventDefault={() => navigate('/support')} class="{currentPath === '/support' ? 'text-white' : 'hover:text-white'} transition-colors cursor-pointer">Support</a>
    </div>

    <div class="flex items-center gap-2 sm:gap-4">
      <button class="p-2 hover:bg-white/10 rounded-full transition-colors relative cursor-pointer hidden sm:block">
        <Bell size={20} />
        <span class="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-black"></span>
      </button>
      <button class="flex items-center gap-2 sm:gap-3 sm:pl-4 sm:border-l border-white/10 hover:opacity-80 transition-opacity cursor-pointer text-left" on:click={() => navigate('/profile')}>
        <span class="text-sm font-medium hidden sm:block">Mathieu L.</span>
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-500 to-pink-500 border border-white/20 overflow-hidden shrink-0">
          <img src="https://picsum.photos/seed/sarah/100/100" alt="Profile" class="w-full h-full object-cover" referrerPolicy="no-referrer" />
        </div>
      </button>
    </div>

  </nav>

  <!-- Mobile Drawer Menu -->
  {#if isMobileMenuOpen}
    <div class="md:hidden fixed inset-0 z-[100] flex">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div 
        transition:fade={{ duration: 200 }} 
        class="absolute inset-0 bg-black/60 backdrop-blur-sm" 
        on:click={() => isMobileMenuOpen = false}>
      </div>

      <div 
        transition:fly={{ x: -300, duration: 300 }} 
        class="relative w-3/4 max-w-[300px] h-full bg-zinc-950 border-r border-white/10 shadow-2xl flex flex-col">
        
        <div class="flex items-center justify-between p-4 border-b border-white/10">
          <button class="p-2 -mr-2 text-gray-400 hover:text-white transition-colors cursor-pointer" on:click={() => isMobileMenuOpen = false}>
            <X size={24} />
          </button>
           <div class="flex items-center gap-2">
            <div class="w-8 h-8 bg-white/10 rounded-lg flex items-center justify-center shrink-0">
              <Grid size={20} class="text-white" />
            </div>
            <span class="font-bold tracking-tight text-lg uppercase text-white">App Central</span>
          </div>
        </div>

        <div class="flex flex-col py-4 px-3 gap-2 text-lg font-medium text-gray-400 overflow-y-auto">
          <button on:click={() => navigate('/')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Home
          </button>
          <button on:click={() => navigate('/workflows')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/workflows' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Workflows
          </button>
          <button on:click={() => navigate('/apps')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/apps' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Apps
          </button>
          <button on:click={() => navigate('/prompts')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/prompts' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Prompts
          </button>
          <button on:click={() => navigate('/explore')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/explore' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Explore
          </button>
          <button on:click={() => navigate('/support')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/support' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Support
          </button>
          <div class="h-px w-full bg-white/10 my-2"></div>
          <button on:click={() => navigate('/profile')} class="text-left px-4 py-3 rounded-xl transition-colors {currentPath === '/profile' ? 'text-white bg-white/5' : 'hover:bg-white/5 hover:text-white'}">
            Profile
          </button>
        </div>
      </div>
    </div>
  {/if}

  <!-- Main Content -->
  {#if currentPath === '/'}
    <HomePage {navigate} />
  {:else if currentPath === '/explore'}
    <ExplorePage {navigate} />
  {:else if currentPath === '/support'}
    <SupportPage {navigate} />
  {:else if currentPath === '/profile'}
    <ProfilePage {navigate} />
  {:else if currentPath === '/prompts'}
    <PromptsPage {navigate} />
  {:else}
    <main class="max-w-7xl mx-auto px-4 sm:px-8 py-8 sm:py-12 w-full">
      {#if currentPath === '/apps'}
        <!-- Search Bar -->
        <SearchBar bind:searchTerm />

        <!-- Categories -->
        <div class="space-y-24">
          {#if filteredCategories.length > 0}
            {#each filteredCategories as category}
              <CategorySection title={category.name}>
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-3 sm:gap-4">
                  {#each category.apps as app}
                    <AppCard {...app} />
                  {/each}
                </div>
              </CategorySection>
            {/each}
          {:else}
            <div class="text-center text-gray-500 py-12">
              No apps found matching "{searchTerm}"
            </div>
          {/if}
        </div>
      {:else if currentPath === '/workflows'}
        <Workflows />
      {/if}
    </main>
  {/if}
</div>

<style>
  :global(body) {
    background-color: black;
    margin: 0;
  }
</style>
