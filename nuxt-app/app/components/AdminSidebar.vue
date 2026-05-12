<script setup lang="ts">
import { computed, h, ref, watch } from "vue";
import { useRoute } from "vue-router";

const { t, locale, locales, setLocale } = useI18n();
const colorMode = useColorMode();
const isSettingsOpen = ref(false);
const isMobileMenuOpen = ref(false);

const { logout } = useAuth();
const route = useRoute();

const activeTab = computed(() => {
  if (route.path === "/admin" || route.path === "/admin/") return "overview";
  return route.path.split("/").pop() || "overview";
});

watch(
  () => route.path,
  () => {
    isMobileMenuOpen.value = false;
  },
);

const toggleColorMode = () => {
  colorMode.preference = colorMode.value === "dark" ? "light" : "dark";
};

const navItems = computed(() => [
  {
    id: "overview",
    label: t("adminbar.overview"),
    icon: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6",
  },
  {
    id: "users",
    label: t("adminbar.users"),
    icon: "M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z",
  },
  {
    id: "hospitals",
    label: t("adminbar.hospitals"),
    icon: "M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z",
  },
  {
    id: "doctors",
    label: t("adminbar.doctors"),
    icon: "M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z",
  },
  {
    id: "faq",
    label: t("adminbar.faq"),
    icon: "M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z",
  },
  {
    id: "analytics",
    label: t("adminbar.analytics"),
    icon: "M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z",
  },
  {
    id: "system-analytics",
    label: t("adminbar.systemanalytics"),
    icon: "M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z",
  },
]);

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

const flags: Record<string, any> = {
  en: () =>
    h("svg", { viewBox: "0 0 24 24", class: "w-5 h-5" }, [
      h("path", {
        d: "M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12Z",
        fill: "#F0F0F0",
      }),
      h("path", {
        d: "M23.898 10.435H13.565V.102a12.12 12.12 0 0 0-3.13 0v10.333H.102a12.12 12.12 0 0 0 0 3.13h10.333v10.333a12.12 12.12 0 0 0 3.13 0V13.565h10.333a12.12 12.12 0 0 0 0-3.13Z",
        fill: "#D80027",
      }),
    ]),
  np: () =>
    h("svg", { viewBox: "0 0 24 24", class: "w-5 h-5" }, [
      h("path", {
        d: "M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12Z",
        fill: "#F0F0F0",
      }),
      h("path", {
        d: "M20.87 12 9.198.329C3.923 1.591 0 6.337 0 11.999c0 6.628 5.373 12 12 12 2.514 0 4.847-.773 6.775-2.094L8.87 11.999h12Z",
        fill: "#D80027",
      }),
    ]),
};
</script>

<template>
  <div
    class="lg:hidden flex items-center justify-between p-4 border-b border-[var(--border)] bg-[var(--card)] sticky top-0 z-[60]"
  >
    <div class="flex items-center gap-3">
      <div
        class="w-8 h-8 bg-[var(--primary)] rounded-lg flex items-center justify-center text-white font-black text-xs"
      >
        M
      </div>
      <h2 class="text-lg font-black tracking-tighter">
        MediAI <span class="text-[var(--primary)]">Pro</span>
      </h2>
    </div>
    <button
      @click="isMobileMenuOpen = true"
      class="p-2 bg-[var(--border)]/30 rounded-xl"
    >
      <svg
        class="w-6 h-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2.5"
          d="M4 6h16M4 12h16m-7 6h7"
        />
      </svg>
    </button>
  </div>

  <transition name="fade">
    <div
      v-if="isMobileMenuOpen"
      @click="isMobileMenuOpen = false"
      class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[70] lg:hidden"
    ></div>
  </transition>

  <aside
    :class="[
      'fixed inset-y-0 left-0 z-[80] w-72 border-r border-[var(--border)] bg-[var(--card)] flex flex-col p-6 h-screen transition-transform duration-300',
      isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full',
      'lg:translate-x-0',
    ]"
  >
    <button
      @click="isMobileMenuOpen = false"
      class="lg:hidden absolute top-6 right-6 p-2 rounded-xl bg-[var(--border)]/30"
    >
      <svg
        class="w-5 h-5"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="3"
          d="M6 18L18 6M6 6l12 12"
        />
      </svg>
    </button>

    <div class="mb-10 px-2">
      <div
        class="w-10 h-10 bg-[var(--primary)] rounded-xl mb-4 flex items-center justify-center text-white font-black shadow-lg shadow-[var(--primary)]/20"
      >
        M
      </div>
      <h2 class="text-xl font-black tracking-tighter">
        MediAI <span class="text-[var(--primary)]">Pro</span>
      </h2>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 space-y-2 overflow-y-auto pr-2 custom-scrollbar">
      <NuxtLink
        v-for="item in navItems"
        :key="item.id"
        :to="item.id === 'overview' ? '/admin' : `/admin/${item.id}`"
        :class="[
          'w-full flex items-center gap-3 px-4 py-3 rounded-2xl font-bold transition-all text-sm',
          activeTab === item.id
            ? 'bg-[var(--primary)] text-white shadow-lg shadow-[var(--primary)]/20'
            : 'text-[var(--subtext)] hover:bg-[var(--border)] hover:text-[var(--text)]',
        ]"
      >
        <svg
          class="w-5 h-5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            :d="item.icon"
          />
        </svg>
        {{ item.label }}
      </NuxtLink>
    </nav>

    <!-- Footer Settings & Logout -->
    <div class="mt-auto pt-6 border-t border-[var(--border)] space-y-2">
      <div class="relative px-2">
        <button
          @click="isSettingsOpen = !isSettingsOpen"
          :class="[
            'w-full flex justify-between items-center px-4 py-3 text-sm font-bold rounded-2xl transition-all duration-200',
            isSettingsOpen
              ? 'bg-[var(--text)] text-[var(--card)] shadow-lg'
              : 'text-[var(--subtext)] hover:bg-[var(--border)] hover:text-[var(--text)]',
          ]"
        >
          <div class="flex items-center gap-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="feather feather-settings"
            >
              <circle cx="12" cy="12" r="3" />
              <path
                d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"
              />
            </svg>
            <span>Settings</span>
          </div>
          <svg
            :class="{ 'rotate-180': isSettingsOpen }"
            class="w-4 h-4 transition-transform duration-300"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              d="M19 9l-7 7-7-7"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>

        <transition name="pop-up">
          <div
            v-if="isSettingsOpen"
            class="absolute bottom-full left-0 mb-3 w-full p-2 bg-[var(--card)] border-2 border-[var(--border)] rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.2)] z-[90]"
          >
            <div
              class="px-3 py-2 text-[10px] font-black uppercase tracking-widest text-[var(--subtext)]"
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
              <span>{{
                colorMode.value === "dark" ? "Light Mode" : "Dark Mode"
              }}</span>
            </button>
            <div class="h-[1px] bg-[var(--border)] my-3 mx-2"></div>
            <div
              class="px-3 py-2 text-[10px] font-black uppercase tracking-widest text-[var(--subtext)]"
            >
              Language
            </div>
            <div class="grid grid-cols-1 gap-1">
              <button
                v-for="lang in locales"
                :key="lang.code"
                @click="setLocale(lang.code)"
                :class="[
                  'w-full flex items-center gap-3 p-3 text-xs rounded-xl transition-all border',
                  locale === lang.code
                    ? 'bg-[var(--primary)] border-[var(--primary)] text-white font-black'
                    : 'bg-transparent border-transparent text-[var(--subtext)] hover:bg-[var(--background)] hover:border-[var(--border)]',
                ]"
              >
                <component :is="flags[lang.code]" class="w-5" />
                {{ lang.name }}
              </button>
            </div>
          </div>
        </transition>
      </div>

      <div class="px-2 pb-2 lg:pb-0">
        <button
          @click="logout"
          class="w-full flex items-center gap-3 px-4 py-3 bg-red-50 text-red-600 dark:bg-red-500/10 dark:text-red-500 font-bold text-sm border border-transparent hover:border-red-500/20 rounded-2xl transition-all"
        >
          <svg
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2.5"
              d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
            />
          </svg>
          <span>Logout</span>
        </button>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 10px;
}

.pop-up-enter-active,
.pop-up-leave-active {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.pop-up-enter-from,
.pop-up-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
