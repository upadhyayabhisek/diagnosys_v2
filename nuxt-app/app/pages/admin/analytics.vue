<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2 uppercase"
      >
        Model Training Data
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">
        Feature <span class="opacity-30">Analysis</span>
      </h1>
    </header>

    <!-- Model Stats -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div
        v-for="stat in modelStats"
        :key="stat.label"
        class="bg-[var(--card)] border border-[var(--border)] p-6 rounded-[2rem]"
      >
        <p
          class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2"
        >
          {{ stat.label }}
        </p>
        <h3 class="text-3xl font-black tracking-tighter">{{ stat.value }}</h3>
        <p class="text-[10px] font-bold text-[var(--primary)] mt-2">
          Source: {{ stat.source }}
        </p>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Feature 1: Diabetes Correlation (Glucose vs BMI) -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black tracking-tight">
              Glucose vs BMI Density
            </h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Diabetes CSV Model Base
            </p>
          </div>
          <Icon
            name="ph:intersect-square-fill"
            class="text-2xl text-[var(--primary)]"
          />
        </div>
        <div class="h-[300px]">
          <Scatter :data="diabetesScatterData" :options="chartOptions" />
        </div>
      </section>

      <!-- Feature 2: Liver Function Distribution (Bilirubin levels) -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black tracking-tight">
              Liver Enzyme Spread
            </h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Direct vs Total Bilirubin
            </p>
          </div>
          <Icon name="ph:test-tube-fill" class="text-2xl text-amber-500" />
        </div>
        <div class="h-[300px]">
          <Bar :data="liverBarData" :options="chartOptions" />
        </div>
      </section>

      <!-- Feature 3: Kidney Disease Indicators (Albumin/Sugar/BP) -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8 lg:col-span-2"
      >
        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-xl font-black tracking-tight">
              CKD Model: Critical Feature Weights
            </h2>
            <p class="text-[10px] font-bold text-[var(--subtext)] uppercase">
              Analysis of Blood Pressure (bp) & Specific Gravity (sg)
            </p>
          </div>
        </div>
        <div class="h-[350px]">
          <Line :data="kidneyTrendData" :options="chartOptions" />
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
import { Bar, Line, Scatter } from "vue-chartjs";

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

const modelStats = [
  { label: "Training Rows", value: "2,450", source: "Diabetes.csv" },
  { label: "Features Used", value: "26", source: "Kidney.csv" },
  { label: "Target Classes", value: "2", source: "Liver.csv" },
  { label: "Missing Data", value: "0.4%", source: "Global" },
];

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: { legend: { display: false } },
  scales: {
    y: {
      grid: { color: "rgba(255,255,255,0.05)" },
      ticks: { font: { weight: "bold" } },
    },
    x: { grid: { display: false }, ticks: { font: { weight: "bold" } } },
  },
};

// Diabetes CSV: Glucose vs BMI scatter plot (Commonly used to find clusters)
const diabetesScatterData = {
  datasets: [
    {
      label: "Glucose/BMI Correlation",
      data: [
        { x: 85, y: 26 },
        { x: 120, y: 33 },
        { x: 150, y: 40 },
        { x: 90, y: 22 },
        { x: 180, y: 45 },
        { x: 110, y: 30 },
        { x: 140, y: 38 },
        { x: 100, y: 25 },
        { x: 160, y: 42 },
        { x: 95, y: 28 },
      ],
      backgroundColor: "#6366f1",
    },
  ],
};

// Liver CSV: Bilirubin levels (Direct vs Total)
const liverBarData = {
  labels: ["P1", "P2", "P3", "P4", "P5", "P6"],
  datasets: [
    {
      label: "Total Bilirubin",
      data: [0.7, 1.2, 0.8, 3.5, 1.1, 0.9],
      backgroundColor: "#f59e0b",
      borderRadius: 8,
    },
    {
      label: "Direct Bilirubin",
      data: [0.1, 0.4, 0.2, 1.8, 0.3, 0.2],
      backgroundColor: "#ef4444",
      borderRadius: 8,
    },
  ],
};

// Kidney CSV: BP and Specific Gravity Trend
const kidneyTrendData = {
  labels: ["Row 10", "Row 20", "Row 30", "Row 40", "Row 50", "Row 60"],
  datasets: [
    {
      label: "Blood Pressure (bp)",
      data: [80, 70, 90, 80, 110, 70],
      borderColor: "#6366f1",
      tension: 0.4,
      pointRadius: 4,
    },
    {
      label: "Specific Gravity (sg)",
      data: [1.02, 1.01, 1.02, 1.0, 1.01, 1.02],
      borderColor: "#10b981",
      tension: 0.4,
      yAxisID: "y1",
    },
  ],
};
</script>
