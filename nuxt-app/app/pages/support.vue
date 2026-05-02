<template>
  <div class="min-h-screen bg-[var(--bg)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32">
    
    <section class="pt-32 pb-20 px-6 max-w-4xl mx-auto text-center">
      <h1 class="text-5xl md:text-7xl font-bold tracking-tighter mb-8">How can we help?</h1>
      
      <div class="relative max-w-2xl mx-auto">
        <div class="absolute inset-y-0 left-6 flex items-center pointer-events-none text-[var(--subtext)]">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
          </svg>
        </div>
        <input 
          type="text" 
          placeholder="Search for articles, guides, or FAQs..." 
          class="w-full pl-16 pr-6 py-5 text-lg rounded-full bg-[var(--card)] border border-[var(--border)] focus:outline-none focus:ring-2 focus:ring-[var(--primary)] shadow-xl shadow-black/5 transition-all"
        />
      </div>
    </section>

    <!-- Categories Grid -->
    <section class="max-w-5xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <NuxtLink to="#" class="bg-[var(--card)] rounded-[2rem] p-8 border border-[var(--border)] hover:-translate-y-2 hover:shadow-2xl transition-all duration-300">
        <div class="h-14 w-14 rounded-2xl bg-blue-500/10 text-blue-500 flex items-center justify-center mb-6">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-7 h-7"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" /></svg>
        </div>
        <h3 class="text-xl font-bold mb-2">Account Settings</h3>
        <p class="text-[var(--subtext)] text-sm">Manage your profile, password, and subscription preferences.</p>
      </NuxtLink>

      <NuxtLink to="#" class="bg-[var(--card)] rounded-[2rem] p-8 border border-[var(--border)] hover:-translate-y-2 hover:shadow-2xl transition-all duration-300">
        <div class="h-14 w-14 rounded-2xl bg-emerald-500/10 text-emerald-500 flex items-center justify-center mb-6">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-7 h-7"><path stroke-linecap="round" stroke-linejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" /></svg>
        </div>
        <h3 class="text-xl font-bold mb-2">Reading Graphs</h3>
        <p class="text-[var(--subtext)] text-sm">Learn how to interpret your personalized diabetes, liver, and kidney charts.</p>
      </NuxtLink>

      <NuxtLink to="#" class="bg-[var(--card)] rounded-[2rem] p-8 border border-[var(--border)] hover:-translate-y-2 hover:shadow-2xl transition-all duration-300">
        <div class="h-14 w-14 rounded-2xl bg-purple-500/10 text-purple-500 flex items-center justify-center mb-6">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-7 h-7"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
        </div>
        <h3 class="text-xl font-bold mb-2">Data Input Issues</h3>
        <p class="text-[var(--subtext)] text-sm">Troubleshooting errors when entering lab results or generating plans.</p>
      </NuxtLink>

    </section>

    <section class="max-w-5xl mx-auto px-6 mt-16">
      <div class="bg-[var(--bg-secondary)] rounded-[3rem] p-12 text-center flex flex-col items-center">
        <h3 class="text-2xl font-bold mb-4">Still need help?</h3>
        <p class="text-[var(--subtext)] mb-8">Our support team is available Monday through Friday, 9am - 5pm EST.</p>
        <button class="px-8 py-4 bg-[var(--primary)] text-white rounded-xl font-bold hover:opacity-90 transition-opacity">
          Contact Support
        </button>
      </div>
    </section>
  </div>
</template>