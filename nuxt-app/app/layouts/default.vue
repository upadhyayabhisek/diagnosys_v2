<template>
  <div
    class="min-h-screen bg-[var(--bg)] text-[var(--text)] font-sans selection:bg-[var(--primary)]/30 transition-colors duration-300"
  >
    <Navbar />
    <main class="container mx-auto px-6">
      <slot />
    </main>

    <ChatWidget />
    <Footer />
  </div>
</template>
