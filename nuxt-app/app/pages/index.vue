<template>
  <div>
    <section class="py-24 text-center max-w-4xl mx-auto">
      <div
        class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[var(--primary)]/10 border border-[var(--primary)]/20 text-[var(--primary)] text-sm mb-6 font-medium"
      >
        <span class="relative flex h-2 w-2">
          <span
            class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[var(--primary)] opacity-75"
          ></span>
          <span
            class="relative inline-flex rounded-full h-2 w-2 bg-[var(--primary)]"
          ></span>
        </span>
        {{ $t("hero.badge") || "New: AI Symptom Checker v2.0" }}
      </div>

      <h1
        class="text-5xl md:text-7xl font-black tracking-tight mb-6 bg-gradient-to-b from-[var(--text)] to-[var(--subtext)] bg-clip-text text-transparent leading-[1.1]"
      >
        AI-Powered <br class="hidden md:block" />
        Medical Diagnosis
      </h1>

      <p
        class="text-[var(--subtext)] text-lg md:text-xl leading-relaxed mb-10 max-w-2xl mx-auto font-medium"
      >
        Get instant health insights using advanced machine learning. Smart
        predictions, clear results, and data-driven decisions for your
        well-being.
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <NuxtLink
          to="/signup"
          class="px-8 py-4 bg-[var(--primary)] text-white hover:brightness-110 rounded-2xl font-bold transition-all hover:scale-105 shadow-xl shadow-[var(--primary)]/20 w-full sm:w-auto text-center"
        >
          Get Started Free
        </NuxtLink>
        <NuxtLink
          to="/login"
          class="px-8 py-4 bg-[var(--card)] text-[var(--text)] border border-[var(--border)] hover:bg-[var(--bg-secondary)] rounded-2xl font-bold transition-all w-full sm:w-auto text-center"
        >
          Sign In
        </NuxtLink>
      </div>
    </section>

    <section class="grid grid-cols-1 md:grid-cols-3 gap-6 pb-24">
      <div
        class="group p-8 rounded-[2rem] bg-[var(--card)] border border-[var(--border)] hover:border-[var(--primary)]/50 transition-all duration-300"
      >
        <div
          class="h-12 w-12 rounded-2xl bg-blue-500/10 flex items-center justify-center text-blue-500 mb-6 group-hover:scale-110 transition-transform"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
        <h3 class="text-xl font-extrabold mb-3 text-[var(--text)]">
          Accurate Predictions
        </h3>
        <p class="text-[var(--subtext)] leading-relaxed text-sm font-medium">
          ML-powered disease detection based on your unique symptoms and
          history.
        </p>
      </div>

      <div
        class="group p-8 rounded-[2rem] bg-[var(--card)] border border-[var(--border)] hover:border-emerald-500/50 transition-all duration-300"
      >
        <div
          class="h-12 w-12 rounded-2xl bg-emerald-500/10 flex items-center justify-center text-emerald-500 mb-6 group-hover:scale-110 transition-transform"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
            />
          </svg>
        </div>
        <h3 class="text-xl font-extrabold mb-3 text-[var(--text)]">
          Insights Dashboard
        </h3>
        <p class="text-[var(--subtext)] leading-relaxed text-sm font-medium">
          Visual trends and health analytics designed for total body awareness.
        </p>
      </div>

      <div
        class="group p-8 rounded-[2rem] bg-[var(--card)] border border-[var(--border)] hover:border-purple-500/50 transition-all duration-300"
      >
        <div
          class="h-12 w-12 rounded-2xl bg-purple-500/10 flex items-center justify-center text-purple-500 mb-6 group-hover:scale-110 transition-transform"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
            />
          </svg>
        </div>
        <h3 class="text-xl font-extrabold mb-3 text-[var(--text)]">
          Personalized Advice
        </h3>
        <p class="text-[var(--subtext)] leading-relaxed text-sm font-medium">
          Custom diet, exercise, and severity recommendations tailored to you.
        </p>
      </div>
    </section>
  </div>

  <div class="p-4">
    <h1 class="text-xl font-bold">Backend Test</h1>
    <button
      @click="callApi"
      class="px-4 py-2 bg-blue-500 text-white rounded mt-4"
    >
      Click to Print in Flask
    </button>
  </div>
</template>

<script setup>
import { useTestApi } from "@services/test";

const { printOnBackend } = useTestApi();

const callApi = async () => {
  console.log("Sending request...");
  const res = await printOnBackend();
  console.log("Response from Flask:", res);
};
</script>
