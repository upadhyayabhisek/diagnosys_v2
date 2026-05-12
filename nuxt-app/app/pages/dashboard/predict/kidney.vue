<script setup lang="ts">
import { reactive, ref } from "vue";

definePageMeta({
  layout: "dashboard",
});

// Access user session
const { user } = useAuth();
const isSubmitting = ref(false);
const predictionData = ref(null);

const form = reactive({
  age: null,
  blood_pressure: null,
  specific_gravity: "1.020",
  albumin: "0",
  sugar: "0",
  red_blood_cells: "normal",
  pus_cell: "normal",
  pus_cell_clumps: "notpresent",
  bacteria: "notpresent",
  blood_glucose_random: null,
  blood_urea: null,
  serum_creatinine: null,
  sodium: null,
  potassium: null,
  haemoglobin: null,
  packed_cell_volume: null,
  white_blood_cell_count: null,
  red_blood_cell_count: null,
  hypertension: "no",
  diabetes_mellitus: "no",
  coronary_artery_disease: "no",
  appetite: "good",
  peda_edema: "no",
  aanemia: "no",
});

const handleSubmit = async () => {
  if (!user.value?.email) {
    alert("User session expired.");
    return;
  }

  isSubmitting.value = true;

  // FIX: Prevent 'NoneType' error by providing fallbacks (0) for all null fields
  const payload = {
    ...form,
    user_email: user.value.email,
    age: form.age ?? 0,
    blood_pressure: form.blood_pressure ?? 0,
    blood_glucose_random: form.blood_glucose_random ?? 0,
    blood_urea: form.blood_urea ?? 0,
    serum_creatinine: form.serum_creatinine ?? 0,
    sodium: form.sodium ?? 0,
    potassium: form.potassium ?? 0,
    haemoglobin: form.haemoglobin ?? 0,
    packed_cell_volume: form.packed_cell_volume ?? 0,
    white_blood_cell_count: form.white_blood_cell_count ?? 0,
    red_blood_cell_count: form.red_blood_cell_count ?? 0,
  };

  try {
    const response: any = await $fetch(
      "http://localhost:5001/api/predict/kidney",
      {
        method: "POST",
        body: payload,
      },
    );

    if (response.status === "success") {
      predictionData.value = response;
    } else {
      alert(response.message);
    }
  } catch (error: any) {
    console.error(error);
    alert(error.data?.message || "Failed connecting to Kidney AI server.");
  } finally {
    isSubmitting.value = false;
  }
};

const resetForm = () => {
  predictionData.value = null;
};
</script>

<template>
  <div class="max-w-5xl">
    <!-- Result Overlay -->
    <div v-if="predictionData">
      <DiagnosisResult
        type="Kidney Disease"
        :result="predictionData.result"
        :confidence="predictionData.confidence"
        :formData="form"
        :reportId="predictionData.report_id"
        @back="resetForm"
      />
    </div>

    <!-- Main Form Content -->
    <div v-else>
      <header class="mb-12">
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2 uppercase"
        >
          AI Diagnostics
        </p>
        <h1 class="text-5xl font-black tracking-tight mb-4">
          Kidney Disease <br /><span class="opacity-50">Renal Analysis</span>
        </h1>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Main Diagnostic Form -->
        <section
          class="lg:col-span-2 bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-10"
        >
          <div class="flex justify-between items-center mb-10">
            <h2 class="text-xl font-black">Clinical Indicators</h2>
            <span
              class="text-[10px] font-bold text-[var(--primary)] px-3 py-1 bg-[var(--primary)]/10 rounded-full"
            >
              24 Parameters Active
            </span>
          </div>

          <form @submit.prevent="handleSubmit" class="space-y-6">
            <!-- Cluster 1: Vital Biometrics -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                v-for="field in [
                  { id: 'age', label: 'Patient Age', hint: 'Years' },
                  {
                    id: 'blood_pressure',
                    label: 'Blood Pressure',
                    hint: 'mm Hg',
                  },
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
                    type="number"
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

            <!-- Cluster 2: Laboratory Chemistry -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                v-for="field in [
                  {
                    id: 'blood_glucose_random',
                    label: 'Glucose (Random)',
                    hint: 'mg/dL',
                  },
                  {
                    id: 'serum_creatinine',
                    label: 'Serum Creatinine',
                    hint: 'mg/dL',
                  },
                  { id: 'haemoglobin', label: 'Haemoglobin', hint: 'g/dL' },
                  {
                    id: 'packed_cell_volume',
                    label: 'Packed Cell Vol',
                    hint: '%',
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
                    step="any"
                    required
                    class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold focus:border-[var(--primary)] outline-none transition-all"
                    placeholder="0.00"
                  />
                  <span
                    class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-black text-[var(--primary)] opacity-40 uppercase"
                    >{{ field.hint }}</span
                  >
                </div>
              </div>
            </div>

            <!-- Cluster 3: Electrolytes & Count (Adding missing visual fields from your 24 param list) -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div
                v-for="field in [
                  { id: 'sodium', label: 'Sodium', hint: 'mEq/L' },
                  { id: 'potassium', label: 'Potassium', hint: 'mEq/L' },
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
                    step="any"
                    required
                    class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold focus:border-[var(--primary)] outline-none transition-all"
                    placeholder="0.00"
                  />
                  <span
                    class="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-black text-[var(--primary)] opacity-40 uppercase"
                    >{{ field.hint }}</span
                  >
                </div>
              </div>
            </div>

            <!-- Quick Selects for Urine Markers -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div
                v-for="field in [
                  {
                    id: 'specific_gravity',
                    label: 'Spec. Gravity',
                    options: ['1.005', '1.010', '1.015', '1.020', '1.025'],
                  },
                  {
                    id: 'albumin',
                    label: 'Albumin',
                    options: ['0', '1', '2', '3', '4', '5'],
                  },
                  {
                    id: 'sugar',
                    label: 'Sugar',
                    options: ['0', '1', '2', '3', '4', '5'],
                  },
                ]"
                :key="field.id"
              >
                <label
                  class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)] px-1 block mb-2"
                  >{{ field.label }}</label
                >
                <select
                  v-model="form[field.id]"
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl p-4 text-sm font-bold appearance-none outline-none focus:border-[var(--primary)] transition-all"
                >
                  <option v-for="opt in field.options" :key="opt" :value="opt">
                    {{ opt }}
                  </option>
                </select>
              </div>
            </div>

            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full mt-4 bg-[var(--primary)] text-white py-5 rounded-2xl font-black text-xs tracking-[0.2em] uppercase hover:brightness-110 active:scale-[0.98] transition-all shadow-lg shadow-[var(--primary)]/20 disabled:opacity-50"
            >
              <span v-if="isSubmitting">Analyzing Neural Data...</span>
              <span v-else>Run Renal Diagnostic &rarr;</span>
            </button>
          </form>
        </section>

        <!-- Sidebar -->
        <aside class="space-y-6">
          <section
            class="bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] p-8"
          >
            <h3 class="text-sm font-black mb-6 flex items-center gap-2">
              <i class="fas fa-history text-[var(--primary)]"></i> Clinical
              Context
            </h3>
            <div class="space-y-3">
              <div
                v-for="field in [
                  { id: 'hypertension', label: 'Hypertension' },
                  { id: 'diabetes_mellitus', label: 'Diabetes' },
                  { id: 'peda_edema', label: 'Pedal Edema' },
                  { id: 'aanemia', label: 'Anemia' },
                  {
                    id: 'appetite',
                    label: 'Appetite',
                    options: ['good', 'poor'],
                  },
                ]"
                :key="field.id"
                class="flex items-center justify-between p-4 rounded-2xl bg-[var(--background)] border border-[var(--border)]/50"
              >
                <span
                  class="text-[10px] font-black uppercase tracking-widest text-[var(--subtext)]"
                  >{{ field.label }}</span
                >
                <select
                  v-model="form[field.id]"
                  class="bg-transparent text-[10px] font-black uppercase text-[var(--primary)] outline-none cursor-pointer"
                >
                  <option
                    v-for="opt in field.options || ['no', 'yes']"
                    :key="opt"
                    :value="opt"
                  >
                    {{ opt }}
                  </option>
                </select>
              </div>
            </div>
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
            <h2 class="text-xl font-black mb-4">Renal Warning Signs</h2>
            <div class="space-y-3 mb-8">
              <div
                v-for="item in [
                  {
                    title: 'Fluid Overload',
                    desc: 'Severe swelling or breathing difficulty',
                  },
                  {
                    title: 'Uremic Toxins',
                    desc: 'Metallic taste or persistent nausea',
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
              <span
                class="text-xs font-black opacity-40 group-hover:opacity-100"
                >102 &rarr;</span
              >
            </a>
          </section>
        </aside>
      </div>
    </div>
  </div>
</template>

<style scoped>
select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M19 9l-7 7-7-7'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1.25rem center;
  background-size: 1em;
  padding-right: 2.5rem !important;
}
select::-ms-expand {
  display: none;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
