<script setup lang="ts">
import { computed, ref } from "vue";

definePageMeta({
  layout: "dashboard",
});

const { user } = useAuth();
const firstName = computed(() => user.value?.name?.split(" ")[0] || "User");

const form = ref({
  age: 24,
  gender: "male",
  weight: 72,
  height: 1.78,
  experience_level: "Beginner",
  target_muscle: "Full Body",
  difficulty: "Medium",
  frequency: 3,
  goal: "Strength",
});

const isAnalyzing = ref(false);
const recommendation = ref(null);

const bmi = computed(() => {
  if (!form.value.weight || !form.value.height) return "0.0";
  return (form.value.weight / (form.value.height * form.value.height)).toFixed(
    1,
  );
});

const estimatedMaxBPM = computed(() => 220 - form.value.age);

const handlePredict = async () => {
  isAnalyzing.value = true;
  try {
    const data = await $fetch("http://localhost:5001/recommend-workout", {
      method: "POST",
      body: {
        difficulty: form.value.experience_level,
        target_muscle: form.value.target_muscle,
        weight: form.value.weight,
      },
    });

    recommendation.value = data;
  } catch (e) {
    console.error("Prediction failed", e);
  } finally {
    isAnalyzing.value = false;
  }
};

const isSaving = ref(false);
const saveSuccess = ref(false);
const handleAddToPlan = async () => {
  if (!user.value?.email) return alert("Please log in first!");

  isSaving.value = true;
  saveSuccess.value = false;

  try {
    const response = await $fetch("http://localhost:5001/save-workout", {
      method: "POST",
      body: {
        email: user.value.email,
        difficulty: form.value.experience_level,
        recommendation: recommendation.value,
      },
    });

    if (response.status === "success") {
      saveSuccess.value = true;
      setTimeout(() => {
        saveSuccess.value = false;
      }, 3000);
    }
  } catch (e) {
    console.error("Save error:", e);
  } finally {
    isSaving.value = false;
  }
};
</script>

<template>
  <div class="max-w-6xl mx-auto pb-20">
    <header class="mb-12">
      <div class="flex items-center gap-4 mb-2">
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
        >
          Personalised Plan
        </p>
      </div>
      <h1 class="text-5xl font-black tracking-tight">
        Optimize Your <br /><span class="opacity-50">Performance</span>
      </h1>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
      <section class="lg:col-span-5 space-y-6 flex flex-col">
        <div
          class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8 flex-grow"
        >
          <h2
            class="text-[10px] font-black uppercase tracking-widest mb-8 flex items-center gap-2 text-[var(--subtext)]"
          >
            Biometrics & Goals
          </h2>

          <div class="space-y-5">
            <div class="grid grid-cols-2 gap-4">
              <AppSelect
                v-model="form.experience_level"
                label="Experience"
                :options="['Beginner', 'Intermediate', 'Advanced']"
              />

              <AppSelect
                v-model="form.target_muscle"
                label="Target"
                :options="['Chest', 'Legs', 'Back', 'Full Body']"
              />
            </div>

            <div class="grid grid-cols-3 gap-4">
              <div class="space-y-1.5">
                <label
                  class="text-[9px] font-black text-[var(--subtext)] uppercase ml-1"
                  >Kg</label
                >
                <input
                  v-model="form.weight"
                  type="number"
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl px-4 py-3.5 text-xs font-bold outline-none focus:border-[var(--primary)] transition-all"
                />
              </div>
              <div class="space-y-1.5">
                <label
                  class="text-[9px] font-black text-[var(--subtext)] uppercase ml-1"
                  >Height</label
                >
                <input
                  v-model="form.height"
                  type="number"
                  step="0.01"
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl px-4 py-3.5 text-xs font-bold outline-none focus:border-[var(--primary)] transition-all"
                />
              </div>
              <div class="space-y-1.5">
                <label
                  class="text-[9px] font-black text-[var(--subtext)] uppercase ml-1"
                  >Freq/Wk</label
                >
                <input
                  v-model="form.frequency"
                  type="number"
                  class="w-full bg-[var(--background)] border border-[var(--border)] rounded-2xl px-4 py-3.5 text-xs font-bold outline-none focus:border-[var(--primary)] transition-all"
                />
              </div>
            </div>

            <button
              @click="handlePredict"
              :disabled="isAnalyzing"
              class="w-full py-5 bg-[var(--text)] text-[var(--card)] rounded-2xl font-black text-xs uppercase tracking-widest hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center justify-center gap-3 mt-4 disabled:opacity-50"
            >
              <span
                v-if="isAnalyzing"
                class="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin"
              ></span>
              {{
                isAnalyzing
                  ? "Analyzing Performance..."
                  : "Generate AI Strategy"
              }}
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div
            class="p-6 bg-[var(--primary)]/5 border border-[var(--border)] rounded-[2.5rem]"
          >
            <p
              class="text-[9px] font-black text-[var(--primary)] uppercase tracking-widest mb-1"
            >
              BMI Index
            </p>
            <p class="text-4xl font-black tracking-tighter">{{ bmi }}</p>
          </div>
          <div class="p-6 bg-[var(--text)] text-[var(--card)] rounded-[2.5rem]">
            <p
              class="text-[9px] font-black opacity-60 uppercase tracking-widest mb-1"
            >
              Max BPM
            </p>
            <p class="text-4xl font-black tracking-tighter">
              {{ estimatedMaxBPM }}
            </p>
          </div>
        </div>
      </section>
      <section class="lg:col-span-7">
        <transition name="fade" mode="out-in">
          <div
            v-if="recommendation"
            class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-10 h-full relative overflow-hidden flex flex-col"
          >
            <div
              class="absolute -top-10 -right-10 opacity-[0.03] pointer-events-none"
            >
              <svg class="w-80 h-80" fill="currentColor" viewBox="0 0 24 24">
                <path d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>

            <div class="relative z-10 flex-grow">
              <div class="mb-8">
                <h2 class="text-4xl font-black tracking-tight uppercase">
                  Target: {{ recommendation.target }}
                </h2>
              </div>

              <div class="space-y-3 mb-10">
                <div
                  v-for="exercise in recommendation.exercises"
                  :key="exercise.name"
                  class="group flex items-center justify-between p-6 rounded-[2rem] bg-[var(--background)] border border-[var(--border)] hover:border-[var(--primary)] transition-all"
                >
                  <div class="flex items-center gap-4">
                    <div>
                      <p class="font-black text-sm">{{ exercise.name }}</p>
                      <p
                        class="text-[10px] text-[var(--subtext)] font-bold uppercase tracking-widest"
                      >
                        {{ exercise.sets }}
                      </p>
                    </div>
                  </div>
                  <p
                    class="text-xs font-black text-[var(--primary)] bg-[var(--primary)]/5 px-3 py-1 rounded-lg"
                  >
                    ~{{ exercise.calories }} KCAL
                  </p>
                </div>
              </div>
            </div>

            <div
              class="pt-8 border-t border-[var(--border)] flex justify-between items-center relative z-10"
            >
              <div>
                <p
                  class="text-[9px] font-black text-[var(--subtext)] uppercase tracking-widest mb-1"
                >
                  Total Burn Energy
                </p>
                <p
                  class="text-4xl font-black text-[var(--primary)] tracking-tighter"
                >
                  {{ recommendation.expected_burn
                  }}<span class="text-sm opacity-50 ml-1">KCAL</span>
                </p>
              </div>
              <button
                @click="handleAddToPlan"
                :disabled="isSaving || saveSuccess"
                class="px-8 py-4 transition-all rounded-2xl text-[10px] font-black uppercase tracking-widest flex items-center gap-3"
                :class="[
                  saveSuccess
                    ? 'bg-green-500 text-white'
                    : 'bg-[var(--text)] text-[var(--card)] hover:bg-[var(--primary)] hover:text-white',
                ]"
              >
                <span
                  v-if="isSaving"
                  class="w-3 h-3 border-2 border-current border-t-transparent rounded-full animate-spin"
                ></span>
                <svg
                  v-if="saveSuccess"
                  class="w-3 h-3"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="3"
                    d="M5 13l4 4L19 7"
                  />
                </svg>
                <span>
                  {{
                    isSaving
                      ? "Syncing..."
                      : saveSuccess
                        ? "Plan Updated"
                        : "Add to Daily Plan"
                  }}
                </span>
              </button>
            </div>
          </div>

          <div
            v-else
            class="h-full border-2 border-dashed border-[var(--border)] rounded-[3rem] flex flex-col items-center justify-center p-12 text-center opacity-40"
          >
            <div
              class="w-16 h-16 mb-6 rounded-full bg-[var(--border)] flex items-center justify-center"
            >
              <svg
                class="w-8 h-8 text-[var(--subtext)]"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
            </div>
            <p class="text-xs font-black uppercase tracking-[0.3em] mb-2">
              Awaiting Parameters
            </p>
            <p
              class="text-[10px] text-[var(--subtext)] font-medium max-w-[200px]"
            >
              Input your biometrics to generate a custom AI workout strategy.
            </p>
          </div>
        </transition>
      </section>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition:
    opacity 0.3s ease,
    transform 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
