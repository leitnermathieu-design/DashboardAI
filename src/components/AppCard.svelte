<script lang="ts">
  import * as Icons from 'lucide-svelte';
  
  export let name: string;
  export let desc: string;
  export let icon: string;
  export let color: string = 'text-white';
  export let link: string;
  export let logo: string;

  // Map string icon name to Lucide component
  // const iconMap: Record<string, any> = {
  //   'mail': Icons.Mail,
  //   'hard-drive': Icons.HardDrive,
  //   'book': Icons.Book,
  //   'trello': Icons.Trello,
  //   'slack': Icons.Slack,
  //   'image': Icons.Image,
  //   'figma': Icons.Figma,
  //   'palette': Icons.Palette,
  //   'book-open': Icons.BookOpen,
  //   'music': Icons.Music,
  //   'youtube': Icons.Youtube,
  //   'github': Icons.Github,
  //   'code': Icons.Code,
  //   'triangle': Icons.Triangle,
  //   'terminal': Icons.Terminal,
  //   'cloud': Icons.Cloud,
  //   'video': Icons.Video,
  //   'users': Icons.Users,
  //   'message-square': Icons.MessageSquare,
  //   'message-circle': Icons.MessageCircle,
  // };

  // const IconComponent = iconMap[icon] || Icons.HelpCircle;
</script>

<a href="{link}" target="_blank" class="flex flex-col items-start p-5 bg-[#1a1a1a] border border-white/5 rounded-2xl hover:bg-[#252525] hover:border-white/10 transition-all group text-left w-full sm:aspect-auto">
  <div class="logo-container mb-6 p-3 bg-black/20 rounded-xl group-hover:scale-110 transition-transform duration-300">
    <!-- <svelte:component this={icon} size={24} class={color} strokeWidth={1.5} /> -->
    <img class="logo" height="48px" width="48px" src="{logo}" alt="">
  </div>
  <div class="mt-auto">
    <h3 class="font-medium text-[15px] leading-tight mb-1 group-hover:text-white transition-colors">{name}</h3>
    <p class="text-[13px] text-gray-400 leading-snug line-clamp-2 font-normal">{desc}</p>
  </div>
</a>


<style>
  .logo {
    
  }

  .logo-container {
    background: rgb(122, 122, 122); /* Subtle white tint */
    backdrop-filter: blur(5px); /* Softens the background */
    border-radius: 4px;
    padding: 8px; 
  }
</style>
