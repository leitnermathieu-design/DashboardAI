<script lang="ts">
  import { User, Settings, CreditCard, Bell, Shield, LogOut, ChevronRight, Zap, Boxes } from 'lucide-svelte';

  export let navigate: (path: string) => void;

  const user = {
    name: 'Mathieu L.',
    email: 'mathieu.design@example.com',
    plan: 'Pro Ecosystem',
    memberSince: 'December 2023',
    avatar: 'https://picsum.photos/seed/sarah/200/200'
  };

  const sections = [
    { title: 'Account Settings', icon: User, desc: 'Manage your personal information and profile visibility' },
    { title: 'Billing & Plan', icon: CreditCard, desc: 'View your current subscription and payment history' },
    { title: 'Notifications', icon: Bell, desc: 'Configure email digests and push alerts for workflows' },
    { title: 'Security', icon: Shield, desc: 'Update password, set up 2FA and view active sessions' },
    { title: 'App Preferences', icon: Settings, desc: 'Customize your layout, themes, and dashboard experience' }
  ];
</script>

<div class="flex flex-col animate-in fade-in duration-500 w-full z-0 relative">
  <!-- Profile Header -->
  <div class="relative w-full overflow-hidden border-b border-white/5 flex flex-col justify-end min-h-[380px] md:min-h-[400px] shrink-0 pt-10">
    <div class="absolute inset-0 bg-gradient-to-br from-purple-900/60 via-black to-blue-900/40 z-0"></div>
    <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-pink-500/10 rounded-full blur-[120px] mix-blend-screen translate-x-1/3 -translate-y-1/3 z-0"></div>
    <!-- glass layer -->
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNTQgNjBIMTBWMGg0NHY2MHptLTQwLTJIMTJWNGg0MHY1NHoiIGZpbGw9InJnYmEoMjU1LCAyNTUsIDI1NSwgMC4wNSkiIGZpbGwtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==')] opacity-10 mix-blend-overlay z-0"></div>
    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent z-10"></div>
    
    <div class="relative z-20 w-full px-6 sm:px-12 pb-10 flex flex-col sm:flex-row items-center sm:items-end gap-6 sm:gap-8 text-center sm:text-left">
      <div class="w-32 h-32 md:w-44 md:h-44 rounded-full border-4 border-black overflow-hidden shadow-[0_0_40px_rgba(0,0,0,0.5)] relative group bg-gradient-to-br from-purple-500 to-pink-500 shrink-0">
        <img src={user.avatar} alt="Profile" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
        <div class="absolute inset-0 bg-black/50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 cursor-pointer backdrop-blur-sm">
          <User class="text-white" size={32} />
        </div>
      </div>
      <div class="mb-2 sm:mb-4">
        <h1 class="text-4xl md:text-6xl font-black bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400 mb-2 tracking-tighter">{user.name}</h1>
        <p class="text-lg md:text-xl text-gray-400 font-light flex items-center justify-center sm:justify-start gap-2">
          {user.email}
        </p>
      </div>
      <div class="mt-2 sm:mt-0 sm:mb-4 sm:ml-auto flex items-center gap-3">
        <div class="px-5 py-2.5 rounded-full border border-purple-500/30 bg-purple-500/10 backdrop-blur-md text-purple-300 font-semibold flex items-center gap-2 shadow-[0_0_20px_rgba(168,85,247,0.15)]">
          <Zap size={18} class="text-purple-400" />
          {user.plan}
        </div>
      </div>
    </div>
  </div>

  <main class="max-w-7xl mx-auto px-6 sm:px-12 py-16 w-full grid grid-cols-1 lg:grid-cols-3 gap-12 z-20 relative">
    <!-- Left Column: Stats & Actions -->
    <div class="flex flex-col gap-8 lg:col-span-1 transform -translate-y-4">
      <div class="bg-white/[0.02] border border-white/5 rounded-3xl p-6 md:p-8 backdrop-blur-xl shadow-2xl relative overflow-hidden group hover:border-white/10 transition-colors duration-500">
        <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 blur-3xl rounded-full group-hover:bg-blue-500/20 transition-colors duration-500"></div>

        <h3 class="text-xl font-bold text-white mb-8">Overview</h3>
        <div class="grid grid-cols-2 gap-4">
          <div class="bg-black/40 border border-white/5 rounded-2xl p-5 flex flex-col items-center justify-center text-center transition-all hover:bg-black/60 hover:scale-[1.02]">
            <div class="w-12 h-12 rounded-full bg-blue-500/10 flex items-center justify-center mb-3">
              <Boxes size={22} class="text-blue-400" />
            </div>
            <span class="text-3xl font-black text-white mb-1">42</span>
            <span class="text-xs text-gray-500 uppercase font-bold tracking-widest">Apps Used</span>
          </div>
          <div class="bg-black/40 border border-white/5 rounded-2xl p-5 flex flex-col items-center justify-center text-center transition-all hover:bg-black/60 hover:scale-[1.02]">
            <div class="w-12 h-12 rounded-full bg-pink-500/10 flex items-center justify-center mb-3">
              <Zap size={22} class="text-pink-400" />
            </div>
            <span class="text-3xl font-black text-white mb-1">12</span>
            <span class="text-xs text-gray-500 uppercase font-bold tracking-widest">Workflows</span>
          </div>
        </div>
        <div class="mt-8 pt-6 border-t border-white/5">
          <div class="flex justify-between items-center bg-black/20 rounded-xl p-4 border border-white/[0.02]">
            <span class="text-sm text-gray-400">Member since</span>
            <span class="text-white font-semibold text-sm">{user.memberSince}</span>
          </div>
        </div>
      </div>

      <button class="w-full flex items-center justify-center gap-2 py-4 px-6 rounded-2xl border border-red-500/20 bg-red-500/5 hover:bg-red-500/15 hover:border-red-500/40 text-red-400 font-bold transition-all shadow-[0_0_20px_rgba(239,68,68,0)] hover:shadow-[0_0_20px_rgba(239,68,68,0.1)]">
        <LogOut size={20} />
        Sign Out Securely
      </button>
    </div>

    <!-- Right Column: Settings Sections -->
    <div class="lg:col-span-2 flex flex-col gap-4">
      <h2 class="text-2xl font-bold text-white mb-2 pl-2">Settings & Preferences</h2>
      {#each sections as section}
        <button class="group bg-white/[0.02] border border-white/5 hover:border-white/10 hover:bg-white/[0.04] rounded-2xl p-5 sm:p-6 flex items-center gap-6 transition-all duration-300 text-left hover:shadow-[0_4px_20px_rgba(0,0,0,0.5)]">
          <div class="w-14 h-14 rounded-2xl bg-black/50 border border-white/5 flex items-center justify-center shrink-0 group-hover:scale-105 group-hover:bg-gradient-to-br group-hover:from-purple-500/20 group-hover:to-blue-500/20 group-hover:text-white transition-all text-gray-400 shadow-inner">
            <svelte:component this={section.icon} size={26} />
          </div>
          <div class="flex-grow">
            <h3 class="text-lg md:text-xl font-semibold text-white mb-1 group-hover:text-purple-300 transition-colors">{section.title}</h3>
            <p class="text-sm md:text-base text-gray-400 leading-relaxed max-w-md">{section.desc}</p>
          </div>
          <div class="text-gray-600 group-hover:text-white group-hover:translate-x-2 transition-all">
            <ChevronRight size={24} />
          </div>
        </button>
      {/each}
    </div>
  </main>
</div>
