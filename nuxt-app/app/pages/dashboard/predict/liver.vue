<script setup lang="ts">
import { reactive } from "vue";

definePageMeta({
  layout: "dashboard",
});

const form = reactive({
  age: null,
  gender: "0",
  total_bilirubin: null,
  direct_bilirubin: null,
  alkaline_phosphatase: null,
  alamine_aminotransferase: null,
  aspartate_aminotransferase: null,
  total_proteins: null,
  albumin: null,
  albumin_and_globulin_ratio: null,
});

const handleSubmit = () => {
  console.log("Initiating Hepatic Neural Analysis...", form);
};
</script>

<template>
  <div class="max-w-5xl">
    <header class="mb-12">
      <p
        class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
      >
        AI Diagnostics
      </p>
      <h1 class="text-5xl font-black tracking-tight mb-4">
        Liver Disease <br /><span class="opacity-50">Hepatic Analysis</span>
      </h1>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Main Form Section -->
      <section
        class="lg:col-span-2 bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-10"
      >
        <div class="flex justify-between items-center mb-10">
          <h2 class="text-xl font-black">Clinical Indicators</h2>
          <span
            class="text-[10px] font-bold text-[var(--primary)] px-3 py-1 bg-[var(--primary)]/10 rounded-full"
          >
            10 Parameters Required
          </span>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Cluster 1: Patient Profile -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="group">
              <label
                class="block text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2 px-1"
                >Patient Age</label
              >
              <div class="relative">
                <input
                  v-model="form.age"
                  type="number"
                  min="18"
                  max="100"
                  required
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold focus:border-[var(--primary)] outline-none transition-all"
                  placeholder="Enter value..."
                />
                <span
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-black text-[var(--primary)] opacity-40 uppercase"
                  >Years</span
                >
              </div>
            </div>
            <div class="group">
              <label
                class="block text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2 px-1"
                >Gender</label
              >
              <div class="relative">
                <select
                  v-model="form.gender"
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold appearance-none outline-none focus:border-[var(--primary)] transition-all"
                >
                  <option value="0">Male</option>
                  <option value="1">Female</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Cluster 2: Laboratory Indicators -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div
              v-for="field in [
                {
                  id: 'total_bilirubin',
                  label: 'Total Bilirubin',
                  hint: 'mg/dL',
                  step: '0.1',
                },
                {
                  id: 'direct_bilirubin',
                  label: 'Direct Bilirubin',
                  hint: 'mg/dL',
                  step: '0.1',
                },
                {
                  id: 'alkaline_phosphatase',
                  label: 'Alkaline Phos.',
                  hint: 'IU/L',
                  step: '1',
                },
                {
                  id: 'alamine_aminotransferase',
                  label: 'Alamine Amin.',
                  hint: 'IU/L',
                  step: '1',
                },
                {
                  id: 'aspartate_aminotransferase',
                  label: 'Aspartate Amin.',
                  hint: 'IU/L',
                  step: '1',
                },
                {
                  id: 'total_proteins',
                  label: 'Total Proteins',
                  hint: 'g/dL',
                  step: '0.1',
                },
                { id: 'albumin', label: 'Albumin', hint: 'g/dL', step: '0.1' },
                {
                  id: 'albumin_and_globulin_ratio',
                  label: 'A/G Ratio',
                  hint: 'Ratio',
                  step: '0.1',
                },
              ]"
              :key="field.id"
              class="group"
            >
              <label
                class="block text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2 px-1"
                >{{ field.label }}</label
              >
              <div class="relative">
                <input
                  v-model="form[field.id]"
                  type="number"
                  :step="field.step"
                  required
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold focus:border-[var(--primary)] outline-none transition-all"
                  placeholder="Enter value..."
                />
                <span
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-black text-[var(--primary)] opacity-40 uppercase"
                  >{{ field.hint }}</span
                >
              </div>
            </div>
          </div>

          <button
            type="submit"
            class="w-full mt-8 bg-[var(--primary)] text-white py-5 rounded-2xl font-black text-xs tracking-[0.2em] uppercase hover:brightness-110 active:scale-[0.98] transition-all shadow-lg shadow-[var(--primary)]/20"
          >
            Run Hepatic Diagnostic &rarr;
          </button>
        </form>
      </section>

      <!-- Sidebar -->
      <aside class="space-y-6">
        <section
          class="bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] p-8"
        >
          <h3 class="text-sm font-black mb-4 flex items-center gap-2">
            <i class="fas fa-microscope text-[var(--primary)]"></i>
            How it works
          </h3>
          <p
            class="text-[11px] text-[var(--subtext)] font-medium leading-relaxed opacity-80"
          >
            This module evaluates 10 metabolic markers to detect cellular damage
            or obstruction.
            <br /><br />
            Please ensure all clinical data is accurate for the most precise
            result.
          </p>
        </section>

        <!-- Emergency Block -->
        <section
          class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
        >
          <div class="flex items-center gap-3 mb-6">
            <h3
              class="text-[10px] font-black tracking-[0.2em] text-red-500 uppercase"
            >
              Critical Indicators
            </h3>
          </div>
          <h2 class="text-xl font-black mb-4">Hepatic Warning Signs</h2>
          <div class="space-y-3 mb-8">
            <div
              v-for="item in [
                {
                  title: 'Jaundice',
                  desc: 'Yellowing of skin or whites of eyes',
                },
                {
                  title: 'Acute Pain',
                  desc: 'Severe pain in the upper right abdomen',
                },
                {
                  title: 'Encephalopathy',
                  desc: 'Mental confusion or extreme drowsiness',
                },
              ]"
              :key="item.title"
              class="p-4 rounded-2xl bg-[var(--background)] border border-[var(--border)]/50"
            >
              <p
                class="text-[11px] font-black uppercase tracking-tight text-[var(--primary)] mb-1"
              >
                {{ item.title }}
              </p>
              <p
                class="text-[10px] font-bold text-[var(--subtext)] leading-tight opacity-70"
              >
                {{ item.desc }}
              </p>
            </div>
          </div>
          <a
            href="tel:102"
            class="flex items-center justify-between p-4 rounded-2xl bg-red-500/5 border border-red-500/20 hover:bg-red-500 hover:text-white transition-all group"
          >
            <div class="flex items-center gap-3">
              <i
                class="fas fa-ambulance text-red-500 group-hover:text-white transition-colors"
              ></i>
              <span class="text-[10px] font-black uppercase tracking-widest"
                >Immediate Help</span
              >
            </div>
            <span class="text-xs font-black opacity-40 group-hover:opacity-100"
              >102 &rarr;</span
            >
          </a>
        </section>
      </aside>
    </div>
  </div>
</template>

<style scoped>
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M19 9l-7 7-7-7'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1em;
}
</style>
