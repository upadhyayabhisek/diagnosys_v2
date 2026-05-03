<script setup lang="ts">
import { h } from "vue";

const { locale, locales, setLocale } = useI18n();
const colorMode = useColorMode();
const isSettingsOpen = ref(false);

const { user, logout } = useAuth();

const adminName = computed(() => user.value?.name || "Admin");
const activeTab = ref("overview");

const toggleColorMode = () => {
  colorMode.preference = colorMode.value === "dark" ? "light" : "dark";
};

const navItems = [
  {
    id: "overview",
    label: "Overview",
    icon: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6",
  },
  {
    id: "users",
    label: "User Management",
    icon: "M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z",
  },
  {
    id: "hospitals",
    label: "Partner Hospitals",
    icon: "M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z",
  },
  {
    id: "doctors",
    label: "Medical Staff",
    icon: "M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z",
  },
  {
    id: "faq",
    label: "FAQs",
    icon: "M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z",
  },
  {
    id: "legal",
    label: "Terms & Policies",
    icon: "M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z",
  },
  {
    id: "analytics",
    label: "Health Trends",
    icon: "M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z",
  },
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

<template>
  <div
    class="flex h-screen bg-[var(--background)] text-[var(--text)] overflow-hidden"
  >
    <aside
      class="w-72 border-r border-[var(--border)] bg-[var(--card)]/50 backdrop-blur-xl flex flex-col p-6"
    >
      <div class="mb-10 px-2">
        <div
          class="w-10 h-10 bg-[var(--primary)] rounded-xl mb-4 flex items-center justify-center text-white font-black"
        >
          M
        </div>
        <h2 class="text-xl font-black tracking-tighter">
          MediAI <span class="text-[var(--primary)]">Pro</span>
        </h2>
      </div>

      <nav class="flex-1 space-y-2">
        <button
          v-for="item in navItems"
          :key="item.id"
          @click="activeTab = item.id"
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
        </button>
      </nav>

      <div class="mt-auto pt-6 border-t border-[var(--border)] space-y-2">
        <!-- SETTINGS GROUP -->
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
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2.5"
                  d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2.5"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
              <span>Settings</span>
            </div>
            <span
              :class="{ 'rotate-180': isSettingsOpen }"
              class="transition-transform duration-300 text-xs"
            >
              <svg
                class="w-4 h-4"
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
            </span>
          </button>

          <!-- SOLID FLOATING PANEL -->
          <transition name="pop-up">
            <div
              v-if="isSettingsOpen"
              class="absolute bottom-full left-0 mb-3 w-full p-2 bg-[var(--card)] border-2 border-[var(--border)] rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.2)] z-50"
            >
              <!-- Appearance Section -->
              <div
                class="px-3 py-2 text-[10px] font-black uppercase tracking-widest text-[var(--subtext)]"
              >
                Appearance
              </div>
              <button
                @click="toggleColorMode"
                class="w-full flex items-center gap-3 p-3 text-xs font-bold rounded-xl bg-[var(--background)] border border-[var(--border)] hover:border-[var(--primary)] transition-all"
              >
                <span>{{ colorMode.value === "dark" ? "☀️" : "🌙" }}</span>
                {{ colorMode.value === "dark" ? "Light Mode" : "Dark Mode" }}
              </button>

              <div class="h-[1px] bg-[var(--border)] my-3 mx-2"></div>

              <!-- Language Section -->
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
                      ? 'bg-[var(--primary)] border-[var(--primary)] text-white shadow-md font-black'
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

        <!-- SOLID LOGOUT BUTTON -->
        <div class="px-2">
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

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 overflow-y-auto p-8 md:p-12">
      <header class="mb-12">
        <p
          class="text-[10px] font-black tracking-[0.2em] text-[var(--primary)] mb-2"
        >
          Admin Panel
        </p>
        <h1 class="text-5xl font-black tracking-tight mb-4">
          Welcome back, <br /><span class="opacity-50">{{ adminName }}</span>
        </h1>
      </header>

      <!-- Dashboard Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div
          v-for="i in 3"
          :key="i"
          class="p-8 bg-[var(--card)] border border-[var(--border)] rounded-[2.5rem] hover:scale-[1.02] transition-transform cursor-pointer"
        >
          <div
            class="w-12 h-12 rounded-2xl bg-[var(--primary)]/10 flex items-center justify-center mb-6 text-[var(--primary)]"
          >
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
          <h3
            class="text-[10px] font-bold uppercase text-[var(--subtext)] mb-1"
          >
            Growth Metric {{ i }}
          </h3>
          <p class="text-3xl font-black tracking-tight">+{{ 12 * i }}%</p>
        </div>
      </div>

      <!-- Mock Data Section -->
      <section
        class="bg-[var(--card)] border border-[var(--border)] rounded-[3rem] p-8"
      >
        <div class="flex justify-between items-center mb-8">
          <h2 class="text-xl font-black">Recent System Activity</h2>
          <button
            class="px-4 py-2 bg-[var(--text)] text-[var(--background)] rounded-full text-xs font-bold"
          >
            View Reports
          </button>
        </div>
        <div class="space-y-4">
          <div
            v-for="n in 4"
            :key="n"
            class="flex items-center justify-between p-4 rounded-2xl border border-[var(--border)]/50 hover:bg-[var(--border)]/20 transition-colors"
          >
            <div class="flex items-center gap-4">
              <div
                class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-500 flex items-center justify-center font-bold text-xs"
              >
                U
              </div>
              <div>
                <p class="text-sm font-bold">New User Registered</p>
                <p class="text-[10px] text-[var(--subtext)] font-medium">
                  user_{{ n }}42@example.com
                </p>
              </div>
            </div>
            <p class="text-[10px] font-bold text-[var(--subtext)]">
              2 mins ago
            </p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>
