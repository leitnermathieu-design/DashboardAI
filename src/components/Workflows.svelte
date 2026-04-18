<script lang="ts">
  import workflows from '../workflow.json';
  import { Workflow, Layers, PlayCircle } from 'lucide-svelte';
</script>

<div class="space-y-12 animate-in fade-in slide-in-from-bottom-4 duration-500">
  <div class="mb-12">
    <h1 class="text-4xl font-bold mb-4 flex items-center gap-3">
      <Workflow class="text-purple-500" size={36} />
      Creative Workflows
    </h1>
    <p class="text-gray-400 text-lg max-w-3xl">
      Discover unique multi-platform workflows to automate tasks and unleash your creativity.
    </p>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
    {#each workflows as workflow}
      <div class="bg-[#111] border border-white/10 rounded-2xl p-6 md:p-8 hover:border-white/20 transition-all group overflow-hidden relative flex flex-col">
        <!-- Decoration -->
        <div class="absolute -top-10 -right-10 w-40 h-40 bg-purple-500/10 blur-3xl rounded-full group-hover:bg-purple-500/20 transition-colors pointer-events-none"></div>

        <h2 class="text-2xl font-bold mb-2 relative z-10">{workflow.title}</h2>
        <p class="text-gray-400 mb-6 relative z-10 min-h-[3rem]">{workflow.description}</p>
        
        <div class="flex flex-wrap gap-2 mb-8 relative z-10">
          {#each workflow.tags as tag}
            <span class="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-xs font-medium text-purple-300">
              {tag}
            </span>
          {/each}
        </div>

        <div class="space-y-6 relative z-10 flex-grow">
          <h3 class="text-sm font-semibold text-gray-500 uppercase tracking-wider flex items-center gap-2">
            <Layers size={16} />
            Pipeline Steps
          </h3>
          <div class="space-y-0 relative before:content-[''] before:absolute before:left-[15px] before:top-2 before:bottom-2 before:w-[2px] before:bg-white/10">
            {#each workflow.steps as step, i}
              <div class="relative pl-10 pb-6 last:pb-0 group/step">
                <div class="absolute left-0 top-1 w-8 h-8 rounded-full bg-black border border-white/20 flex items-center justify-center -translate-x-[4px] z-10 group-hover/step:border-purple-500 group-hover/step:text-purple-500 transition-colors">
                  <span class="text-xs font-bold">{i + 1}</span>
                </div>
                <div>
                  <h4 class="font-bold text-white mb-1">{step.app}</h4>
                  <p class="text-sm text-gray-400 leading-relaxed">{step.action}</p>
                </div>
              </div>
            {/each}
          </div>
        </div>

        <div class="mt-8 pt-6 border-t border-white/10 relative z-10 flex gap-2">
           <button class="bg-white text-black hover:bg-gray-200 px-4 py-2 rounded-xl text-sm font-bold flex items-center gap-2 transition-colors cursor-pointer">
              <PlayCircle size={18} /> Run Workflow
           </button>
           <button class="bg-white/10 text-white hover:bg-white/20 px-4 py-2 rounded-xl text-sm font-semibold transition-colors cursor-pointer">
              Details
           </button>
        </div>
      </div>
    {/each}
  </div>
</div>
