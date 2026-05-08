<script setup lang="ts">
definePageMeta({ layout: "dashboard" });

const healthTracks = [
  {
    title: "Kidney Health",
    icon: "ph:leaf-bold",
    params: [
      {
        name: "Creatinine",
        current: "0.8",
        previous: "1.1",
        unit: "mg/dL",
        status: "improved",
      },
      {
        name: "eGFR",
        current: "95",
        previous: "88",
        unit: "mL/min",
        status: "improved",
      },
    ],
  },
  {
    title: "Liver Profile",
    icon: "ph:activity-bold",
    params: [
      {
        name: "ALT",
        current: "32",
        previous: "30",
        unit: "U/L",
        status: "stable",
      },
      {
        name: "AST",
        current: "28",
        previous: "29",
        unit: "U/L",
        status: "improved",
      },
    ],
  },
  {
    title: "Diabetes Control",
    icon: "ph:drop-bold",
    params: [
      {
        name: "HbA1c",
        current: "5.6",
        previous: "6.2",
        unit: "%",
        status: "improved",
      },
      {
        name: "Fasting Glucose",
        current: "98",
        previous: "115",
        unit: "mg/dL",
        status: "improved",
      },
    ],
  },
];
</script>

<template>
  <div>
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        Past Data
      </p>
      <h1 class="text-5xl font-black tracking-tight">
        Health <span class="opacity-50">Trends</span>
      </h1>
    </header>

    <div class="space-y-12">
      <section
        v-for="track in healthTracks"
        :key="track.title"
        class="space-y-6"
      >
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 rounded-full bg-[var(--primary)]/10 text-[var(--primary)] flex items-center justify-center"
          >
            <Icon :name="track.icon" class="text-xl" />
          </div>
          <h2 class="text-xl font-black tracking-tight">{{ track.title }}</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="param in track.params"
            :key="param.name"
            class="bg-[var(--card)] border border-[var(--border)] p-8 rounded-[3rem] transition-all hover:border-[var(--primary)] group"
          >
            <div class="flex justify-between items-start mb-6">
              <div>
                <p
                  class="text-[10px] font-black uppercase text-[var(--subtext)] mb-1"
                >
                  {{ param.name }}
                </p>
                <div class="flex items-baseline gap-1">
                  <span class="text-4xl font-black tracking-tighter">{{
                    param.current
                  }}</span>
                  <span class="text-xs font-bold text-[var(--subtext)]">{{
                    param.unit
                  }}</span>
                </div>
              </div>

              <div
                :class="[
                  'px-3 py-1 rounded-full text-[10px] font-black uppercase flex items-center gap-1',
                  param.status === 'improved'
                    ? 'bg-emerald-500/10 text-emerald-500'
                    : 'bg-amber-500/10 text-amber-500',
                ]"
              >
                <Icon
                  :name="
                    param.status === 'improved'
                      ? 'ph:arrow-down-bold'
                      : 'ph:minus-bold'
                  "
                />
                {{ param.status }}
              </div>
            </div>

            <div class="pt-6 border-t border-[var(--border)]/50">
              <div
                class="flex justify-between items-center text-[10px] font-bold uppercase tracking-widest text-[var(--subtext)]"
              >
                <span>Previous Record</span>
                <span class="text-[var(--text)]"
                  >{{ param.previous }} {{ param.unit }}</span
                >
              </div>
              <div
                class="w-full bg-[var(--background)] h-1.5 rounded-full mt-3 overflow-hidden"
              >
                <div
                  class="bg-[var(--primary)] h-full transition-all duration-1000"
                  :style="{
                    width:
                      (parseFloat(param.current) / parseFloat(param.previous)) *
                        100 +
                      '%',
                  }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
