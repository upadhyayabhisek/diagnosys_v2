<template>
  <footer
    class="border-t border-[var(--border)] bg-[var(--bg)] pt-16 pb-12 mt-20 transition-colors duration-300"
  >
    <div class="max-w-7xl mx-auto px-8">
      <div class="flex flex-col lg:flex-row justify-between gap-12 pb-16">
        <div class="max-w-sm">
          <NuxtLink to="/" class="flex items-center gap-2 group mb-6">
            <div
              class="h-9 w-9 bg-[var(--primary)] rounded-xl flex items-center justify-center font-black text-white shadow-lg shadow-blue-500/20 transition-all group-hover:scale-110 group-hover:rotate-3"
            >
              M
            </div>
            <span class="font-bold text-2xl tracking-tighter text-[var(--text)]"
              >MediAI</span
            >
          </NuxtLink>
          <p class="text-[var(--subtext)] text-sm leading-relaxed mb-6">
            {{ t("footer.description") }}
          </p>
          <div class="flex items-center gap-4 text-[var(--subtext)]">
            <a
              href="#"
              class="hover:text-[var(--primary)] transition-colors"
              aria-label="X"
            >
              <!-- X icon -->x
            </a>
            <a
              href="#"
              class="hover:text-[var(--primary)] transition-colors"
              aria-label="GitHub"
            >
              <!-- GitHub icon -->github
            </a>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-16 lg:gap-24">
          <div class="flex flex-col gap-4">
            <span
              class="text-[10px] font-black uppercase tracking-[0.2em] text-[var(--subtext)]"
              >{{ t("footer.compliance") }}</span
            >
            <div class="flex flex-col gap-3">
              <NuxtLink
                to="/privacy"
                class="text-sm font-medium text-[var(--text)] hover:text-[var(--primary)] transition-colors"
                >{{ t("footer.privacyPolicy") }}</NuxtLink
              >
              <NuxtLink
                to="/terms"
                class="text-sm font-medium text-[var(--text)] hover:text-[var(--primary)] transition-colors"
                >{{ t("footer.termsOfService") }}</NuxtLink
              >
            </div>
          </div>

          <div class="flex flex-col gap-4">
            <span
              class="text-[10px] font-black uppercase tracking-[0.2em] text-[var(--subtext)]"
              >{{ t("footer.assistance") }}</span
            >
            <div class="flex flex-col gap-3">
              <NuxtLink
                to="/support"
                class="text-sm font-medium text-[var(--text)] hover:text-[var(--primary)] transition-colors"
                >{{ t("footer.helpCenter") }}</NuxtLink
              >
              <NuxtLink
                to="/emergency"
                class="text-sm font-bold text-red-500 hover:text-red-400 transition-colors flex items-center gap-1.5"
              >
                {{ t("footer.emergencyInfo") }}
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>

      <div class="pt-8 border-t border-[var(--border)] flex flex-col gap-8">
        <p
          class="text-[var(--subtext)]/60 text-[11px] leading-relaxed italic max-w-4xl"
        >
          {{ t("footer.disclaimer") }}
        </p>

        <div
          class="flex flex-col md:flex-row justify-between items-center gap-6"
        >
          <div class="flex flex-col md:items-start gap-1">
            <p class="text-[var(--subtext)] text-xs font-semibold">
              {{ t("footer.copyright") }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const { t, locale } = useI18n();
</script>
