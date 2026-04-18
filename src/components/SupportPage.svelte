<script lang="ts">
  import { Mail, Send, CheckCircle2 } from 'lucide-svelte';

  export let navigate: (path: string) => void;

  let name = '';
  let email = '';
  let subject = '';
  let message = '';
  
  let isSubmitting = false;
  let isSuccess = false;

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (!name || !email || !message) return;
    
    isSubmitting = true;
    
    // Call formsubmit.co to send actual email
    fetch("https://formsubmit.co/ajax/leitner.mathieu@gmail.com", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        name,
        email,
        subject,
        message,
        _subject: subject || "New Contact Form Submission - App Central"
      })
    })
    .then(response => response.json())
    .then(data => {
      isSubmitting = false;
      isSuccess = true;
      name = '';
      email = '';
      subject = '';
      message = '';
      
      // Reset success state after a few seconds
      setTimeout(() => {
        isSuccess = false;
      }, 5000);
    })
    .catch(error => {
      console.error(error);
      isSubmitting = false;
      alert("Something went wrong while sending your message. Please try again later.");
    });
  }
</script>

<div class="animate-in fade-in duration-700 py-12">
  <div class="max-w-3xl mx-auto space-y-12">
    
    <!-- Header -->
    <div class="text-center space-y-4">
      <div class="inline-flex items-center justify-center p-3 bg-white/5 rounded-2xl mb-4 border border-white/10">
        <Mail size={32} class="text-pink-400" />
      </div>
      <h1 class="text-5xl font-black tracking-tight">How can we help?</h1>
      <p class="text-xl text-gray-400 max-w-2xl mx-auto">We'd love to hear from you. Please fill out this form and we will get back to you as soon as possible.</p>
    </div>

    <!-- Contact Form -->
    <div class="relative">
      <div class="absolute -inset-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-[2rem] blur opacity-20"></div>
      <div class="relative bg-[#09090b] rounded-3xl border border-white/10 p-8 md:p-10 shadow-2xl">
        
        {#if isSuccess}
          <div class="absolute inset-0 z-10 bg-[#09090b]/80 backdrop-blur-sm rounded-3xl flex flex-col items-center justify-center p-8 text-center animate-in zoom-in duration-300">
            <div class="w-20 h-20 bg-green-500/20 rounded-full flex items-center justify-center mb-6">
              <CheckCircle2 size={40} class="text-green-500" />
            </div>
            <h3 class="text-3xl font-bold mb-4">Message Sent!</h3>
            <p class="text-lg text-gray-400">Thanks for reaching out. We'll get back to you as soon as possible.</p>
          </div>
        {/if}

        <form on:submit={handleSubmit} class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Name Input -->
            <div class="space-y-2">
              <label for="name" class="text-sm font-medium text-gray-300">First Name <span class="text-red-400">*</span></label>
              <input 
                type="text" 
                id="name" 
                bind:value={name} 
                required
                placeholder="John Doe"
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 transition-all"
              >
            </div>
            
            <!-- Email Input -->
            <div class="space-y-2">
              <label for="email" class="text-sm font-medium text-gray-300">Email Address <span class="text-red-400">*</span></label>
              <input 
                type="email" 
                id="email" 
                bind:value={email} 
                required
                placeholder="john@example.com"
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 transition-all"
              >
            </div>
          </div>

          <!-- Subject Input -->
          <div class="space-y-2">
            <label for="subject" class="text-sm font-medium text-gray-300">Subject</label>
            <input 
              type="text" 
              id="subject" 
              bind:value={subject} 
              placeholder="How can we help?"
              class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 transition-all"
            >
          </div>

          <!-- Message Input -->
          <div class="space-y-2">
            <label for="message" class="text-sm font-medium text-gray-300">Message <span class="text-red-400">*</span></label>
            <textarea 
              id="message" 
              bind:value={message} 
              required
              rows="5"
              placeholder="Leave us a message..."
              class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white placeholder:text-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500 transition-all resize-y"
            ></textarea>
          </div>

          <button 
            type="submit" 
            disabled={isSubmitting}
            class="w-full py-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white rounded-xl font-bold flex items-center justify-center gap-2 transition-all hover:shadow-[0_0_20px_rgba(168,85,247,0.4)] disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {#if isSubmitting}
              <div class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
              <span>Sending...</span>
            {:else}
              <span>Send Message</span>
              <Send size={18} />
            {/if}
          </button>
          <p class="text-xs text-center text-gray-500 mt-4">By submitting this form, you agree to our Terms of Service and Privacy Policy.</p>
        </form>
      </div>
    </div>
    
  </div>
</div>
