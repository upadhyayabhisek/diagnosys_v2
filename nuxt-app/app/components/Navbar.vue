<template>
  <!-- FULL WIDTH NAVBAR -->
  <div
    class="sticky top-0 z-50 w-full border-b backdrop-blur-xl bg-[var(--bg)]/70 border-[var(--border)]"
  >
    <!-- CENTERED CONTENT -->
    <nav class="mx-auto max-w-7xl px-6 md:px-8 py-4">
      <div class="flex items-center justify-between">
        <!-- LOGO -->
        <NuxtLink to="/" class="flex items-center gap-2 group shrink-0">
          <div
            class="h-9 w-9 bg-[var(--primary)] rounded-xl flex items-center justify-center font-black text-white transition-all duration-300 group-hover:rotate-12 shadow-lg shadow-blue-500/20"
          >
            M
          </div>
          <span class="text-xl font-bold tracking-tight text-[var(--text)]">
            MediAI
          </span>
        </NuxtLink>

        <div class="hidden lg:flex items-center gap-1 p-1 rounded-2xl">
          <NuxtLink
            v-for="item in menuItems"
            :key="item.to"
            :to="item.to"
            class="px-4 py-2 text-sm font-medium rounded-xl text-[var(--subtext)] hover:text-[var(--text)] hover:bg-[var(--primary)]/10 transition-all"
            active-class="active-nav-link"
          >
            {{ $t(item.label) || item.fall }}
          </NuxtLink>
        </div>

        <div class="hidden md:flex items-center gap-3">
          <NuxtLink
            to="/login"
            class="text-sm font-medium text-[var(--subtext)] hover:text-[var(--text)] transition"
          >
            {{ $t("nav.login") }}
          </NuxtLink>

          <NuxtLink
            to="/signup"
            class="px-5 py-2 text-sm font-bold text-white rounded-xl bg-[var(--primary)] hover:opacity-90 shadow-lg shadow-blue-500/10 active:scale-95 transition"
          >
            {{ $t("nav.signup") }}
          </NuxtLink>

          <div class="w-[1px] h-5 bg-[var(--border)] mx-1"></div>

          <div
            class="relative"
            @mouseenter="isSettingsOpen = true"
            @mouseleave="isSettingsOpen = false"
          >
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl border bg-[var(--card)] border-[var(--border)] text-[var(--subtext)] hover:text-[var(--text)] transition"
            >
              <SettingsIcon class="w-5 h-5" />
            </button>

            <transition name="fade-slide">
              <div
                v-show="isSettingsOpen"
                class="absolute right-0 mt-3 w-56 p-2 rounded-2xl border bg-[var(--card)] border-[var(--border)] shadow-2xl z-50"
              >
                <div
                  class="px-3 py-2 text-[10px] font-bold uppercase text-[var(--subtext)]"
                >
                  Appearance
                </div>

                <button
                  @click="toggleColorMode"
                  class="w-full flex items-center gap-3 px-3 py-2.5 text-sm rounded-xl text-[var(--subtext)] hover:bg-[var(--primary)]/10 hover:text-[var(--text)] transition mb-2"
                >
                  <component
                    :is="colorMode.value === 'dark' ? SunIcon : MoonIcon"
                    class="w-4 h-4"
                  />
                  <span>
                    Switch to
                    {{ colorMode.value === "dark" ? "Light" : "Dark" }}
                  </span>
                </button>

                <div class="h-[1px] bg-[var(--border)] my-1"></div>

                <div
                  class="px-3 py-2 text-[10px] font-bold uppercase text-[var(--subtext)]"
                >
                  Language
                </div>

                <button
                  v-for="lang in supportedLocales"
                  :key="lang.code"
                  @click="setLocale(lang.code)"
                  class="w-full flex items-center gap-3 px-3 py-2.5 text-sm rounded-xl transition"
                  :class="
                    locale === lang.code
                      ? 'text-[var(--primary)] bg-[var(--primary)]/15 font-semibold'
                      : 'text-[var(--subtext)] hover:bg-[var(--primary)]/5 hover:text-[var(--text)]'
                  "
                >
                  <component :is="flags[lang.code]" class="w-4 h-3" />
                  <span class="flex-1 text-left">{{ lang.name }}</span>
                </button>
              </div>
            </transition>
          </div>
        </div>

        <button
          @click="isMobileOpen = !isMobileOpen"
          class="lg:hidden w-10 h-10 flex items-center justify-center rounded-xl border bg-[var(--card)] border-[var(--border)] text-[var(--subtext)] active:scale-90 transition"
        >
          <svg
            width="24"
            height="24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              :d="
                isMobileOpen
                  ? 'M6 18L18 6M6 6l12 12'
                  : 'M4 7H20M4 12H15M4 17H20'
              "
            />
          </svg>
        </button>
      </div>
    </nav>

    <transition name="fade-slide">
      <div v-if="isMobileOpen" class="lg:hidden px-6 md:px-8 pb-6">
        <div
          class="mx-auto max-w-7xl p-6 rounded-3xl border bg-[var(--card)] border-[var(--border)] shadow-xl flex flex-col gap-6"
        >
          <NuxtLink
            v-for="item in menuItems"
            :key="item.to"
            :to="item.to"
            @click="isMobileOpen = false"
            class="px-4 py-3 text-lg rounded-xl text-[var(--subtext)] hover:bg-[var(--bg-secondary)] hover:text-[var(--text)] transition"
          >
            {{ $t(item.label) || item.fall }}
          </NuxtLink>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
const { locale, locales, setLocale } = useI18n();
const supportedLocales = computed(() => locales.value);
const colorMode = useColorMode();

const isSettingsOpen = ref(false);
const isMobileOpen = ref(false);

const toggleColorMode = () => {
  colorMode.preference = colorMode.value === "dark" ? "light" : "dark";
};

// Icons
const SettingsIcon = () =>
  h(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      fill: "none",
      viewBox: "0 0 24 24",
      stroke: "currentColor",
    },
    [
      h("path", {
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "stroke-width": "2",
        d: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z",
      }),
      h("path", {
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "stroke-width": "2",
        d: "M15 12a3 3 0 11-6 0 3 3 0 016 0z",
      }),
    ],
  );

const SunIcon = () =>
  h(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      fill: "none",
      viewBox: "0 0 24 24",
      stroke: "currentColor",
    },
    [
      h("path", {
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "stroke-width": "2",
        d: "M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.364l-.707-.707M15 12a3 3 0 11-6 0 3 3 0 016 0z",
      }),
    ],
  );

const MoonIcon = () =>
  h(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      fill: "none",
      viewBox: "0 0 24 24",
      stroke: "currentColor",
    },
    [
      h("path", {
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "stroke-width": "2",
        d: "M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z",
      }),
    ],
  );

const menuItems = [
  { to: "/", label: "nav.home", fall: "Home" },
  { to: "/prediction", label: "nav.prediction", fall: "Prediction" },
  { to: "/insights", label: "nav.insights", fall: "Insights" },
  { to: "/exercise", label: "nav.exercise", fall: "Exercise" },
];

const flags = {
  en: () =>
    h("svg", { viewBox: "0 0 24 24", width: "24", height: "24" }, [
      h("g", [
        h("path", {
          d: "M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12Z",
          fill: "#F0F0F0",
        }),
        h("path", {
          d: "M2.48 4.693A11.956 11.956 0 0 0 .413 8.868h6.243L2.48 4.693Zm21.106 4.176a11.957 11.957 0 0 0-2.067-4.176L17.344 8.87h6.242ZM.413 15.13a11.957 11.957 0 0 0 2.067 4.176l4.176-4.176H.413ZM19.305 2.48A11.957 11.957 0 0 0 15.13.412v6.243l4.175-4.175ZM4.693 21.518a11.957 11.957 0 0 0 4.176 2.067v-6.243l-4.176 4.176ZM8.869.412A11.957 11.957 0 0 0 4.693 2.48L8.87 6.655V.412Zm6.261 23.173a11.96 11.96 0 0 0 4.175-2.067l-4.175-4.176v6.243Zm2.214-8.455 4.175 4.176a11.957 11.957 0 0 0 2.067-4.176h-6.242Z",
          fill: "#0052B4",
        }),
        h("path", {
          d: "M23.898 10.435H13.565V.102a12.12 12.12 0 0 0-3.13 0v10.333H.102a12.12 12.12 0 0 0 0 3.13h10.333v10.333a12.12 12.12 0 0 0 3.13 0V13.565h10.333a12.12 12.12 0 0 0 0-3.13Z",
          fill: "#D80027",
        }),
        h("path", {
          d: "m15.13 15.131 5.356 5.355c.246-.246.48-.503.705-.77l-4.584-4.585H15.13Zm-6.26 0-5.355 5.355c.246.246.503.481.77.705l4.585-4.584V15.13Zm0-6.261v-.001L3.515 3.514a12.03 12.03 0 0 0-.705.77L7.394 8.87H8.87Zm6.26 0 5.356-5.355a12.023 12.023 0 0 0-.77-.705L15.13 7.394V8.87Z",
          fill: "#D80027",
        }),
      ]),
    ]),
  np: () =>
    h("svg", { viewBox: "0 0 24 24", width: "24", height: "24" }, [
      h("g", [
        h("path", {
          d: "M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12Z",
          fill: "#F0F0F0",
        }),
        h("path", {
          d: "M23.93 13.304 10.77.062c-.594.06-1.175.164-1.74.308C3.839 1.692 0 12 0 12s16.8 11.242 18.716 9.945c.384-.26.752-.54 1.102-.842l-7.8-7.799H23.93Z",
          fill: "#0052B4",
        }),
        h("path", {
          d: "M20.87 12 9.198.329C3.923 1.591 0 6.337 0 11.999c0 6.628 5.373 12 12 12 2.514 0 4.847-.773 6.775-2.094L8.87 11.999h12Z",
          fill: "#D80027",
        }),
        h("path", {
          d: "m11.413 17.717-1.466-.689.78-1.42-1.591.305-.202-1.608-1.108 1.183-1.109-1.183-.201 1.608-1.592-.304.78 1.419-1.465.69 1.466.689-.78 1.419 1.59-.304.202 1.607 1.109-1.182 1.108 1.182.202-1.607 1.591.304-.78-1.42 1.466-.689Zm-.979-11.062-1.066-.501.568-1.033-1.158.222-.146-1.17-.806.86-.807-.86-.146 1.17-1.158-.222.568 1.033-1.066.5 2.609.523 2.608-.522Z",
          fill: "#F0F0F0",
        }),
        h("path", {
          d: "M10.957 6.655a3.13 3.13 0 0 1-6.26 0",
          fill: "#F0F0F0",
        }),
      ]),
    ]),
};
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.2s ease-out;
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(8px) scale(0.95);
}

/* Custom class for active NuxtLink to ensure it uses CSS variables correctly */
.active-nav-link {
  color: var(--primary) !important;
}
</style>
