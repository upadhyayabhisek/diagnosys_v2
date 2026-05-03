<template>
  <div
    class="min-h-screen bg-[var(--bg)] font-sans text-[var(--text)] selection:bg-red-500/20 pb-32"
  >
    <!-- Urgent Hero Banner -->
    <section class="pt-32 pb-12 px-6 max-w-4xl mx-auto">
      <div
        class="bg-red-500 rounded-[3rem] p-12 md:p-20 text-center shadow-2xl shadow-red-500/20 relative overflow-hidden"
      >
        <div class="relative z-10">
          <div
            class="h-16 w-16 mx-auto rounded-full bg-white/20 flex items-center justify-center text-white mb-8 backdrop-blur-sm"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="2.5"
              stroke="currentColor"
              class="w-8 h-8"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
              />
            </svg>
          </div>
          <h1
            class="text-3xl md:text-5xl font-black text-white tracking-tight mb-6"
          >
            Immediate Medical Assistance in Nepal
          </h1>
          <p class="text-white/90 text-lg font-medium max-w-2xl mx-auto">
            MediAI is an analytical tool for chronic health tracking. It is
            <strong>not</strong> a diagnostic service for acute emergencies. If
            you are in distress, please use the contacts below.
          </p>
        </div>
      </div>
    </section>

    <section class="max-w-4xl mx-auto px-6 space-y-6">
      <div
        class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)] flex items-start gap-6 hover:border-red-500/50 transition-colors"
      >
        <div class="text-red-500 shrink-0">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-8 h-8"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
            />
          </svg>
        </div>
        <div class="flex-1">
          <h3 class="text-xl font-bold mb-1">
            Ambulance (Nepal Ambulance Service)
          </h3>
          <p class="text-[var(--subtext)] mb-4">
            Dedicated 24/7 emergency medical response across major cities.
          </p>
          <a
            href="tel:102"
            class="inline-flex items-center gap-2 px-6 py-3 bg-red-500 text-white rounded-xl font-bold hover:scale-105 transition-transform"
          >
            <span>Dial 102</span>
          </a>
        </div>
      </div>

      <div
        class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)] flex items-start gap-6"
      >
        <div class="text-blue-500 shrink-0">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-8 h-8"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751A11.959 11.959 0 0112 2.714z"
            />
          </svg>
        </div>
        <div class="flex-1">
          <h3 class="text-xl font-bold mb-1">Nepal Police (Emergency)</h3>
          <p class="text-[var(--subtext)] mb-4">
            Contact for accidents, public safety issues, or immediate rescue
            needs.
          </p>
          <a
            href="tel:100"
            class="inline-flex items-center gap-2 px-6 py-3 bg-[var(--bg-secondary)] text-[var(--text)] rounded-xl font-bold hover:bg-blue-500 hover:text-white transition-all"
          >
            <span>Dial 100</span>
          </a>
        </div>
      </div>

      <div
        class="bg-[var(--card)] rounded-3xl p-8 border border-[var(--border)]"
      >
        <h3 class="text-xl font-bold mb-4">Major Emergency Centers</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 rounded-2xl bg-[var(--bg-secondary)]">
            <p class="font-bold text-sm">
              Tribhuvan University Teaching Hospital
            </p>
            <p class="text-xs text-[var(--subtext)]">Maharajgunj, Kathmandu</p>
          </div>
          <div class="p-4 rounded-2xl bg-[var(--bg-secondary)]">
            <p class="font-bold text-sm">Patan Hospital</p>
            <p class="text-xs text-[var(--subtext)]">Lagankhel, Lalitpur</p>
          </div>
          <div class="p-4 rounded-2xl bg-[var(--bg-secondary)]">
            <p class="font-bold text-sm">Bir Hospital</p>
            <p class="text-xs text-[var(--subtext)]">Kantipath, Kathmandu</p>
          </div>
          <div class="p-4 rounded-2xl bg-[var(--bg-secondary)]">
            <p class="font-bold text-sm">Mediciti Hospital</p>
            <p class="text-xs text-[var(--subtext)]">Bhaisepati, Lalitpur</p>
          </div>
        </div>
      </div>

      <div
        class="p-6 rounded-[2rem] border border-yellow-500/20 bg-yellow-500/5"
      >
        <p class="text-xs text-[var(--subtext)] leading-relaxed italic">
          Disclaimer: MediAI is a technology platform. We do not provide
          ambulance services ourselves. The numbers provided above are the
          public emergency response lines of the Government of Nepal and
          non-profit organizations.
        </p>
      </div>
    </section>
  </div>
</template>
