<script setup lang="ts">
import { computed, h, ref, watch } from "vue";
import { useRoute } from "vue-router";
const { t, locale, locales, setLocale } = useI18n();
const colorMode = useColorMode();
const { logout } = useAuth();
const route = useRoute();

const isSettingsOpen = ref(false);
const isPredictionsOpen = ref(true);
const isMobileMenuOpen = ref(false);
const activeTab = computed(() => {
  if (route.path === "/dashboard" || route.path === "/dashboard/")
    return "overview";
  return route.path.split("/").pop() || "overview";
});

const activeTabIsDiagnostic = computed(() => {
  return predictionSubItems.some((sub) => sub.id === activeTab.value);
});
watch(
  () => route.path,
  () => {
    isMobileMenuOpen.value = false;
  },
);
const toggleColorMode = () => {
  colorMode.preference = colorMode.preference === "dark" ? "light" : "dark";
};
const navItems = computed(() => [
  {
    id: "overview",
    label: "My Health Overview",
    path: "/dashboard",
    icon: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6",
  },
  {
    id: "exercise",
    label: "Exercise Plan",
    path: "/dashboard/exercise",
    icon: "M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.048 8.287 8.287 0 0 0 9 9.6a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z",
  },
  {
    id: "history",
    label: "Report History",
    path: "/dashboard/predict/history",
    icon: "M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25",
  },
  {
    id: "records",
    label: "Medical Records",
    path: "/dashboard/records",
    icon: "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
  },
  {
    id: "hospitals",
    label: "Nearby Facilities",
    path: "/dashboard/hospitals",
    icon: "M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z",
  },
]);

const predictionSubItems = [
  {
    id: "diabetes",
    label: "Diabetes Analysis",
    path: "/dashboard/predict/diabetes",
  },
  { id: "liver", label: "Liver Function", path: "/dashboard/predict/liver" },
  { id: "kidney", label: "Kidney Health", path: "/dashboard/predict/kidney" },
];
const SunIcon = () =>
  h(
    "svg",
    {
      fill: "none",
      viewBox: "0 0 24 24",
      stroke: "currentColor",
      class: "w-4 h-4",
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
      fill: "none",
      viewBox: "0 0 24 24",
      stroke: "currentColor",
      class: "w-4 h-4",
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
        class="w-8 h-8 bg-[var(--primary)] rounded-lg flex items-center justify-center text-white font-black"
      >
        M
      </div>
      <h2 class="text-lg font-black tracking-tighter">MediAI</h2>
    </div>
    <button
      @click="isMobileMenuOpen = true"
      class="p-2 bg-[var(--border)]/50 rounded-xl"
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
      'fixed inset-y-0 left-0 z-[80] w-72 border-r border-[var(--border)] bg-[var(--card)] lg:bg-[var(--card)]/50 backdrop-blur-xl flex flex-col p-6 h-screen transition-transform duration-300 lg:translate-x-0 lg:static',
      isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full',
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
        MediAI <span class="text-[var(--primary)] font-bold">User</span>
      </h2>
    </div>
    <nav class="flex-1 space-y-2 overflow-y-auto pr-2 custom-scrollbar">
      <NuxtLink
        :to="navItems[0].path"
        :class="[
          'w-full flex items-center gap-3 px-4 py-3 rounded-2xl font-bold transition-all text-sm',
          activeTab === navItems[0].id
            ? 'bg-[var(--primary)] text-white shadow-lg shadow-[var(--primary)]/20'
            : 'text-[var(--subtext)] hover:bg-[var(--border)] hover:text-[var(--text)]',
        ]"
      >
        <svg
          class="w-5 h-5"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            :d="navItems[0].icon"
          />
        </svg>
        {{ navItems[0].label }}
      </NuxtLink>
      <div class="space-y-1">
        <button
          @click="isPredictionsOpen = !isPredictionsOpen"
          :class="[
            'w-full flex items-center justify-between px-4 py-3 rounded-2xl font-bold text-sm transition-all',
            activeTabIsDiagnostic
              ? 'text-[var(--text)] bg-[var(--border)]/50'
              : 'text-[var(--subtext)] hover:bg-[var(--border)] hover:text-[var(--text)]',
          ]"
        >
          <div class="flex items-center gap-3">
            <svg
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"
              />
            </svg>
            <span>AI Diagnostics</span>
          </div>
          <svg
            :class="{ 'rotate-180': isPredictionsOpen }"
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

        <transition name="dropdown">
          <div
            v-if="isPredictionsOpen"
            class="ml-4 border-l-2 border-[var(--border)] space-y-1 my-1"
          >
            <NuxtLink
              v-for="sub in predictionSubItems"
              :key="sub.id"
              :to="sub.path"
              :class="[
                'block px-6 py-2.5 text-xs font-bold transition-all rounded-r-xl',
                activeTab === sub.id
                  ? 'text-[var(--primary)] bg-[var(--primary)]/10 border-l-2 border-[var(--primary)] -ml-[2px]'
                  : 'text-[var(--subtext)] hover:text-[var(--text)] hover:bg-[var(--border)]/30',
              ]"
            >
              {{ sub.label }}
            </NuxtLink>
          </div>
        </transition>
      </div>
      <NuxtLink
        v-for="item in navItems.slice(1)"
        :key="item.id"
        :to="item.path"
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
          stroke-width="2"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" :d="item.icon" />
        </svg>
        {{ item.label }}
      </NuxtLink>
    </nav>

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
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
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

        <transition name="pop">
          <div
            v-if="isSettingsOpen"
            class="absolute bottom-full left-0 mb-3 w-full p-2 bg-[var(--card)] border-2 border-[var(--border)] rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.2)] z-50"
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
                    ? 'bg-[var(--primary)] border-[var(--primary)] text-white font-black shadow-md'
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

      <div class="px-2">
        <button
          @click="logout"
          class="w-full flex items-center gap-3 px-4 py-3 bg-red-50 text-red-600 dark:bg-red-500/10 dark:text-red-500 font-bold text-sm border border-transparent hover:border-red-500/20 rounded-2xl transition-all"
        >
          <svg
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            stroke-width="2.5"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
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

.pop-enter-active,
.pop-leave-active {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.pop-enter-from,
.pop-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease-out;
  max-height: 200px;
  overflow: hidden;
}
.dropdown-enter-from,
.dropdown-leave-to {
  max-height: 0;
  opacity: 0;
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
