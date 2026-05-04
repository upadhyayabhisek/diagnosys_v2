<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20 pb-32"
  >
    <section
      class="pt-24 pb-12 px-6 max-w-6xl mx-auto flex flex-col md:flex-row md:items-end justify-between gap-6"
    >
      <div>
        <h1 class="text-4xl md:text-6xl font-bold tracking-tighter mb-4">
          Find Care Near You.
        </h1>
        <p class="text-[var(--subtext)] text-lg font-medium">
          Discover top-rated clinics specialized in nephrology, hepatology, and
          endocrinology.
        </p>
      </div>

      <!-- Minimalist Search -->
      <div class="relative w-full md:w-96">
        <input
          type="text"
          placeholder="Enter city or zip code..."
          class="w-full px-6 py-4 rounded-2xl bg-[var(--bg-secondary)] border border-[var(--border)] focus:outline-none focus:border-[var(--primary)] transition-colors"
        />
        <button
          class="absolute right-4 top-1/2 -translate-y-1/2 text-[var(--primary)] font-bold"
        >
          Search
        </button>
      </div>
    </section>

    <!-- Hospital Grid -->
    <section
      class="max-w-6xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-8"
    >
      <!-- Card 1 -->
      <div
        v-for="i in 6"
        :key="i"
        class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)] hover:shadow-2xl transition-all duration-300 group"
      >
        <div
          class="h-12 w-12 rounded-xl bg-blue-500/10 text-blue-500 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 10.5h.375c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125H21M4.5 10.5h6.75V15H4.5v-4.5zM3.75 18h15A2.25 2.25 0 0021 15.75v-6a2.25 2.25 0 00-2.25-2.25h-15A2.25 2.25 0 001.5 9.75v6A2.25 2.25 0 003.75 18z"
            />
          </svg>
        </div>
        <h3 class="text-xl font-bold mb-2">City Health Medical Center</h3>
        <p class="text-[var(--subtext)] text-sm mb-6">
          123 Health Ave, New York, NY
        </p>

        <div class="flex flex-wrap gap-2 mb-6">
          <span
            class="px-3 py-1 text-xs font-semibold rounded-lg bg-[var(--primary)]/10 text-[var(--primary)]"
            >Renal Care</span
          >
          <span
            class="px-3 py-1 text-xs font-semibold rounded-lg bg-orange-500/10 text-orange-500"
            >Diabetic Center</span
          >
        </div>

        <NuxtLink
          to="#"
          class="block w-full py-3 text-center text-sm font-bold bg-[var(--bg-secondary)] rounded-xl hover:bg-[var(--primary)] hover:text-white transition-colors"
        >
          View Details
        </NuxtLink>
      </div>
    </section>
  </div>
</template>
