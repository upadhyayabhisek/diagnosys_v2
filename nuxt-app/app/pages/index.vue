<template>
  <div
    class="min-h-screen bg-[var(--background)] font-sans text-[var(--text)] selection:bg-[var(--primary)]/20"
  >
    <!-- Hero Section (Apple-style minimalism) -->
    <section
      class="relative pt-32 pb-32 px-6 overflow-hidden flex flex-col items-center justify-center min-h-[90vh]"
    >
      <!-- Soft Ambient Glow -->
      <div
        class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-to-tr from-[var(--primary)]/10 to-transparent rounded-full blur-[100px] -z-10 opacity-70 pointer-events-none"
      ></div>

      <div class="max-w-5xl mx-auto text-center flex flex-col items-center">
        <!-- Pill Badge -->
        <div
          class="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-[var(--bg-secondary)] text-[var(--primary)] text-sm font-semibold tracking-wide mb-12 shadow-sm"
        >
          <span class="relative flex h-2.5 w-2.5">
            <span
              class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[var(--primary)] opacity-60"
            ></span>
            <span
              class="relative inline-flex rounded-full h-2.5 w-2.5 bg-[var(--primary)]"
            ></span>
          </span>
          {{ $t("home.hero.badge") }}
        </div>

        <!-- Huge, Clean Typography -->
        <h1
          class="text-6xl md:text-8xl lg:text-[7rem] font-bold tracking-tighter mb-8 leading-[1.05]"
        >
          {{ $t("home.hero.title_part1") }} <br />
          <span
            class="bg-gradient-to-r from-[var(--primary)] to-blue-500 bg-clip-text text-transparent"
          >
            {{ $t("home.hero.title_part2") }}
          </span>
        </h1>

        <p
          class="text-[var(--subtext)] text-xl md:text-2xl leading-relaxed mb-16 max-w-2xl font-medium"
        >
          {{ $t("home.hero.subtitle") }}
        </p>

        <!-- Pill Buttons -->
        <div
          class="flex flex-col sm:flex-row items-center gap-4 w-full sm:w-auto"
        >
          <NuxtLink
            to="/signup"
            class="px-10 py-5 bg-[var(--text)] text-[var(--background)] rounded-full font-bold transition-all hover:scale-105 hover:shadow-2xl hover:shadow-[var(--text)]/20 w-full sm:w-auto text-center text-lg flex items-center justify-center gap-3"
          >
            {{ $t("home.hero.cta_primary") }}
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              class="w-5 h-5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"
              />
            </svg>
          </NuxtLink>
          <NuxtLink
            to="/login"
            class="px-10 py-5 bg-transparent text-[var(--text)] hover:bg-[var(--bg-secondary)] rounded-full font-bold transition-all w-full sm:w-auto text-center text-lg"
          >
            {{ $t("home.hero.cta_secondary") }}
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Main Feature Showcase (Fluid, Non-Boxy) -->
    <section class="max-w-7xl mx-auto px-6 py-24">
      <!-- Feature 1: The Synthesis Engine (Full Width, Soft) -->
      <div
        class="bg-[var(--bg-secondary)] rounded-[3rem] p-12 md:p-24 mb-10 flex flex-col md:flex-row items-center gap-16 transition-transform duration-500 hover:scale-[1.01]"
      >
        <div class="flex-1 space-y-8">
          <div
            class="h-20 w-20 rounded-full bg-[var(--primary)]/10 flex items-center justify-center text-[var(--primary)]"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-10 h-10"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M9.75 3.104v17.792m0-17.792l-3.3 3.3m3.3-3.3l3.3 3.3M9.75 20.896l-3.3-3.3m3.3 3.3l3.3-3.3M18 3.104v17.792m0-17.792l-3.3 3.3m3.3-3.3l3.3 3.3M18 20.896l-3.3-3.3m3.3 3.3l3.3-3.3"
              />
            </svg>
          </div>
          <h2 class="text-4xl md:text-5xl font-bold tracking-tight">
            {{ $t("home.features.synthesis.title") }}
          </h2>
          <p class="text-[var(--subtext)] text-xl leading-relaxed font-medium">
            {{ $t("home.features.synthesis.description") }}
          </p>
          <div class="flex flex-wrap gap-4 pt-4">
            <span class="text-sm font-semibold text-[var(--text)]">{{
              $t("home.tags.renal")
            }}</span>
            <span class="text-sm text-[var(--border)]">•</span>
            <span class="text-sm font-semibold text-[var(--text)]">{{
              $t("home.tags.hepatic")
            }}</span>
            <span class="text-sm text-[var(--border)]">•</span>
            <span class="text-sm font-semibold text-[var(--text)]">{{
              $t("home.tags.metabolic")
            }}</span>
          </div>
        </div>
        <!-- Abstract representation instead of a hard image box -->
        <div
          class="flex-1 flex justify-center items-center relative w-full h-64 md:h-auto"
        >
          <div
            class="absolute w-64 h-64 bg-gradient-to-tr from-blue-400 to-[var(--primary)] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-blob"
          ></div>
          <div
            class="absolute w-64 h-64 bg-gradient-to-tr from-emerald-400 to-teal-300 rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-blob animation-delay-2000 top-10 right-10"
          ></div>
        </div>
      </div>

      <!-- Feature 2 & 3: Floating Panels -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-10 mb-10">
        <!-- AI Companion -->
        <div
          class="bg-[var(--card)] rounded-[3rem] p-12 shadow-2xl shadow-black/5 flex flex-col justify-between hover:-translate-y-2 transition-transform duration-500"
        >
          <div>
            <div
              class="h-16 w-16 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-500 mb-8"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-8 h-8"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M7.5 8.25h9m-9 3h9m-9 3h3m-6.75 12a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0120.25 18V6.75A2.25 2.25 0 0018 4.5H3a2.25 2.25 0 00-2.25 2.25v10.5A2.25 2.25 0 003 18h1.5V21l3-3z"
                />
              </svg>
            </div>
            <h3 class="text-3xl font-bold mb-4 tracking-tight">
              {{ $t("home.features.companion.title") }}
            </h3>
            <p
              class="text-[var(--subtext)] text-lg leading-relaxed font-medium mb-10"
            >
              {{ $t("home.features.companion.description") }}
            </p>
          </div>
          <div class="bg-[var(--bg-secondary)] rounded-2xl p-6">
            <p class="text-sm font-medium text-[var(--text)] italic">
              "{{ $t("home.features.companion.prompt_example") }}"
            </p>
          </div>
        </div>

        <!-- Interactive Charts -->
        <div
          class="bg-[var(--card)] rounded-[3rem] p-12 shadow-2xl shadow-black/5 flex flex-col justify-between hover:-translate-y-2 transition-transform duration-500"
        >
          <div>
            <div
              class="h-16 w-16 rounded-full bg-emerald-500/10 flex items-center justify-center text-emerald-500 mb-8"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-8 h-8"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z"
                />
              </svg>
            </div>
            <h3 class="text-3xl font-bold mb-4 tracking-tight">
              {{ $t("home.features.charts.title") }}
            </h3>
            <p
              class="text-[var(--subtext)] text-lg leading-relaxed font-medium"
            >
              {{ $t("home.features.charts.description") }}
            </p>
          </div>
        </div>
      </div>

      <!-- Feature 4 & 5: Minimalist Row (Reports & Emergency) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div
          class="flex items-start gap-6 p-8 rounded-[2rem] hover:bg-[var(--bg-secondary)] transition-colors duration-300"
        >
          <div
            class="h-12 w-12 rounded-full bg-orange-500/10 flex items-center justify-center text-orange-500 shrink-0 mt-1"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"
              />
            </svg>
          </div>
          <div>
            <h3 class="text-xl font-bold mb-2">
              {{ $t("home.features.reports.title") }}
            </h3>
            <p
              class="text-[var(--subtext)] text-base font-medium leading-relaxed"
            >
              {{ $t("home.features.reports.description") }}
            </p>
          </div>
        </div>

        <div
          class="flex items-start gap-6 p-8 rounded-[2rem] hover:bg-[var(--bg-secondary)] transition-colors duration-300"
        >
          <div
            class="h-12 w-12 rounded-full bg-red-500/10 flex items-center justify-center text-red-500 shrink-0 mt-1"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 3v1.5a9 9 0 00-9 9H1.5a10.5 10.5 0 0110.5-10.5zM12 21v-1.5a9 9 0 009-9H22.5A10.5 10.5 0 0112 21zM3 12H1.5A10.5 10.5 0 0112 1.5V3a9 9 0 00-9 9zM21 12h1.5A10.5 10.5 0 0112 22.5V21a9 9 0 009-9z"
              />
            </svg>
          </div>
          <div>
            <h3 class="text-xl font-bold mb-2">
              {{ $t("home.features.emergency.title") }}
            </h3>
            <p
              class="text-[var(--subtext)] text-base font-medium leading-relaxed"
            >
              {{ $t("home.features.emergency.description") }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Final Serene CTA -->
    <section class="max-w-5xl mx-auto px-6 pb-32">
      <div
        class="bg-[var(--primary)] rounded-[3rem] p-16 md:p-24 text-center relative overflow-hidden shadow-2xl shadow-[var(--primary)]/20"
      >
        <div class="relative z-10 flex flex-col items-center">
          <h2
            class="text-4xl md:text-5xl font-bold mb-6 tracking-tight text-white"
          >
            {{ $t("home.final_cta.title") }}
          </h2>
          <p class="text-white/80 mb-12 max-w-xl mx-auto text-xl font-medium">
            {{ $t("home.final_cta.description") }}
          </p>
          <NuxtLink
            to="/signup"
            class="inline-block px-12 py-5 bg-white text-[var(--primary)] rounded-full font-bold hover:scale-105 transition-transform text-lg shadow-xl"
          >
            {{ $t("home.final_cta.button") }}
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Optional soft animation for the abstract blobs in feature 1 */
@keyframes blob {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  33% {
    transform: translate(30px, -50px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
}
.animate-blob {
  animation: blob 7s infinite;
}
.animation-delay-2000 {
  animation-delay: 2s;
}
</style>
