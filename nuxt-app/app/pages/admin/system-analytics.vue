<template>
  <div>
    <!-- HEADER -->
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        System Monitoring
      </p>

      <h1 class="text-5xl font-black tracking-tight mb-4">System Health</h1>
    </header>

    <!-- STATS -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div
        v-for="stat in systemStats"
        :key="stat.label"
        class="bg-[var(--card)] border border-[var(--border)] p-6 rounded-[2rem]"
      >
        <p
          class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2"
        >
          {{ stat.label }}
        </p>

        <h3 class="text-3xl font-black tracking-tighter">
          {{ stat.value }}
        </h3>

        <p class="text-[10px] font-bold text-[var(--primary)] mt-2">
          {{ stat.note }}
        </p>
      </div>
    </div>

    <!-- GRAPHS -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- 1. DISEASE DISTRIBUTION -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black">Disease Distribution</h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Reports per model
            </p>
          </div>
          <Icon
            name="ph:chart-pie-slice-fill"
            class="text-2xl text-[var(--primary)]"
          />
        </div>

        <div class="h-[300px]">
          <Bar :data="diseaseDistribution" :options="chartOptions" />
        </div>
      </section>

      <!-- 2. ACCURACY / CONFIDENCE -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black">AI Confidence Score</h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Average prediction confidence
            </p>
          </div>
          <Icon name="ph:cpu-fill" class="text-2xl text-emerald-500" />
        </div>

        <div class="h-[300px]">
          <Line :data="confidenceTrend" :options="chartOptions" />
        </div>
      </section>

      <!-- 3. SYSTEM ACTIVITY -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8 lg:col-span-2"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black">System Activity Log</h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Predictions over time
            </p>
          </div>
        </div>

        <div class="h-[350px]">
          <Line :data="activityData" :options="chartOptions" />
        </div>
      </section>
    </div>
  </div>
</template>
<script setup>
import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
} from "chart.js";
import { Bar, Line } from "vue-chartjs";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
);

definePageMeta({ layout: "admin" });
const { data: analyticsData } = await useFetch(
  "http://127.0.0.1:5001/api/admin/system-analytics",
  {
    key: "system-analytics",
  },
);

const stats = computed(() => analyticsData.value?.stats || {});
const charts = computed(() => analyticsData.value?.charts || {});

const systemStats = computed(() => [
  {
    label: "Total Predictions",
    value: stats.value.total_predictions || 0,
    note: "All-time system usage",
  },
  {
    label: "Diabetes Cases",
    value: stats.value.diabetes || 0,
    note: "AI model usage",
  },
  {
    label: "Kidney Cases",
    value: stats.value.kidney || 0,
    note: "CKD model usage",
  },
  {
    label: "Avg Confidence",
    value: `${stats.value.avg_confidence || 0}%`,
    note: "Model certainty",
  },
]);

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: { legend: { display: false } },
  scales: {
    y: { grid: { color: "rgba(255,255,255,0.05)" } },
    x: { grid: { display: false } },
  },
};

const diseaseDistribution = computed(() => {
  const dist = charts.value.disease_distribution || {};

  return {
    labels: dist.labels || [],
    datasets: [
      {
        data: dist.data || [],
        backgroundColor: ["#6366f1", "#10b981", "#f59e0b"],
        borderRadius: 10,
      },
    ],
  };
});

const confidenceTrend = computed(() => {
  const data = charts.value.confidence_trend || [];

  return {
    labels: data.map((_, i) => `R${i + 1}`),
    datasets: [
      {
        data,
        borderColor: "#10b981",
        tension: 0.4,
      },
    ],
  };
});

const activityData = computed(() => {
  const activity = charts.value.activity || [];

  return {
    labels: activity.map((a) => a.date),
    datasets: [
      {
        data: activity.map((a) => a.count),
        borderColor: "#6366f1",
        tension: 0.4,
      },
    ],
  };
});
</script>
