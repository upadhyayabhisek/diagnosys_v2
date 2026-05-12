<script setup lang="ts">
import { computed } from "vue";

definePageMeta({
  layout: "dashboard",
});

const { user } = useAuth();

const firstName = computed(() => user.value?.name?.split(" ")[0] || "User");

/* ----------------------------------------
   Workout Plan
---------------------------------------- */

const { data: savedPlan, pending } = await useFetch(
  `http://localhost:5001/get-workout-plan`,
  {
    params: {
      email: user.value?.email,
    },
    watch: [user],
  },
);

const exercises = computed(() => savedPlan.value?.data?.exercises || []);

const { data: reportsData, pending: reportsPending } = await useFetch(
  `http://localhost:5001/api/reports/${user.value?.email}`,
  {
    params: {
      limit: 4,
    },
    watch: [user],
  },
);

const reports = computed(() => reportsData.value?.reports || []);
const stats = computed(() => {
  const totalReports = reportsData.value?.pagination?.total || 0;

  const highRisk = reports.value.filter(
    (r: any) =>
      !r.status.toLowerCase().includes("no") &&
      !r.status.toLowerCase().includes("normal"),
  ).length;

  const latestType = reports.value[0]?.type?.replace(" Analysis", "") || "None";

  return [
    {
      label: "Total Reports",
      value: totalReports,
      trend: "AI Generated",
      color: "text-blue-500",
    },

    {
      label: "Risk Alerts",
      value: highRisk,
      trend: highRisk > 0 ? "Needs Attention" : "All Good",
      color: highRisk > 0 ? "text-red-500" : "text-emerald-500",
    },

    {
      label: "Latest Scan",
      value: latestType,
      trend: "Most Recent",
      color: "text-[var(--primary)]",
    },
  ];
});

const diseaseIcons: Record<string, string> = {
  Diabetes: "lucide:droplets",
  Kidney: "lucide:activity",
  Liver: "lucide:heart-pulse",
};

const getDiseaseIcon = (type: string) => {
  const clean = type.replace(" Analysis", "");
  return diseaseIcons[clean] || "📄";
};

const navigateToHistory = async (reportId: string) => {
  await navigateTo({
    path: "/dashboard/history",
    query: {
      report: reportId,
    },
  });
};
</script>

<template>
  <div>
    <!-- Header -->
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Patient Dashboard
      </p>

      <h1 class="text-5xl font-black tracking-tight mb-4">
        Stay Healthy,
        <br />
        <span class="opacity-50">
          {{ firstName }}
        </span>
      </h1>
    </header>

    <!-- Stats -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
      <div
        v-for="stat in stats"
        :key="stat.label"
        class="p-8 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] transition-all"
      >
        <h3 class="text-[10px] font-bold text-[var(--subtext)] mb-1 uppercase">
          {{ stat.label }}
        </h3>

        <p class="text-3xl font-black tracking-tight mb-2">
          {{ stat.value }}
        </p>

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

    <!-- Main Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Workout Plan -->
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
              Target:
              {{ savedPlan.data.target }}
            </p>
          </div>

          <NuxtLink
            to="/dashboard/exercise"
            class="text-[var(--primary)] text-xs font-bold"
          >
            Full Plan →
          </NuxtLink>
        </div>

        <div class="space-y-4">
          <!-- Loading -->
          <div v-if="pending" class="animate-pulse space-y-4">
            <div
              v-for="i in 2"
              :key="i"
              class="h-16 bg-[var(--background)] rounded-2xl"
            />
          </div>

          <!-- Empty -->
          <div
            v-else-if="exercises.length === 0"
            class="py-10 text-center opacity-50"
          >
            <p class="text-xs font-bold">No plan saved yet.</p>
          </div>

          <!-- Exercises -->
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
                <p class="text-sm font-bold">
                  {{ ex.name }}
                </p>

                <p class="text-[10px] text-[var(--subtext)]">
                  {{ ex.sets }} • ~{{ ex.calories }}
                  kcal
                </p>
              </div>
            </div>
          </div>

          <!-- Footer -->
          <div
            v-if="savedPlan?.data"
            class="pt-4 mt-4 border-t border-[var(--border)] flex justify-between items-center"
          >
            <span class="text-[9px] font-black uppercase text-[var(--subtext)]">
              Total Burn
            </span>

            <span class="text-lg font-black text-[var(--primary)]">
              {{ savedPlan.data.total_calories }}
              KCAL
            </span>
          </div>
        </div>
      </section>

      <!-- Recent Reports -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black">Recent Reports</h2>

            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Latest AI Predictions
            </p>
          </div>

          <NuxtLink
            to="/dashboard/history"
            class="text-[var(--primary)] text-xs font-bold"
          >
            View All →
          </NuxtLink>
        </div>

        <div class="space-y-4">
          <!-- Loading -->
          <div v-if="reportsPending" class="animate-pulse space-y-4">
            <div
              v-for="i in 3"
              :key="i"
              class="h-20 bg-[var(--background)] rounded-2xl"
            />
          </div>

          <!-- Empty -->
          <div
            v-else-if="reports.length === 0"
            class="py-10 text-center opacity-50"
          >
            <p class="text-xs font-bold">No reports available.</p>
          </div>

          <!-- Reports -->
          <button
            v-for="report in reports"
            :key="report.id"
            @click="navigateToHistory(report.id)"
            class="w-full flex items-center justify-between p-4 rounded-2xl border border-[var(--border)]/50 hover:border-[var(--primary)]/30 hover:bg-[var(--background)] transition-all text-left"
          >
            <div class="flex items-center gap-4">
              <!-- Icon -->
              <div
                class="w-12 h-12 rounded-2xl bg-[var(--primary)]/10 text-[var(--primary)] flex items-center justify-center text-lg"
              >
                <Icon :name="getDiseaseIcon(report.type)" class="w-5 h-5" />
              </div>

              <!-- Content -->
              <div>
                <p class="text-sm font-bold">
                  {{ report.type }}
                </p>

                <p class="text-[10px] font-bold" :class="report.statusColor">
                  {{ report.status }}
                </p>

                <p class="text-[9px] text-[var(--subtext)] mt-1">
                  {{ report.summary }}
                </p>
              </div>
            </div>

            <!-- Right -->
            <div class="text-right">
              <p class="text-[10px] font-bold text-[var(--subtext)]">
                {{ new Date(report.date).toLocaleDateString() }}
              </p>

              <p class="text-[9px] text-[var(--subtext)] mt-1">
                {{ report.id }}
              </p>
            </div>
          </button>
        </div>
      </section>
    </div>
  </div>
</template>
