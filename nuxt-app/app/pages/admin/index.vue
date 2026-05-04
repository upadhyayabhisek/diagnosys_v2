<script setup lang="ts">
import { computed } from "vue";
definePageMeta({
  layout: "admin",
});

const { user } = useAuth();
const adminName = computed(() => user.value?.name || "Admin");
</script>

<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Admin Panel
      </p>

      <h1 class="text-5xl font-black tracking-tight mb-4">
        Welcome back, <br /><span class="opacity-50">{{ adminName }}</span>
      </h1>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
      <div
        v-for="i in 3"
        :key="i"
        class="p-8 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] hover:scale-[1.02] transition-transform cursor-pointer"
      >
        <div
          class="w-12 h-12 rounded-2xl bg-[var(--primary)]/10 flex items-center justify-center mb-6 text-[var(--primary)]"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>

        <h3 class="text-[10px] font-bold uppercase text-[var(--subtext)] mb-1">
          Growth Metric {{ i }}
        </h3>

        <p class="text-3xl font-black tracking-tight">+{{ 12 * i }}%</p>
      </div>
    </div>

    <section
      class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
    >
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-xl font-black">Recent System Activity</h2>

        <button
          class="px-4 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold"
        >
          View Reports
        </button>
      </div>

      <div class="space-y-4">
        <div
          v-for="n in 4"
          :key="n"
          class="flex items-center justify-between p-4 rounded-2xl border border-[var(--border)]/50 hover:bg-[var(--border)]/20 transition-colors"
        >
          <div class="flex items-center gap-4">
            <div
              class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-500 flex items-center justify-center font-bold text-xs"
            >
              U
            </div>

            <div>
              <p class="text-sm font-bold">New User Registered</p>
              <p class="text-[10px] text-[var(--subtext)] font-medium">
                user_{{ n }}42@example.com
              </p>
            </div>
          </div>

          <p class="text-[10px] font-bold text-[var(--subtext)]">2 mins ago</p>
        </div>
      </div>
    </section>
  </div>
</template>
