<template>
  <div
    class="min-h-screen bg-[var(--background)] text-[var(--text)] pt-32 pb-20 px-6 transition-colors duration-500"
  >
    <div class="max-w-7xl mx-auto text-center mb-16">
      <h1
        class="text-4xl md:text-5xl font-black mb-4 bg-gradient-to-r from-[var(--text)] to-[var(--subtext)] bg-clip-text text-transparent tracking-tighter"
      >
        {{ $t("prediction.title") || "Disease Prediction Portal" }}
      </h1>
      <p
        class="text-[var(--subtext)] max-w-2xl mx-auto font-medium leading-relaxed"
      >
        {{
          $t("prediction.subtitle") ||
          "Early detection is the first step toward a healthier life. Select a category to begin your assessment."
        }}
      </p>
    </div>

    <div
      class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto"
    >
      <div
        v-for="disease in diseases"
        :key="disease.id"
        class="group relative theme-card rounded-[2.5rem] p-8 hover:border-[var(--primary)] transition-all duration-500 shadow-xl shadow-black/5 hover:shadow-[var(--primary)]/5"
      >
        <div class="flex items-center justify-between mb-8">
          <div
            class="h-12 w-12 rounded-2xl bg-[var(--primary)]/10 flex items-center justify-center text-[var(--primary)] group-hover:scale-110 transition-transform"
          >
            <i :class="['fas', disease.icon, 'text-xl']"></i>
          </div>
          <span
            class="text-[10px] font-black uppercase tracking-[0.2em] theme-text-muted"
          >
            {{ disease.category }}
          </span>
        </div>

        <h2 class="text-2xl font-bold mb-3 tracking-tight">
          {{ $t(`prediction.${disease.id}.name`) }}
        </h2>
        <p class="theme-text-muted text-sm leading-relaxed mb-6 font-medium">
          {{ $t(`prediction.${disease.id}.intro`) }}
        </p>

        <div class="mb-8">
          <h3
            class="text-[10px] font-black uppercase tracking-widest theme-text-muted mb-4"
          >
            Risk Factors
          </h3>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="risk in disease.risks"
              :key="risk"
              class="text-[11px] font-bold bg-[var(--bg-secondary)] border border-[var(--border)] px-3 py-1.5 rounded-xl theme-text-muted"
            >
              {{ risk }}
            </span>
          </div>
        </div>

        <div class="space-y-1 mb-10">
          <Disclosure
            v-for="section in ['symptoms', 'prevention']"
            :key="section"
            v-slot="{ open }"
          >
            <DisclosureButton
              class="flex items-center justify-between w-full text-left py-4 border-b border-[var(--border)] group-hover:border-[var(--primary)]/30 transition-colors focus:outline-none"
            >
              <span class="text-sm font-bold tracking-tight">{{
                $t(`prediction.${section}`)
              }}</span>
              <i
                class="fas fa-chevron-right text-[10px] transition-transform duration-300 opacity-50 theme-text-muted"
                :class="{ 'rotate-90': open }"
              ></i>
            </DisclosureButton>

            <transition
              enter-active-class="transition duration-200 ease-out"
              enter-from-class="transform -translate-y-2 opacity-0"
              enter-to-class="transform translate-y-0 opacity-100"
            >
              <DisclosurePanel
                class="pt-4 pb-2 text-[13px] theme-text-muted leading-relaxed font-medium"
              >
                <ul class="space-y-2">
                  <li
                    v-for="tip in disease[section]"
                    :key="tip"
                    class="flex items-start gap-2"
                  >
                    <span
                      class="h-1.5 w-1.5 rounded-full bg-[var(--primary)] mt-1.5 shrink-0"
                    ></span>
                    {{ tip }}
                  </li>
                </ul>
              </DisclosurePanel>
            </transition>
          </Disclosure>
        </div>

        <NuxtLink
          :to="disease.link"
          class="block w-full text-center bg-[var(--primary)] hover:bg-[var(--primary-hover)] text-white font-bold py-4 rounded-2xl transition-all active:scale-[0.98] shadow-lg shadow-[var(--primary)]/20"
        >
          {{ $t("prediction.button_text") }}
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/vue";

const diseases = [
  {
    id: "kidney",
    icon: "fa-organ-vines",
    category: "Renal Health",
    link: "/kidney_form",
    risks: ["Diabetes", "Obesity", "Smoking"],
    symptoms: ["Swelling of feet", "Fatigue", "Urination changes"],
    prevention: ["Healthy BP", "Hydration", "Avoid painkillers"],
  },
  {
    id: "liver",
    icon: "fa-bacteria",
    category: "Hepatic Health",
    link: "/liver_form",
    risks: ["Alcohol", "Hepatitis", "Fatty Liver"],
    symptoms: ["Jaundice", "Abdominal pain", "Dark urine"],
    prevention: ["Limit Alcohol", "Vaccination", "Healthy Diet"],
  },
  {
    id: "diabetes",
    icon: "fa-vial",
    category: "Metabolic Health",
    link: "/diabetes_form",
    risks: ["Genetics", "Inactivity", "Age 45+"],
    symptoms: ["Thirst", "Frequent urination", "Blurred vision"],
    prevention: ["Fiber-rich diet", "Exercise", "Weight control"],
  },
];
</script>
