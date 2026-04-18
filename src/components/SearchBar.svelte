<script lang="ts">
  import { Search } from 'lucide-svelte';
  export let searchTerm = '';
</script>

<div class="max-w-2xl mx-auto mb-24">
  <div class="relative group">
    <div class="absolute inset-y-0 left-6 flex items-center pointer-events-none text-gray-500 group-focus-within:text-white transition-colors">
      <Search size={22} strokeWidth={1.5} />
    </div>
    <input 
      bind:value={searchTerm}
      type="text" 
      placeholder="Search all apps, tools, or categories..." 
      class="w-full bg-[#1a1a1a] border border-white/5 rounded-full py-5 pl-16 pr-8 focus:outline-none focus:ring-2 focus:ring-white/10 focus:bg-[#222] transition-all text-lg placeholder:text-gray-500 shadow-2xl"
    />
  </div>
</div>
