<script setup lang="ts">
import { reactive } from "vue";

definePageMeta({
  layout: "dashboard",
});

const form = reactive({
  pregnancies: null,
  glucose: null,
  blood_pressure: null,
  skin_thickness: null,
  insulin: null,
  bmi: null,
  diabetes_pedigree_function: null,
  age: null,
});

const handleSubmit = () => {
  console.log("Analyzing data...", form);
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
        Diabetes <br /><span class="opacity-50">Risk Analysis</span>
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
            8 Parameters Required
          </span>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Reusable Input Field Design -->
            <div
              v-for="field in [
                {
                  id: 'pregnancies',
                  label: 'Pregnancies',
                  hint: '0 - 20',
                  type: 'number',
                },
                {
                  id: 'glucose',
                  label: 'Glucose Concentration',
                  hint: 'mg/dL',
                  type: 'number',
                },
                {
                  id: 'blood_pressure',
                  label: 'Blood Pressure',
                  hint: 'mm Hg',
                  type: 'number',
                },
                {
                  id: 'skin_thickness',
                  label: 'Triceps Skin Fold',
                  hint: 'mm',
                  type: 'number',
                },
                {
                  id: 'insulin',
                  label: 'Serum Insulin',
                  hint: 'mu U/ml',
                  type: 'number',
                },
                {
                  id: 'bmi',
                  label: 'Body Mass Index',
                  hint: 'Weight/Height²',
                  type: 'number',
                  step: '0.1',
                },
                {
                  id: 'diabetes_pedigree_function',
                  label: 'Pedigree Function',
                  hint: 'Genetic Risk',
                  type: 'number',
                  step: '0.01',
                },
                { id: 'age', label: 'Age', hint: 'Years', type: 'number' },
              ]"
              :key="field.id"
              class="group"
            >
              <label
                :for="field.id"
                class="block text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] mb-2 px-1"
              >
                {{ field.label }}
              </label>
              <div class="relative">
                <input
                  v-model="form[field.id]"
                  :id="field.id"
                  :type="field.type"
                  :step="field.step || '1'"
                  required
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold focus:border-[var(--primary)] outline-none transition-all"
                  placeholder="Enter value..."
                />
                <span
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-black text-[var(--primary)] opacity-40 uppercase"
                >
                  {{ field.hint }}
                </span>
              </div>
            </div>
          </div>

          <button
            type="submit"
            class="w-full mt-8 bg-[var(--primary)] text-white py-5 rounded-2xl font-black text-xs tracking-[0.2em] uppercase hover:brightness-110 active:scale-[0.98] transition-all shadow-lg shadow-[var(--primary)]/20"
          >
            Run AI Diagnostic &rarr;
          </button>
        </form>
      </section>

      <!-- Sidebar Info Section: Matches the "Recent Reports" style -->
      <aside class="space-y-6">
        <section
          class="bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] p-8"
        >
          <h3 class="text-sm font-black mb-4 flex items-center gap-2">
            <i class="fas fa-info-circle text-[var(--primary)]"></i>
            How it works
          </h3>
          <p
            class="text-[11px] text-[var(--subtext)] font-medium leading-relaxed opacity-80"
          >
            This system uses a trained Neural Network to predict the onset of
            diabetes based on diagnostic measures.
            <br /><br />
            Please ensure all clinical data is accurate for the most precise
            result.
          </p>
        </section>

        <!-- Updated Emergency / Warning Section -->
        <section
          class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
        >
          <div class="flex items-center gap-3 mb-6">
            <h3 class="text-[10px] font-black tracking-[0.2em] text-red-500">
              Critical Indicators
            </h3>
          </div>

          <h2 class="text-xl font-black mb-4">When to seek help?</h2>

          <div class="space-y-3 mb-8">
            <div
              v-for="item in [
                {
                  title: 'Ketoacidosis',
                  desc: 'Shortness of breath, fruity breath odor',
                },
                {
                  title: 'Severe Hyperglycemia',
                  desc: 'Blood sugar consistently above 300 mg/dL',
                },
                {
                  title: 'Extreme Lethargy',
                  desc: 'Confusion or inability to stay awake',
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

          <!-- Sleek Action Button -->
          <a
            href="tel:+977102"
            class="flex items-center justify-between p-4 rounded-2xl bg-red-500/5 border border-red-500/20 hover:bg-red-500 hover:text-white transition-all group"
          >
            <div class="flex items-center gap-3">
              <i
                class="fas fa-ambulance text-red-500 group-hover:text-white transition-colors"
              ></i>
              <span class="text-[10px] font-black uppercase tracking-widest"
                >Immediate Assistance</span
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
/* Cleaning up the number input appearance */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
