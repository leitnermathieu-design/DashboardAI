<script lang="ts">
  export let title: string;
</script>

<section>
  <h2 class="text-xs font-bold tracking-[0.2em] text-gray-500 mb-6 uppercase">{title}</h2>
  <slot />
</section>
