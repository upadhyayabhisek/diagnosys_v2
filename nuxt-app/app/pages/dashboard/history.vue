<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const reports = ref([
  {
    id: "REP-001",
    type: "Kidney Function",
    date: "May 12, 2024",
    status: "Normal",
    statusColor: "text-emerald-500",
    summary: "Creatinine and GFR levels within optimal range.",
  },
  {
    id: "REP-002",
    type: "Diabetes Screening",
    date: "May 10, 2024",
    status: "Borderline",
    statusColor: "text-amber-500",
    summary: "HbA1c is slightly elevated (5.8%). Monitor sugar intake.",
  },
  {
    id: "REP-003",
    type: "Liver Profile",
    date: "May 05, 2024",
    status: "Healthy",
    statusColor: "text-emerald-500",
    summary: "ALT/AST enzymes show no signs of inflammation.",
  },
]);

const downloadPDF = (reportId: string) => {
  console.log(`Generating PDF for ${reportId}...`);
};
</script>

<template>
  <div>
    <header class="mb-12 flex justify-between items-end">
      <div>
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
        >
          Past Analysis
        </p>
        <h1 class="text-5xl font-black tracking-tight mb-4">
          Report <span class="opacity-50">History</span>
        </h1>
      </div>
    </header>

    <div class="space-y-6">
      <div
        v-for="report in reports"
        :key="report.id"
        class="group bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] p-8 hover:border-[var(--primary)] transition-all"
      >
        <div
          class="flex flex-col md:flex-row md:items-center justify-between gap-6"
        >
          <div class="flex items-center gap-6">
            <div
              class="w-16 h-16 rounded-3xl bg-[var(--background)] border border-[var(--border)] flex items-center justify-center"
            >
              <Icon
                name="ph:file-magnifying-glass-duotone"
                class="text-3xl text-[var(--primary)]"
              />
            </div>

            <div>
              <div class="flex items-center gap-3 mb-1">
                <h2 class="text-xl font-black">{{ report.type }}</h2>
                <span
                  :class="[
                    'text-[10px] font-black uppercase px-2 py-0.5 rounded-md bg-black/5 dark:bg-white/5',
                    report.statusColor,
                  ]"
                >
                  {{ report.status }}
                </span>
              </div>
              <p class="text-sm text-[var(--subtext)] font-medium mb-2">
                {{ report.summary }}
              </p>
              <p
                class="text-[10px] font-bold text-[var(--subtext)] uppercase tracking-widest"
              >
                {{ report.date }} • ID: {{ report.id }}
              </p>
            </div>
          </div>

          <div class="flex items-center gap-3">
            <NuxtLink
              :to="`/dashboard/reports/${report.id}`"
              class="px-6 py-3 rounded-xl border border-[var(--border)] text-xs font-bold hover:bg-[var(--background)] transition-colors"
            >
              View Analysis
            </NuxtLink>
            <button
              @click="downloadPDF(report.id)"
              class="w-12 h-12 flex items-center justify-center rounded-xl bg-[var(--primary)] text-white hover:brightness-110 transition-all"
              title="Download PDF"
            >
              <Icon name="ph:download-simple-bold" class="text-xl" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
