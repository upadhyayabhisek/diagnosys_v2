<script setup lang="ts">
import DiagnosisResult from "~/components/DiagnosisResult.vue";

// 1. Mock Data: This mimics what your form or API would send
const mockData = {
  type: "Kidney" as const,
  result: "Chronic Kidney Disease Detected", // Change to "Normal" to test green theme
  confidence: "94.8",
  reportId: "DX-KN-2026-0042",
  patientName: "Guest User",

  // This mimics the 'form' object from your Kidney page
  formData: {
    age: 52,
    blood_pressure: 85,
    specific_gravity: "1.010",
    albumin: "3",
    sugar: "0",
    blood_glucose_random: 145,
    serum_creatinine: 2.4,
    haemoglobin: 10.2,
    packed_cell_volume: 32,
    hypertension: "yes",
    diabetes_mellitus: "yes",
    appetite: "poor",
    peda_edema: "yes",
    aanemia: "no",
  },
};

const handleDownload = () => {
  alert("PDF Generation Logic Triggered!");
};

const handleBack = () => {
  alert("Navigating back to Diagnostic Form...");
};
</script>

<template>
  <!-- Background wrapper to match your dashboard theme -->
  <div class="min-h-screen bg-[var(--background)] p-8 md:p-12">
    <div class="max-w-5xl mx-auto">
      <!-- Page Header -->
      <div class="mb-10">
        <h2
          class="text-[10px] font-black uppercase tracking-[0.3em] text-[var(--primary)] mb-2"
        >
          Design Preview Mode
        </h2>
        <p class="text-sm text-[var(--subtext)] font-bold">
          Testing high-fidelity result component with mock neural data.
        </p>
      </div>

      <!-- THE COMPONENT -->
      <DiagnosisResult
        :type="mockData.type"
        :result="mockData.result"
        :confidence="mockData.confidence"
        :formData="mockData.formData"
        :reportId="mockData.reportId"
        :patientName="mockData.patientName"
        @download="handleDownload"
        @back="handleBack"
      />

      <!-- Design Tester Controls -->
      <div
        class="mt-12 p-6 border border-[var(--border)] border-dashed rounded-[2rem] flex flex-wrap gap-4 items-center justify-center"
      >
        <p
          class="text-[10px] font-black uppercase text-[var(--subtext)] w-full text-center mb-2"
        >
          Theme Switcher
        </p>
        <button
          @click="mockData.result = 'Chronic Kidney Disease Detected'"
          class="px-4 py-2 bg-red-500/10 text-red-500 rounded-xl text-[10px] font-black uppercase"
        >
          Test Warning (Red)
        </button>
        <button
          @click="mockData.result = 'No Kidney Disease Detected'"
          class="px-4 py-2 bg-emerald-500/10 text-emerald-500 rounded-xl text-[10px] font-black uppercase"
        >
          Test Normal (Green)
        </button>
      </div>
    </div>
  </div>
</template>

<style>
/* Ensure your global variables are present if not in layout */
:root {
  --primary: #256d85;
  --background: #f0f4f8;
  --card: #ffffff;
  --border: #d1d9e6;
  --text: #1a1a1a;
  --subtext: #64748b;
}

/* Dark mode support */
.dark-mode {
  --background: #0f172a;
  --card: #1e293b;
  --border: #334155;
  --text: #f8fafc;
  --subtext: #94a3b8;
}
</style>
