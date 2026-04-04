<script setup lang="ts">
defineProps<{ type: "login" | "signup" }>();

const step = ref(1);

// Standardized styles for the "No-Scroll" look
const inputClass =
  "w-full p-3.5 bg-[var(--card)] border border-[var(--border)] rounded-2xl text-[var(--text)] focus:ring-2 focus:ring-[var(--primary)]/30 outline-none transition-all";
const labelClass =
  "text-[10px] font-bold uppercase tracking-widest text-[var(--subtext)] ml-1 mb-1 block";
</script>

<template>
  <div
    class="flex flex-col md:flex-row w-full min-h-[80vh] bg-[var(--background)] rounded-[2.5rem] overflow-hidden border border-[var(--border)] my-4"
  >
    <div
      class="hidden md:flex md:w-1/2 relative bg-[var(--primary)] items-center justify-center p-12"
    >
      <div class="absolute inset-0 z-0">
        <img
          src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80"
          class="w-full h-full object-cover opacity-30 mix-blend-overlay"
        />
      </div>

      <div class="relative z-10 text-white">
        <h1 class="text-5xl font-black tracking-tighter mb-4 leading-tight">
          Elevate Your <br />
          <span class="text-emerald-300">Wellbeing.</span>
        </h1>
        <p class="text-lg text-white/80 font-light max-w-sm">
          Join thousands tracking their health in one unified dashboard.
        </p>
      </div>
    </div>

    <div
      class="w-full md:w-1/2 flex items-center justify-center p-8 md:p-16 bg-[var(--card)]/30"
    >
      <div class="w-full max-w-sm">
        <div class="mb-8">
          <h2 class="text-3xl font-black text-[var(--text)] tracking-tight">
            {{ type === "login" ? "Welcome Back." : "Get Started." }}
          </h2>
        </div>

        <form class="space-y-5" @submit.prevent>
          <template v-if="type === 'login'">
            <div class="space-y-4">
              <div>
                <label :class="labelClass">Email</label>
                <input
                  type="email"
                  placeholder="name@example.com"
                  :class="inputClass"
                />
              </div>
              <div>
                <label :class="labelClass">Password</label>
                <input
                  type="password"
                  placeholder="••••••••"
                  :class="inputClass"
                />
              </div>
            </div>
          </template>

          <template v-else>
            <div v-if="step === 1" class="space-y-4">
              <div>
                <label :class="labelClass">Full Name</label>
                <input type="text" placeholder="John Doe" :class="inputClass" />
              </div>
              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label :class="labelClass">Birthday</label>
                  <input type="date" :class="inputClass" />
                </div>
                <div>
                  <label :class="labelClass">Gender</label>
                  <select :class="inputClass">
                    <option disabled selected>Select</option>
                    <option>Male</option>
                    <option>Female</option>
                  </select>
                </div>
              </div>
              <button
                type="button"
                @click="step = 2"
                class="w-full py-4 bg-[var(--text)] text-[var(--background)] font-bold rounded-2xl"
              >
                Next Step
              </button>
            </div>

            <div v-if="step === 2" class="space-y-4">
              <div>
                <label :class="labelClass">Email Address</label>
                <input
                  type="email"
                  placeholder="name@example.com"
                  :class="inputClass"
                />
              </div>
              <div class="grid grid-cols-2 gap-3">
                <input type="password" placeholder="Pass" :class="inputClass" />
                <input
                  type="password"
                  placeholder="Confirm"
                  :class="inputClass"
                />
              </div>

              <button
                type="button"
                @click="step = 1"
                class="text-[10px] uppercase font-bold text-[var(--subtext)]"
              >
                ← Back
              </button>
            </div>
          </template>

          <button
            v-if="type === 'login' || step === 2"
            type="submit"
            class="w-full py-4 bg-[var(--primary)] text-white font-bold rounded-2xl shadow-lg shadow-[var(--primary)]/20 hover:scale-[1.02] transition-transform"
          >
            {{ type === "login" ? "Sign In" : "Create Account" }}
          </button>
        </form>

        <p class="mt-8 text-center text-xs font-medium text-[var(--subtext)]">
          <NuxtLink
            :to="type === 'login' ? '/signup' : '/login'"
            class="text-[var(--primary)] font-bold hover:underline"
          >
            {{
              type === "login"
                ? "Need an account? Sign Up"
                : "Have an account? Log In"
            }}
          </NuxtLink>
        </p>
      </div>
    </div>
  </div>
</template>
