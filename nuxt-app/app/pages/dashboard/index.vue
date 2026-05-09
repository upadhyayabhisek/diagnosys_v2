<script setup lang="ts">
import { computed } from "vue";
definePageMeta({
  layout: "dashboard",
});

const { user } = useAuth();
const firstName = computed(() => user.value?.name?.split(" ")[0] || "User");

const stats = [
  {
    label: "Health Score",
    value: "84/100",
    trend: "+2%",
    color: "text-emerald-500",
  },
  {
    label: "Active Minutes",
    value: "45m",
    trend: "Goal: 60m",
    color: "text-blue-500",
  },
  {
    label: "Last Prediction",
    value: "Normal",
    trend: "Kidney AI",
    color: "text-[var(--primary)]",
  },
];

const { data: savedPlan, pending } = await useFetch(
  `http://localhost:5001/get-workout-plan`,
  {
    params: { email: user.value?.email },
    watch: [user],
  },
);
const exercises = computed(() => savedPlan.value?.data?.exercises || []);
</script>

<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Patient Dashboard
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">
        Stay Healthy, <br /><span class="opacity-50">{{ firstName }}</span>
      </h1>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
      <div
        v-for="stat in stats"
        :key="stat.label"
        class="p-8 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] transition-all"
      >
        <h3 class="text-[10px] font-bold text-[var(--subtext)] mb-1">
          {{ stat.label }}
        </h3>
        <p class="text-3xl font-black tracking-tight mb-2">{{ stat.value }}</p>
        <span
          :class="[
            'text-[10px] font-bold px-2 py-1 rounded-full bg-black/5 dark:bg-white/5',
            stat.color,
          ]"
        >
          {{ stat.trend }}
        </span>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black">Daily Exercise</h2>
            <p
              v-if="savedPlan?.data"
              class="text-[10px] font-bold text-[var(--primary)] uppercase"
            >
              Target: {{ savedPlan.data.target }}
            </p>
          </div>
          <NuxtLink
            to="/dashboard/exercise"
            class="text-[var(--primary)] text-xs font-bold"
          >
            Full Plan &rarr;
          </NuxtLink>
        </div>

        <div class="space-y-4">
          <!-- Loading State -->
          <div v-if="pending" class="animate-pulse space-y-4">
            <div
              v-for="i in 2"
              :key="i"
              class="h-16 bg-[var(--background)] rounded-2xl"
            ></div>
          </div>

          <!-- Empty State -->
          <div
            v-else-if="exercises.length === 0"
            class="py-10 text-center opacity-50"
          >
            <p class="text-xs font-bold">No plan saved yet.</p>
          </div>

          <!-- Dynamic Exercises -->
          <div
            v-for="ex in exercises.slice(0, 3)"
            :key="ex.name"
            class="flex items-center justify-between p-4 rounded-2xl bg-[var(--background)] border border-[var(--border)]"
          >
            <div class="flex items-center gap-4">
              <div
                class="w-10 h-10 rounded-xl bg-[var(--primary)] text-white flex items-center justify-center"
              >
                <svg
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path d="M13 10V3L4 14h7v7l9-11h-7z" stroke-width="2" />
                </svg>
              </div>
              <div>
                <p class="text-sm font-bold">{{ ex.name }}</p>
                <p class="text-[10px] text-[var(--subtext)]">
                  {{ ex.sets }} • ~{{ ex.calories }} kcal
                </p>
              </div>
            </div>
          </div>

          <!-- Summary footer if plan exists -->
          <div
            v-if="savedPlan?.data"
            class="pt-4 mt-4 border-t border-[var(--border)] flex justify-between items-center"
          >
            <span class="text-[9px] font-black uppercase text-[var(--subtext)]"
              >Total Burn</span
            >
            <span class="text-lg font-black text-[var(--primary)]"
              >{{ savedPlan.data.total_calories }} KCAL</span
            >
          </div>
        </div>
      </section>
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-xl font-black">Recent Reports</h2>
        </div>
        <div class="space-y-4">
          <div
            v-for="n in 3"
            :key="n"
            class="flex items-center justify-between p-4 rounded-2xl border border-[var(--border)]/50"
          >
            <div class="flex items-center gap-4">
              <div
                class="w-10 h-10 rounded-full bg-[var(--primary)]/10 text-[var(--primary)] flex items-center justify-center font-bold text-xs"
              >
                AI
              </div>
              <div>
                <p class="text-sm font-bold">Diabetes Risk Analysis</p>
                <p class="text-[10px] text-[var(--subtext)]">
                  Result: Low Risk
                </p>
              </div>
            </div>
            <p class="text-[10px] font-bold text-[var(--subtext)]">
              May {{ n + 1 }}, 2024
            </p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
